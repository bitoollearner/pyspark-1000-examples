# Contributing

Thanks for wanting to improve this companion repo! Here's how to help.

## What we welcome

- **Errata reports** — typos, wrong output, broken code, dead links, misleading comments
- **Environment fixes** — Docker/dependency issues that affect readers
- **Notebook improvements** — clearer comments, better inline explanations (of the code, not the book's narrative)
- **New reader tools** — helper scripts that make the examples more accessible

## What we can't accept

- **Book content changes** — we can't add narrative, extra examples, or alternative solutions here. Those belong in a future edition of the book.
- **Republishing the book text** — please don't copy prose from the book into notebook markdown cells.

## How to submit

1. Open an issue first for anything non-trivial — it saves work if we're already fixing it or if the change wouldn't fit.
2. Fork, branch, commit, PR against `main`.
3. Keep changes focused. One PR per concern.
4. Verify notebooks still run in the reference Docker environment:
   ```bash
   docker compose build spark
   docker compose run --rm spark jupyter nbconvert --to notebook --execute notebooks/YOUR_CHAPTER.ipynb
   ```

## Style

- Match the existing tone in the notebooks: concise, focused on running code.
- Use 4-space indentation for Python (Black-formatted, 88 columns).
- Don't add heavyweight dependencies — the point is a minimal, reproducible environment.

## Errata process

If you find a mistake in the **book**, please still file an issue here — we maintain the errata list at `docs/errata.md` and readers benefit from seeing corrections.

For each errata report, include:
- Which chapter and example number
- What the book says
- What it should say
- Your Kindle edition or purchase date if known
