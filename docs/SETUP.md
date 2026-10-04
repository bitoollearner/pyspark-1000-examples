# Setup Guide

The complete setup for running the 1,000 examples from
**[PySpark: 1,000 Examples](https://www.amazon.com/dp/B0DXXXXXXX)** on your laptop.

**What you need:** A laptop with 4 GB free RAM and 8 GB free disk space.
Windows 10/11, macOS, or Linux all work.

**What you install:** Just one thing - Docker Desktop. That's it. The practice
environment (Spark, Delta Lake, Python, Jupyter, every library, all datasets)
runs inside Docker. Nothing touches your system Python.

**Total time:** About 15 minutes end-to-end.

---

## Step 1 - Install Docker Desktop

### Windows

1. Go to https://www.docker.com/products/docker-desktop/
2. Click **Download for Windows - AMD64** (or ARM64 if you have a Snapdragon laptop)
3. Run the installer `Docker Desktop Installer.exe`
4. On the config screen, keep both defaults checked:
   - Use WSL 2 instead of Hyper-V
   - Add shortcut to desktop
5. Click **OK**. Installation takes 2-3 minutes. You'll be prompted to log out and back in - do that.
6. After logging back in, Docker Desktop launches automatically. Accept the service agreement (free for personal and small-business use).
7. **Skip the Docker tutorial and sign-in prompts** - you don't need them for this book.
8. Open PowerShell and verify:
   ```powershell
   docker --version
   docker compose version
   ```
   You should see something like `Docker version 27.3.1`.

> **If you see "Hardware assisted virtualization not enabled"**: reboot and enable virtualization in your BIOS. Search the web for `enable virtualization <your laptop model>`.

### macOS

1. Go to https://www.docker.com/products/docker-desktop/
2. Download for your chip - **Apple Silicon** (M1/M2/M3/M4) or **Intel chip**
3. Open the downloaded `.dmg`, drag Docker to Applications
4. Launch Docker from Launchpad, accept permissions
5. Verify in Terminal:
   ```bash
   docker --version
   docker compose version
   ```

### Linux (Ubuntu/Debian)

Lighter path - no GUI:

```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker $USER
newgrp docker
docker --version
```

The `usermod` line lets you run `docker` without `sudo`.

---

## Step 2 - Run the practice environment

**Mac / Linux:**

```bash
mkdir -p practice
docker run --rm \
  -p 8888:8888 -p 4040:4040 \
  -v $(pwd)/practice:/workspace/practice \
  bilearner/pyspark1000-practice:1.0
```

**Windows PowerShell:**

```powershell
mkdir practice -Force
docker run --rm `
  -p 8888:8888 -p 4040:4040 `
  -v ${PWD}/practice:/workspace/practice `
  bilearner/pyspark1000-practice:1.0
```

The first run downloads about 2.5 GB (takes 2-5 minutes). After that, each start takes about 10 seconds.

You should see the terminal fill with Jupyter startup messages ending with:

```
http://127.0.0.1:8888/lab/tree/practice
```

### What that command does

- `mkdir practice` - creates a folder on your laptop where your typed notebooks will live. Everything in `practice/` persists on your host.
- `docker run --rm` - starts a container; auto-removes it when stopped (your notebooks stay on your host)
- `-p 8888:8888 -p 4040:4040` - exposes JupyterLab (port 8888) and the Spark UI (port 4040)
- `-v $(pwd)/practice:/workspace/practice` - mounts your host `practice/` folder into the container. Your edits appear on both sides immediately.
- `bilearner/pyspark1000-practice:1.0` - the image name on Docker Hub

### Stay on this terminal

Keep the terminal window open - closing it stops Jupyter. You'll run everything else from your browser.

---

## Step 3 - Open JupyterLab

In your browser, open:

```
http://localhost:8888
```

JupyterLab appears, with the file browser on the left showing 22 chapter folders:

- `chapter-01-introduction/`
- `chapter-02-session/`
- ...
- `chapter-22-patterns/`

Plus top-level folders `datasets/`, `scripts/`, and `docs/`.

**No login or token** - the practice image is configured for local use without authentication.

> **Only use this on your own machine.** The container has no password protection by design. Never expose port 8888 to the public internet.

---

## Step 4 - Open a chapter and run your first example

1. Double-click `chapter-01-introduction/`
2. Double-click `scratch.ipynb`

The notebook opens with:

- A **Chapter setup** cell (already filled with imports and SparkSession)
- A placeholder cell saying "type your first example here"
- An empty code cell

### Run the Chapter setup cell

Click into the Chapter setup code cell. Press **Shift+Enter**. The number next to the cell changes:
- `[ ]` -> `[*]` (running - takes about 10 seconds the first time)
- `[*]` -> `[1]` (done)

A SparkSession object appears below the cell. Your Spark environment is live for the whole chapter.

### Type your first example from the book

1. Open the book on Kindle. Pick Chapter 1, Example 1.
2. In the empty code cell, **type the Solution code from the book** (don't copy-paste from somewhere - the typing is where the learning happens).
3. Shift+Enter.
4. Compare your output to the book's **Output** section.
5. If they match: celebrate briefly, move on.
6. If they don't: read the book's **Common Mistake** section - the trap you just hit is probably listed.

That's the workflow for all 1,000 examples.

---

## Step 5 - Verify the datasets

The book's examples reference datasets at `/workspace/datasets/` inside the container. All of them are pre-generated inside the image - no setup needed.

To browse, click `datasets/` in the JupyterLab sidebar. You should see:

- 7 CSV files (customers, products, orders, order_items, employees, web_events, transactions)
- `raw/` folder with ~15 messy files (dirty CSV, nested JSON, XML, pipe-delimited, etc.)
- `formats/` folder with Parquet, ORC, Avro, and Delta variants

A quick smoke test. In your scratch notebook, type:

```python
customers = spark.read.csv("/workspace/datasets/customers.csv",
                           header=True, inferSchema=True)
customers.show(5)
print(f"Total rows: {customers.count()}")
```

Should print the first 5 customer rows and a total of 500.

---

## Daily workflow after setup

From now on, your routine is:

```bash
# Mac / Linux
docker run --rm -p 8888:8888 -p 4040:4040 \
  -v $(pwd)/practice:/workspace/practice \
  bilearner/pyspark1000-practice:1.0
```

```powershell
# Windows
docker run --rm -p 8888:8888 -p 4040:4040 `
  -v ${PWD}/practice:/workspace/practice `
  bilearner/pyspark1000-practice:1.0
```

Open http://localhost:8888. Keep practicing.

When you're done, press **Ctrl+C** in the terminal (twice if it asks for confirmation). The container stops; your `practice/` folder stays on your laptop.

---

## Troubleshooting

### "Cannot connect to the Docker daemon"
Docker Desktop isn't running. Start it from the Start menu / Applications.

### Port 8888 is already in use
Something else is using the port, usually a leftover Jupyter from another install. Either stop that process, or map a different port:
```bash
docker run --rm -p 8899:8888 ... bilearner/pyspark1000-practice:1.0
```
Then open http://localhost:8899 instead.

### "No chapter folders in practice/"
Your host `practice/` folder was empty but Docker didn't seed it. This happens occasionally with Docker Desktop on Windows. Run once with no volume mount to warm up the image, then retry with the mount:
```powershell
docker run --rm -p 8888:8888 bilearner/pyspark1000-practice:1.0
# Ctrl+C to stop
mkdir practice -Force
docker run --rm -p 8888:8888 -v ${PWD}/practice:/workspace/practice bilearner/pyspark1000-practice:1.0
```

### Container keeps restarting
Not enough memory. Open Docker Desktop -> Settings -> Resources -> bump Memory to 4 GB minimum.

### "No module named pyspark" inside a notebook
You're running JupyterLab outside the container (probably from an Anaconda install you had before). Make sure your browser URL is `http://localhost:8888` (not a different port from a different Jupyter), and that your terminal shows the Docker container's output.

### Spark UI at http://localhost:4040 is blank
The UI only exists while a Spark job is actively running. Run a notebook cell that creates a DataFrame first, then refresh the UI.

### FileNotFoundError on a dataset
Rare - datasets are baked into the image. But if it happens:
```bash
docker exec -it <container-id> ls /workspace/datasets
```
Should list the CSVs. If it doesn't, your image is corrupt - pull again:
```bash
docker pull bilearner/pyspark1000-practice:1.0
```

### Permission errors on Linux (files owned by root)
The image is built to match your host user ID. If files come out root-owned, rebuild the practice folder as your user:
```bash
sudo chown -R $(id -u):$(id -g) practice/
```

### Everything is wrong - start fresh
```bash
docker system prune -af              # removes all unused images and containers
docker pull bilearner/pyspark1000-practice:1.0
# then follow from Step 2 again
```

---

## What next

- **Chapter 1 scratch notebook** (`practice/chapter-01-introduction/scratch.ipynb`) is your first stop
- Browse **[docs/chapters/](chapters/)** to find a specific example by name
- Read the book on **[Amazon Kindle](https://www.amazon.com/dp/B0DXXXXXXX)** for the explanations behind each example
- Found a bug or typo? [Open an issue](../../issues/new/choose)

Happy learning.
