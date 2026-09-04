#!/usr/bin/env python3
"""
Regenerate the seeded reference datasets used across the book's examples.

Uses a fixed random seed so every reader gets byte-identical files.
Output: ./datasets/*.csv, ./datasets/*.json, ./datasets/*.parquet

Usage:
    docker compose run --rm spark python scripts/generate_datasets.py

Or with a Python env that has faker + pandas + pyarrow installed:
    python scripts/generate_datasets.py

Add or edit datasets by editing the functions below.

NOTE FOR THE BOOK AUTHOR: replace this template with your actual dataset
generator from the private book repo (make.ps1 -> `datasets` target).
The stub below generates a minimal set — enough to smoke-test the container
but not the full data the book examples reference.
"""
from pathlib import Path
import random

from faker import Faker
import pandas as pd

SEED = 42
DATASETS_DIR = Path(__file__).parent.parent / "datasets"


def gen_customers(fake, n=1000):
    """Customer master table."""
    rows = []
    for i in range(n):
        rows.append({
            "customer_id": i + 1,
            "name": fake.name(),
            "email": fake.email(),
            "country": fake.country_code(),
            "signup_date": fake.date_between("-3y", "today"),
        })
    return pd.DataFrame(rows)


def gen_products(fake, n=500):
    """Product catalog."""
    rows = []
    for i in range(n):
        rows.append({
            "product_id": i + 1,
            "sku": f"SKU-{i+1:05d}",
            "category": random.choice(["Books", "Electronics", "Home", "Toys", "Grocery"]),
            "price": round(random.uniform(1.99, 299.99), 2),
        })
    return pd.DataFrame(rows)


def gen_orders(fake, n_customers=1000, n_products=500, n=10000):
    """Orders fact table."""
    rows = []
    for i in range(n):
        rows.append({
            "order_id": i + 1,
            "customer_id": random.randint(1, n_customers),
            "product_id": random.randint(1, n_products),
            "quantity": random.randint(1, 5),
            "status": random.choice(["pending", "paid", "shipped", "delivered", "cancelled"]),
            "order_date": fake.date_time_between("-1y", "now").isoformat(sep=" "),
        })
    return pd.DataFrame(rows)


def main():
    DATASETS_DIR.mkdir(exist_ok=True)
    random.seed(SEED)
    fake = Faker()
    Faker.seed(SEED)

    print("Generating customers.csv...")
    customers = gen_customers(fake)
    customers.to_csv(DATASETS_DIR / "customers.csv", index=False)

    print("Generating products.csv...")
    products = gen_products(fake)
    products.to_csv(DATASETS_DIR / "products.csv", index=False)

    print("Generating orders.csv...")
    orders = gen_orders(fake)
    orders.to_csv(DATASETS_DIR / "orders.csv", index=False)

    # Add more here to match what the book uses:
    #   events.json, sales.parquet, etc.

    print("\nDone.")
    for p in sorted(DATASETS_DIR.glob("*")):
        if p.name.startswith("."):
            continue
        size_kb = p.stat().st_size / 1024
        print(f"  {p.name}: {size_kb:,.1f} KB")


if __name__ == "__main__":
    main()
