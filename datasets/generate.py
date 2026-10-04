#!/usr/bin/env python3
"""
Generate the canonical dataset spine for the book.

Everything is seeded, so regenerating produces byte-identical files. That
matters: every ``**Output**`` block in the book is diffed against real Spark
output by ``scripts/validate.py``. If the data shifts, 1,000 examples break.

    python datasets/generate.py --all           # CSVs + raw files + formats
    python datasets/generate.py --core          # CSVs only (no Spark needed)
    python datasets/generate.py --formats       # parquet/orc/avro/delta/xml
    python datasets/generate.py --all --scale 5 # 5x rows, for the perf chapter

Datasets
--------
customers      dimensions, nulls, SCD Type 1/2, joins
products       pivots, categories, broadcast joins
orders         the fact table - groupBy, aggregations, joins
order_items    line-level grain, explode/aggregate practice
employees      hierarchy and salaries - windows, ranking, rowsBetween
web_events     sessionization, gap detection, time series
transactions   fraud patterns, running totals
raw/           one deliberately broken file per format
"""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
from faker import Faker

SEED = 20240816
HERE = Path(__file__).resolve().parent

N_CUSTOMERS = 500
N_PRODUCTS = 80
N_ORDERS = 2_000
N_EMPLOYEES = 120
N_EVENTS = 5_000
N_TRANSACTIONS = 3_000

START = datetime(2023, 1, 1)
CATEGORIES = ["Electronics", "Apparel", "Home", "Grocery", "Sports", "Books"]
REGIONS = ["North", "South", "East", "West"]
CHANNELS = ["web", "mobile", "store", "partner"]
DEPARTMENTS = ["Engineering", "Sales", "Marketing", "Finance", "Support"]


def new_faker() -> Faker:
    fake = Faker("en_US")
    Faker.seed(SEED)
    random.seed(SEED)
    return fake


# --------------------------------------------------------------------------
# core tables
# --------------------------------------------------------------------------
def build_customers(fake: Faker, scale: int) -> pd.DataFrame:
    rows = []
    for i in range(1, N_CUSTOMERS * scale + 1):
        signup = START + timedelta(days=random.randint(0, 600))
        rows.append(
            {
                "customer_id": i,
                "customer_name": fake.name(),
                "email": fake.email() if random.random() > 0.08 else None,
                "city": fake.city(),
                "region": random.choice(REGIONS),
                "country": "US",
                "signup_date": signup.date().isoformat(),
                "segment": random.choice(["consumer", "smb", "enterprise"]),
                "credit_limit": (
                    round(random.uniform(500, 25_000), 2)
                    if random.random() > 0.05
                    else None
                ),
                "is_active": random.random() > 0.15,
            }
        )
    return pd.DataFrame(rows)


def build_products(scale: int) -> pd.DataFrame:
    rows = []
    for i in range(1, N_PRODUCTS * scale + 1):
        category = random.choice(CATEGORIES)
        rows.append(
            {
                "product_id": i,
                "product_name": f"{category[:4].upper()}-{i:04d}",
                "category": category,
                "subcategory": f"{category} {random.choice('ABC')}",
                "unit_price": round(random.uniform(4.99, 899.00), 2),
                "cost": None,
                "supplier_id": random.randint(1, 12),
                "discontinued": random.random() < 0.1,
            }
        )
    df = pd.DataFrame(rows)
    df["cost"] = (df["unit_price"] * pd.Series(
        [random.uniform(0.45, 0.8) for _ in range(len(df))]
    )).round(2)
    return df


