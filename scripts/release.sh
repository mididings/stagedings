#!/usr/bin/env bash

set -e

VERSION=$(grep '^version =' pyproject.toml | cut -d'"' -f2)

echo "========================================"
echo " Cleaning previous artifacts"
echo "========================================"

rm -rf .venv
rm -rf build
rm -rf dist
rm -rf *.egg-info
find . -type d -name "*.egg-info" -exec rm -rf {} +

echo "========================================"
echo " Creating virtual environment"
echo "========================================"

python3 -m venv .venv
source .venv/bin/activate

echo "========================================"
echo " Upgrading packaging tools"
echo "========================================"

python -m pip install --upgrade pip setuptools wheel

echo "========================================"
echo " Installing build and twine"
echo "========================================"

pip install build twine

echo "========================================"
echo " Building package"
echo "========================================"

python -m build

echo "========================================"
echo " Checking package metadata"
echo "========================================"

twine check dist/*

echo "========================================"
echo " Uploading to PyPI"
echo "========================================"

twine upload --repository pypi dist/*

echo "========================================"
echo " Purging pip cache"
echo "========================================"

pip cache purge || true

echo "======================================="
echo "=== Waiting for PyPI installability ==="
echo "======================================="

PACKAGE="stagedings"
VERSION="${VERSION}"

for i in {1..20}; do
    echo "Check $i/20: trying install simulation for ${PACKAGE}==${VERSION}"

    if pip install \
        --dry-run \
        --no-cache-dir \
        --index-url https://pypi.org/simple/ \
        "${PACKAGE}==${VERSION}" >/dev/null 2>&1; then

        echo "✓ Version is installable"
        break
    fi

    echo "Not ready yet... sleeping 5s"
    sleep 5

    if [ "$i" -eq 20 ]; then
        echo "❌ Timeout: version still not installable"
        exit 1
    fi
done

echo "========================================"
echo " Installing package from PyPI"
echo "========================================"

pip install \
    --no-cache-dir \
    --index-url https://pypi.org/simple/ \
    stagedings=="${VERSION}"

echo "========================================"
echo " Installed packages"
echo "========================================"

pip list

echo "========================================"
echo " Package information"
echo "========================================"

pip show stagedings

echo "========================================"
echo " Launching stagedings"
echo "========================================"

stagedings