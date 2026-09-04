# Convenience: regenerate notebooks + chapter indexes in one shot.
# Usage: .\scripts\build_repo.ps1 -BookDir C:\path\to\book\folder

param(
    [Parameter(Mandatory=$true)]
    [string]$BookDir
)

$RepoRoot = Split-Path -Parent $PSScriptRoot

Write-Host ">> Generating notebooks..." -ForegroundColor Cyan
python "$RepoRoot\scripts\generate_notebooks.py" $BookDir
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ""
Write-Host ">> Generating chapter indexes..." -ForegroundColor Cyan
python "$RepoRoot\scripts\generate_chapter_index.py" $BookDir
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ""
Write-Host "Done. Review the generated files, then:" -ForegroundColor Green
Write-Host "  git status"
Write-Host "  git add ."
Write-Host "  git commit -m 'Regenerate notebooks and indexes'"