def build_orders(scale: int) -> tuple[pd.DataFrame, pd.DataFrame]:
    orders, items = [], []
    item_id = 1
    for order_id in range(1, N_ORDERS * scale + 1):
        ordered = START + timedelta(
            days=random.randint(0, 700), minutes=random.randint(0, 1439)
        )
        status = random.choices(
            ["completed", "shipped", "pending", "cancelled", "returned"],
            weights=[60, 18, 10, 7, 5],
        )[0]
        shipped = (
            (ordered + timedelta(days=random.randint(1, 9))).isoformat(sep=" ")
            if status in ("completed", "shipped") and random.random() > 0.06
            else None
        )
        orders.append(
            {
                "order_id": order_id,
                "customer_id": random.randint(1, N_CUSTOMERS * scale),
                "order_ts": ordered.isoformat(sep=" "),
                "ship_ts": shipped,
                "status": status,
                "channel": random.choice(CHANNELS),
                "region": random.choice(REGIONS),
            }
        )
        for _ in range(random.randint(1, 5)):
            quantity = random.randint(1, 8)
            price = round(random.uniform(4.99, 899.00), 2)
            items.append(
                {
                    "order_item_id": item_id,
                    "order_id": order_id,
                    "product_id": random.randint(1, N_PRODUCTS * scale),
                    "quantity": quantity,
                    "unit_price": price,
                    "discount_pct": random.choice([0, 0, 0, 5, 10, 15, 20]),
                    "line_total": round(quantity * price, 2),
                }
            )
            item_id += 1
    return pd.DataFrame(orders), pd.DataFrame(items)


def build_employees(fake: Faker, scale: int) -> pd.DataFrame:
    """Deliberately shaped for window functions: managers, ties, one CEO."""
    rows = [
        {
            "employee_id": 1,
            "employee_name": fake.name(),
            "manager_id": None,
            "department": "Executive",
            "job_title": "CEO",
            "hire_date": "2015-03-02",
            "salary": 320_000,
            "region": "North",
        }
    ]
    for i in range(2, N_EMPLOYEES * scale + 1):
        department = random.choice(DEPARTMENTS)
        hire = START - timedelta(days=random.randint(0, 2600))
        rows.append(
            {
                "employee_id": i,
                "employee_name": fake.name(),
                "manager_id": 1 if i <= 6 else random.randint(2, min(i - 1, 6)),
                "department": department,
                "job_title": random.choice(
                    ["Analyst", "Engineer", "Manager", "Lead", "Associate"]
                ),
                "hire_date": hire.date().isoformat(),
                "salary": random.randrange(55_000, 210_000, 5_000),
                "region": random.choice(REGIONS),
            }
        )
    return pd.DataFrame(rows)


def build_web_events(scale: int) -> pd.DataFrame:
    """Bursty sessions with deliberate gaps - sessionization fodder."""
    rows = []
    event_id = 1
    for user in range(1, 300 * scale + 1):
        cursor = START + timedelta(days=random.randint(0, 700))
        for _ in range(random.randint(1, 4)):
            cursor += timedelta(minutes=random.randint(45, 900))
            for _ in range(random.randint(2, 12)):
                cursor += timedelta(seconds=random.randint(5, 900))
                rows.append(
                    {
                        "event_id": event_id,
                        "user_id": user,
                        "event_ts": cursor.isoformat(sep=" "),
                        "event_type": random.choices(
                            ["page_view", "click", "add_to_cart", "purchase"],
                            weights=[70, 20, 7, 3],
                        )[0],
                        "page": random.choice(
                            ["/home", "/search", "/product", "/cart", "/checkout"]
                        ),
                        "device": random.choice(["desktop", "mobile", "tablet"]),
                        "session_hint": None,
                    }
                )
                event_id += 1
                if event_id > N_EVENTS * scale:
                    return pd.DataFrame(rows)
    return pd.DataFrame(rows)


