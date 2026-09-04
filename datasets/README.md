# Seeded datasets

The book's examples reference a small set of realistic seeded datasets:

| File | Rows | Purpose |
|------|------|---------|
| `orders.csv` | 10,000 | Order records for filter/group/join examples |
| `customers.csv` | 1,000 | Customer master data for joins |
| `products.csv` | 500 | Product catalog with prices |
| `events.json` | 5,000 | Event stream (nested JSON) for complex-type examples |
| `sales.parquet` | 50,000 | Fact table for aggregation/window examples |

## Regenerating

These files are `.gitignore`d so the repo stays small. Regenerate them from a
fixed seed (results are byte-identical):

```bash
docker compose run --rm spark python scripts/generate_datasets.py
```

The script uses [Faker](https://faker.readthedocs.io/) with a fixed seed
(`SEED=42`) so everyone gets the same data.

If you want to check them in for reproducibility, remove the `datasets/*`
lines from `.gitignore`.
