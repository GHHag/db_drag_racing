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

# Start bigtable

```bash
gcloud beta emulators bigtable start --host-port=127.0.0.1:8086
```

Install requirements, pwd: /db_drag_racing/db-api

```bash
python3 -m venv venv &&
    source venv/bin/activate &&
    python -m pip install --upgrade pip &&
    pip uninstall -r src/requirements.txt -y &&
    pip install -r src/requirements.txt --no-cache-dir &&
    export BIGTABLE_EMULATOR_HOST=127.0.0.1:8086
```

## Run

```bash
python app.py
```

## Exit virual environment

```bash
deactivate
rm -rf venv &&
    sh kill.sh &&
    unset BIGTABLE_EMULATOR_HOST
```