def build_transactions(scale: int) -> pd.DataFrame:
    """Includes a small planted set of fraud-shaped patterns."""
    rows = []
    for i in range(1, N_TRANSACTIONS * scale + 1):
        ts = START + timedelta(
            days=random.randint(0, 700), seconds=random.randint(0, 86_399)
        )
        fraudulent = random.random() < 0.02
        rows.append(
            {
                "txn_id": i,
                "account_id": random.randint(1, 400 * scale),
                "txn_ts": ts.isoformat(sep=" "),
                "amount": round(
                    random.uniform(2_000, 9_500) if fraudulent
                    else random.uniform(3.5, 450),
                    2,
                ),
                "currency": random.choice(["USD", "EUR", "GBP"])
                if fraudulent
                else "USD",
                "merchant": random.choice(
                    ["AcmeMart", "GlobalGas", "NetFlix", "SkyAir", "CoffeeCo"]
                ),
                "country": random.choice(["US", "US", "US", "RO", "NG"])
                if fraudulent
                else "US",
                "is_flagged": fraudulent,
            }
        )
    return pd.DataFrame(rows)


# --------------------------------------------------------------------------
# deliberately messy raw files (Chapters 4 and 13)
# --------------------------------------------------------------------------
def build_raw_files(raw: Path, customers: pd.DataFrame) -> None:
    raw.mkdir(parents=True, exist_ok=True)

    (raw / "customers_dirty.csv").write_text(
        "customer_id,customer_name,city,signup_date,credit_limit\n"
        "1,Alice Chen,Denver,2023-04-01,5000\n"
        "2,Bob \"The Builder\" Ray,Austin,2023-04-02,7500\n"
        "3,Carla Diaz,Miami,not-a-date,8000\n"
        "\n"
        "4,Dan Okafor,Lagos,2023-04-05,1200,EXTRA_COLUMN\n"
        "5,Eve Brandt,,2023-04-06,\n"
        "6,Frank Ito,Oslo,2023-04-07,unknown\n",
        encoding="utf-8",
    )

    (raw / "orders_multiline.json").write_text(
        json.dumps(
            [
                {"order_id": 1, "customer_id": 1, "total": 120.5},
                {"order_id": 2, "customer_id": 2, "total": 89.0},
            ],
            indent=2,
        ),
        encoding="utf-8",
    )

    with (raw / "orders_nested.jsonl").open("w", encoding="utf-8") as handle:
        for order_id in range(1, 26):
            handle.write(
                json.dumps(
                    {
                        "order_id": order_id,
                        "customer": {
                            "id": order_id,
                            "name": f"Customer {order_id}",
                            "address": {
                                "city": random.choice(["Denver", "Austin", "Miami"]),
                                "zip": f"{random.randint(10000, 99999)}",
                            },
                        },
                        "items": [
                            {"sku": f"SKU{n:03d}", "qty": random.randint(1, 4)}
                            for n in range(1, random.randint(2, 5))
                        ],
                        "tags": random.sample(["gift", "rush", "b2b", "repeat"], 2),
                    }
                )
                + "\n"
            )

    with (raw / "employees_fixed_width.txt").open("w", encoding="utf-8") as handle:
        for i in range(1, 21):
            handle.write(
                f"{i:05d}{'Employee ' + str(i):<25}{'Engineering':<15}"
                f"{random.randrange(60000, 180000, 5000):>08d}\n"
            )

    rows = "\n".join(
        f"  <customer id=\"{r.customer_id}\">\n"
        f"    <name>{r.customer_name}</name>\n"
        f"    <city>{r.city}</city>\n"
        f"  </customer>"
        for r in customers.head(20).itertuples()
    )
    (raw / "customers.xml").write_text(
        f"<?xml version=\"1.0\"?>\n<customers>\n{rows}\n</customers>\n",
        encoding="utf-8",
    )

    (raw / "products_pipe.txt").write_text(
        "product_id|product_name|price\n1|Cafe Grinder|89.99\n2|Naive Notebook|4.50\n",
        encoding="utf-8",
    )

    (raw / "notes_multiline.csv").write_text(
        'order_id,note\n'
        '1,"Customer called.\nAsked for a refund."\n'
        '2,"Single line note"\n'
        '3,"Delivered late.\nApology sent.\nCredit applied."\n',
        encoding="utf-8",
    )

    daily = raw / "daily"
    daily.mkdir(parents=True, exist_ok=True)
    daily_rows = {
        "2026-01-01": [(1, "North", 120.0), (2, "South", 340.0)],
        "2026-01-02": [(3, "East", 90.0), (4, "North", 275.0)],
        "2026-01-03": [(5, "West", 410.0)],
    }
    for day, rows in daily_rows.items():
        lines = ["order_id,region,amount"]
        lines += [f"{oid},{region},{amount}" for oid, region, amount in rows]
        (daily / f"{day}.csv").write_text("\n".join(lines) + "\n", encoding="utf-8")

    (daily / "2026-01-04.csv").write_text(
        "order_id,region,amount,channel\n6,South,150.0,web\n",
        encoding="utf-8",
    )

    (raw / "padded_regions.csv").write_text(
        "order_id, region , amount\n"
        "1,  North  ,120.0\n"
        "2, South,340.0\n"
        "3,East  ,90.0\n",
        encoding="utf-8",
    )

    for region in ("North", "South"):
        part = raw / "by_region" / f"region={region}"
        part.mkdir(parents=True, exist_ok=True)
        (part / "data.csv").write_text(
            "order_id,amount\n"
            + ("10,500.0\n11,250.0\n" if region == "North" else "12,80.0\n"),
            encoding="utf-8",
        )


