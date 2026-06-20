#!/usr/bin/env python3
"""
Lightweight runner to start stagedings.cli without installing the package.

Usage:
  python run_cli.py --host 0.0.0.0 --port 5000

It prepends the project's `src/` directory to `sys.path` so the `stagedings`
package can be imported directly from the repository.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def main():
    # Import and run the package's CLI main() which uses argparse
    from stagedings.cli import main as cli_main
    cli_main()


if __name__ == "__main__":
    main()
