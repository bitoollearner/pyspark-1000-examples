# ----------------------------------------------------------------------------
# build-and-push.ps1
# Builds the practice Docker image and (optionally) pushes it to Docker Hub.
# Run from the root of your companion repo folder.
#
# Two-phase dataset generation:
#   Phase 1 (here): runs --core in a throwaway python:3.11-slim container.
#                   Produces 7 CSVs + raw/ messy files. No Spark needed.
#   Phase 2 (in the Dockerfile): runs --formats as a RUN step. Uses the
#                   Spark we install in the image to produce parquet/orc/
#                   avro/delta variants.
# ----------------------------------------------------------------------------

param(
    [string]$Version = "1.0",
    [string]$Image   = "bilearner/pyspark1000-practice"
)

$ErrorActionPreference = "Stop"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  PySpark 1,000 Examples - Practice Image" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# --- Preflight: Docker must be running --------------------------------------
try {
    docker version --format '{{.Server.Version}}' | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Docker not responsive" }
}
catch {
    throw "Docker Desktop is not running. Start it from the Start menu, then rerun this script."
}

# --- Preflight: real generator must exist -----------------------------------
if (-not (Test-Path "datasets\generate.py")) {
    throw "Missing datasets/generate.py. Copy the real generator from your book repo (datasets/generate.py) into this companion repo before running this script."
}

# --- 1. Generate core datasets (CSV + raw) via throwaway Python container --
Write-Host ">> [1/3] Generating core datasets + raw messy files (no Spark needed)..." -ForegroundColor Yellow

$WorkDir = $PWD.Path.Replace("\", "/")

docker run --rm `
    -v "${WorkDir}:/workspace" `
    -w /workspace `
    python:3.11-slim `
    bash -c "pip install --quiet faker==30.8.2 pandas==2.2.3 && python datasets/generate.py --core"

if ($LASTEXITCODE -ne 0) {
    throw "Core dataset generation failed. See errors above."
}

# --- 2. Verify content -----------------------------------------------------
Write-Host ""
Write-Host ">> [2/3] Verifying content ..." -ForegroundColor Yellow
$csvs     = Get-ChildItem datasets\*.csv -ErrorAction SilentlyContinue
$rawDir   = Get-Item datasets\raw -ErrorAction SilentlyContinue
$rawFiles = if ($rawDir) { Get-ChildItem datasets\raw -Recurse -File } else { @() }
$practice = Get-ChildItem practice-template\chapter-* -Directory -ErrorAction SilentlyContinue

Write-Host "   Core CSVs:       $($csvs.Count) files"
Write-Host "   Raw messy files: $($rawFiles.Count) files (in datasets/raw/)"
Write-Host "   Practice dirs:   $($practice.Count) chapter folders"

if ($csvs.Count -lt 6)       { throw "Expected 7 core CSVs, found $($csvs.Count). Check generator output above." }
if (-not $rawDir)            { throw "datasets/raw/ folder not created." }
if ($rawFiles.Count -lt 10)  { throw "Expected 10+ raw messy files, found $($rawFiles.Count)." }
if ($practice.Count -lt 22)  { throw "Expected 22 chapter folders in practice-template/, found $($practice.Count)." }

# --- 3. Build the Docker image (also runs --formats inside) ----------------
Write-Host ""
Write-Host ">> [3/3] Building image ${Image}:${Version} ..." -ForegroundColor Yellow
Write-Host "   (The Dockerfile runs 'generate.py --formats' as a RUN step"
Write-Host "    to produce parquet/orc/avro/delta variants. Adds ~1-2 min.)"
Write-Host ""
docker build `
    -t "${Image}:${Version}" `
    -t "${Image}:latest" `
    -f Dockerfile.allinone `
    .
if ($LASTEXITCODE -ne 0) { throw "Docker build failed" }

Write-Host ""
Write-Host "Image built. Local sanity check:" -ForegroundColor Green
Write-Host "   docker run --rm -p 8888:8888 -p 4040:4040 ${Image}:${Version}"
Write-Host "   # then open http://localhost:8888/lab"
Write-Host ""

$push = Read-Host "Push to Docker Hub now? (y/N)"
if ($push -eq "y" -or $push -eq "Y") {
    Write-Host ""
    Write-Host "Pushing ${Image}:${Version} (upload ~2.5 GB, 5-20 min)..." -ForegroundColor Yellow
    docker push "${Image}:${Version}"
    if ($LASTEXITCODE -ne 0) { throw "Push of :${Version} failed" }

    docker push "${Image}:latest"
    if ($LASTEXITCODE -ne 0) { throw "Push of :latest failed" }

    Write-Host ""
    Write-Host "Done. Image is live at:" -ForegroundColor Green
    Write-Host "   https://hub.docker.com/r/$Image"
} else {
    Write-Host "Skipped push. When ready, run:" -ForegroundColor Yellow
    Write-Host "   docker push ${Image}:${Version}"
    Write-Host "   docker push ${Image}:latest"
}