# --------------------------------------------------------------------------
# binary formats (needs Spark)
# --------------------------------------------------------------------------
def build_formats(base: Path) -> None:
    from pyspark.sql import SparkSession

    spark = (
        SparkSession.builder.appName("dataset-formats")
        .master("local[*]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    formats = base / "formats"
    for name in ("customers", "orders", "order_items", "products"):
        df = spark.read.option("header", True).option(
            "inferSchema", True
        ).csv(str(base / f"{name}.csv"))

        df.write.mode("overwrite").parquet(str(formats / "parquet" / name))
        df.write.mode("overwrite").orc(str(formats / "orc" / name))
        df.write.mode("overwrite").format("avro").save(str(formats / "avro" / name))
        df.write.mode("overwrite").format("delta").save(str(formats / "delta" / name))

    orders = spark.read.option("header", True).option("inferSchema", True).csv(
        str(base / "orders.csv")
    )
    orders.write.mode("overwrite").partitionBy("region", "status").parquet(
        str(formats / "parquet" / "orders_partitioned")
    )

    spark.stop()
    print(f"  formats -> {formats}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--all", action="store_true", help="core + raw + formats")
    parser.add_argument("--core", action="store_true", help="CSV tables only")
    parser.add_argument("--formats", action="store_true", help="parquet/orc/avro/delta")
    parser.add_argument("--scale", type=int, default=1, help="row multiplier")
    parser.add_argument("--out", default=str(HERE), help="output directory")
    args = parser.parse_args()

    if not (args.all or args.core or args.formats):
        parser.error("pick one of --all, --core, --formats")

    base = Path(args.out)
    base.mkdir(parents=True, exist_ok=True)

    if args.all or args.core:
        fake = new_faker()
        customers = build_customers(fake, args.scale)
        products = build_products(args.scale)
        orders, order_items = build_orders(args.scale)
        employees = build_employees(fake, args.scale)
        web_events = build_web_events(args.scale)
        transactions = build_transactions(args.scale)

        tables = {
            "customers": customers,
            "products": products,
            "orders": orders,
            "order_items": order_items,
            "employees": employees,
            "web_events": web_events,
            "transactions": transactions,
        }
        for name, frame in tables.items():
            target = base / f"{name}.csv"
            frame.to_csv(target, index=False)
            print(f"  {name:<14} {len(frame):>7,} rows -> {target.name}")

        build_raw_files(base / "raw", customers)
        print(f"  raw files      -> {base / 'raw'}")

    if args.all or args.formats:
        build_formats(base)

    print("\nDone. Datasets are seeded - regenerating gives identical files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
