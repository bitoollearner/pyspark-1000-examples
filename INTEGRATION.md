# Integrating the real dataset generator

## What's in this package

| File | Where it goes | What changed |
|------|---------------|--------------|
| `datasets/generate.py` | `datasets/generate.py` (NEW) | The real generator, copied from your book repo |
| `datasets/README.md` | `datasets/README.md` (replace) | Updated to reflect the real file list |
| `build-and-push.ps1` | `build-and-push.ps1` (replace) | Calls real generator with `--core` instead of my stub |
| `Dockerfile.allinone` | `Dockerfile.allinone` (replace) | Added RUN step for `--formats` using the installed Spark |

## Deployment

```powershell
cd C:\Users\Caption\PycharmProjects\pyspark-1000-examples-companion

# Extract the zip over the existing files
Expand-Archive -Path "$HOME\Downloads\datasets-fix.zip" -DestinationPath . -Force

# Delete the old stub generator (it's wrong now)
Remove-Item scripts\generate_datasets.py -ErrorAction SilentlyContinue

# Clear out any datasets the stub produced
Remove-Item datasets\*.csv -ErrorAction SilentlyContinue
Remove-Item datasets\raw -Recurse -ErrorAction SilentlyContinue
Remove-Item datasets\formats -Recurse -ErrorAction SilentlyContinue

# Verify the real generator is in place
Get-ChildItem datasets\generate.py | Select-Object Name, Length
```

## Rebuild

```powershell
.\build-and-push.ps1
```

The script now does three phases:

1. **Phase 1 — Core datasets** (~30 sec): Runs `generate.py --core` in a throwaway `python:3.11-slim` container. Produces 7 CSVs + 10+ raw/ messy files on your host at `./datasets/`.

2. **Phase 2 — Verification**: Checks CSVs count, raw/ folder exists, 22 practice folders ready.

3. **Phase 3 — Docker build** (~5-10 min first time): Builds the practice image. During the build, the Dockerfile runs `generate.py --formats` inside the image — this uses the Spark we install to produce Parquet, ORC, Avro, and Delta variants. The final image contains all three dataset layers.

Expected image size: **~2.5 GB** (was ~2.4 GB with the stub).

## What the reader sees

Inside the running container at `/workspace/datasets/`:

```
datasets/
├── customers.csv          (7 core CSVs)
├── products.csv
├── orders.csv
├── order_items.csv
├── employees.csv
├── web_events.csv
├── transactions.csv
├── raw/                   (10+ messy files for Chapter 4)
│   ├── customers_dirty.csv
│   ├── orders_multiline.json
│   ├── orders_nested.jsonl
│   ├── employees_fixed_width.txt
│   ├── customers.xml
│   ├── products_pipe.txt
│   ├── notes_multiline.csv
│   ├── notes_multiline.csv
│   ├── padded_regions.csv
│   ├── daily/
│   │   ├── 2026-01-01.csv
│   │   ├── 2026-01-02.csv
│   │   ├── 2026-01-03.csv
│   │   └── 2026-01-04.csv
│   └── by_region/
│       ├── region=North/data.csv
│       └── region=South/data.csv
└── formats/               (Chapter 5 and 21 use these)
    ├── parquet/
    │   ├── customers/
    │   ├── orders/
    │   ├── order_items/
    │   ├── products/
    │   └── orders_partitioned/   (partitioned by region, status)
    ├── orc/{customers,orders,order_items,products}/
    ├── avro/{customers,orders,order_items,products}/
    └── delta/{customers,orders,order_items,products}/
```

## Verifying inside the container

After the build, run the image and sanity-check:

```powershell
docker run --rm -it bitoollearner/pyspark1000-practice:1.0 bash -c "ls /workspace/datasets && echo --- && ls /workspace/datasets/raw && echo --- && ls /workspace/datasets/formats"
```

You should see all three layers present.

## Potential issue during the build

The `--formats` step inside the Dockerfile starts a Spark session, which takes ~15 seconds and produces verbose INFO logs (even with WARN level set). This is normal. If it fails with:

- `java.lang.ClassNotFoundException: io.delta.sql.DeltaSparkSessionExtension` — the Delta JAR isn't on the classpath. Check that `spark-defaults.conf` exists at `conf/spark-defaults.conf` and has the `spark.sql.extensions` line.

- `No module named 'pyspark'` — `requirements.txt` wasn't installed. Check `requirements.txt` has `pyspark==3.5.3`.

- Build hangs for 10+ minutes on the format step — probably waiting on a network connection Spark can't reach. Rerun with `--no-cache` to force a fresh build.

If any of these happen, paste the Docker build output and I'll help debug.

## Pushing

Once verified locally:

```powershell
docker push bitoollearner/pyspark1000-practice:1.0
docker push bitoollearner/pyspark1000-practice:latest
```

Or re-run `.\build-and-push.ps1` and answer `y` at the push prompt.
