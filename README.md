# Python Learning Collection

This repository contains a collection of small Python examples and exercises organized by topic. It's intended as a personal learning workspace with runnable snippets and simple tasks.

## Structure
- `conditional_statement/` — examples of `if` statements
- `dataType/` — basic data type demos and sequences
- `dayOne/` — first-day exercises
- `Exception_handling/` — exception handling examples
- `FileHandling/` — file I/O examples (includes `msg.txt`)
- `function/` — functions, arguments, decorators, iterators
- `loop/` — loop examples and list comprehensions
- `module/` — module examples and external usage
- `oop/` — object-oriented programming examples
- `operator/` — operator precedence and usage
- `practice ` — practice scripts and problem solving
- `task/` — larger tasks and mini-projects (e.g., `atm.py`, `bank.py`)
- `variable/` — variable examples

## Quick Start

1. Clone the repo (if you haven't already):

   git clone https://github.com/SuzanLama433/Python_learning.git

2. (Optional) Create or activate the virtual environment on macOS:

   python3 -m venv venv
   source venv/bin/activate

3. Run a script, for example the ATM demo:

   python task/atm.py

## Contributing
- Add small, focused examples under the appropriate folder.
- Keep scripts runnable and avoid hard-coded paths.

## Git / GitHub: Add README and push

If you want to add this README and push it to the existing remote, run:

```
cd /Users/sujan/Desktop/python
git add README.md
git commit -m "Add README"
git push origin main
```

Replace `main` with your branch name if different. Pushing may prompt for credentials depending on your Git configuration.

## Notes
- This repo contains a local `venv/` directory; consider adding it to `.gitignore` if you don't want to push it to GitHub.
- Many scripts are intended for educational use; review inputs before running.

---
Created for easy navigation and quick demos.

## Repository

This repository is hosted at: https://github.com/SuzanLama433/Python_learning

README last updated: 2026-06-07.

## Recommended .gitignore

This project contains a local `venv/` folder. It's recommended to add a `.gitignore` file including at least:

- `venv/`
- `__pycache__/`
- `*.pyc`
- `.DS_Store`

You can create a `.gitignore` at the repo root and commit it to avoid pushing virtualenv and cache files.
