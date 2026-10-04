# Apply this update to the GitHub repo

## Files in this package

| File | Where to put it in your companion repo |
|------|----------------------------------------|
| `README.md` | **Replace** the existing `README.md` at the repo root |
| `datasets/generate.py` | **New file** at `datasets/generate.py` |
| `datasets/README.md` | **Replace** the existing `datasets/README.md` |
| `Dockerfile.allinone` | **Replace** (fixes namespace to `bilearner`) |
| `build-and-push.ps1` | **Replace** (fixes namespace to `bilearner`) |

## Step-by-step

```powershell
# 1. Go to your companion repo
cd C:\Users\Caption\PycharmProjects\pyspark-1000-examples-companion

# 2. Extract this bundle over the existing files
Expand-Archive -Path "$HOME\Downloads\github-update.zip" -DestinationPath . -Force

# 3. Delete the old stub generator (we're using the real one now)
Remove-Item scripts\generate_datasets.py -ErrorAction SilentlyContinue

# 4. Review what changed
git status

# You should see modifications to:
#   - README.md
#   - Dockerfile.allinone
#   - build-and-push.ps1
#   - datasets/README.md
# And new file:
#   - datasets/generate.py
# And deleted:
#   - scripts/generate_datasets.py

# 5. Commit and push
git add README.md Dockerfile.allinone build-and-push.ps1 datasets/README.md datasets/generate.py
git rm scripts/generate_datasets.py
git commit -m "Add all-in-one practice image, real dataset generator, feature docker pull one-liner"
git push
```

## After the push

Visit https://github.com/bitoollearner/pyspark-1000-examples - verify:

1. **README loads with the one-liner front and center**
2. **datasets/ folder shows generate.py with real content** (480+ lines, not the stub)
3. **No scripts/generate_datasets.py file** (removed)

## Update the About section on GitHub

While you're there, update the repository's About section:

1. On the GitHub repo page, click the gear icon next to "About" (right sidebar)
2. **Description:** 
   `Official companion code for the eBook "PySpark: 1,000 Examples" on Amazon Kindle. 22 chapter notebooks, 1,000 runnable examples, reproducible Docker environment. docker pull bilearner/pyspark1000-practice`
3. **Website:** `https://hub.docker.com/r/bilearner/pyspark1000-practice`
4. **Topics (if not already):** `pyspark`, `apache-spark`, `delta-lake`, `python`, `jupyter`, `data-engineering`, `docker`, `book-companion`

## Verification checklist

- [ ] README's "Quick start" section works when copy-pasted
- [ ] `datasets/generate.py` is the real 480-line version (not the stub)
- [ ] `Dockerfile.allinone` references `bilearner/` not `bitoollearner/`
- [ ] `build-and-push.ps1` references `bilearner/` not `bitoollearner/`
- [ ] Old `scripts/generate_datasets.py` is gone
- [ ] GitHub About section mentions the Docker image

That is the final step. After this your reader experience is:

1. Reader buys book on Amazon Kindle
2. Reader lands at your GitHub README via the book's companion-link
3. Reader copies the one-liner from the top of the README
4. Reader pastes into a terminal with Docker running
5. Reader opens http://localhost:8888 and starts practicing

No build, no clone, no scripts. Three commands from zero to running.
