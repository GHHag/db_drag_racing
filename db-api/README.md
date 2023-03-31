# db-api

This service wraps Redis (and eventually Bigtable).

## Service logic

1. Request is sent to this API.
2. Service performs get operations to Redis.
3. Service responds with payload.

## Design

- `./src/app.py` - All endpoints
- `./src/clients/*` - All external calls (one client per integration)

# Run instructions

Here's how to get started locally. Recommended is to activate a virtual environment (see Setup below).

## Requirements

- Python 3

## Setup

Install requirements

```bash
python3 -m venv venv &&
    source venv/bin/activate &&
    python -m pip install --upgrade pip &&
    pip uninstall -r src/requirements.txt -y &&
    pip install -r src/requirements.txt --no-cache-dir
```

## Run

```bash
python app.py
```

## Exit virual environment

```bash
deactivate &&
    rm -rf venv
```
