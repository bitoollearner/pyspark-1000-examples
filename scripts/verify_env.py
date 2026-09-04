#!/usr/bin/env python3
"""
Sanity-check that the reader's environment can run the book's examples.

Verifies:
  1. PySpark 3.5.x is importable
  2. A SparkSession starts
  3. Delta Lake JARs are on the classpath
  4. Datasets folder exists (or gives instructions)
  5. Runs a trivial groupBy to prove the whole stack works

Usage:
    docker compose run --rm spark python scripts/verify_env.py
    # or, on a host with pyspark installed:
    python scripts/verify_env.py
"""
import sys
from pathlib import Path


def check(label, ok, details=""):
    mark = "OK  " if ok else "FAIL"
    print(f"[{mark}] {label}")
    if details:
        print(f"       {details}")
    return ok


def main():
    all_ok = True

    # ---- 1. pyspark importable ----------------------------------------
    try:
        import pyspark
        version = pyspark.__version__
        ok = version.startswith("3.5")
        all_ok &= check(
            "PySpark import",
            ok,
            f"Version: {version} (expected 3.5.x for full parity with the book)",
        )
    except ImportError as e:
        return check("PySpark import", False, str(e))

    # ---- 2. spark session ---------------------------------------------
    try:
        from pyspark.sql import SparkSession
        spark = (
            SparkSession.builder
            .master("local[*]")
            .appName("verify_env")
            .config("spark.ui.enabled", "false")
            .getOrCreate()
        )
        spark.sparkContext.setLogLevel("ERROR")
        all_ok &= check("SparkSession start", True, f"Session: {spark.version}")
    except Exception as e:
        return check("SparkSession start", False, str(e))

    # ---- 3. delta on classpath ----------------------------------------
    try:
        jvm = spark._jvm
        _ = jvm.io.delta.tables.DeltaTable
        all_ok &= check("Delta Lake JARs", True)
    except Exception:
        all_ok &= check(
            "Delta Lake JARs",
            False,
            "delta-spark JAR not on classpath. If using Docker, ensure the image was built from this repo's Dockerfile.",
        )

    # ---- 4. datasets folder -------------------------------------------
    root = Path(__file__).parent.parent
    ds = root / "datasets"
    have_data = any(ds.glob("*.csv"))
    all_ok &= check(
        "Datasets present",
        have_data,
        "Run: python scripts/generate_datasets.py" if not have_data else str(ds),
    )

    # ---- 5. minimal end-to-end run ------------------------------------
    try:
        from pyspark.sql import functions as F
        df = spark.range(1000).withColumn("bucket", F.col("id") % 10)
        counts = df.groupBy("bucket").count().orderBy("bucket").collect()
        ok = len(counts) == 10 and counts[0]["count"] == 100
        all_ok &= check("End-to-end groupBy", ok, f"10 buckets of 100 rows each: {ok}")
    except Exception as e:
        all_ok &= check("End-to-end groupBy", False, str(e))

    spark.stop()

    print()
    if all_ok:
        print("Environment looks good. You can open any notebook in notebooks/ and start running examples.")
        return 0
    else:
        print("Some checks failed. See details above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
