# locust

# Run instructions

Here's how to get started locally. Recommended is to activate a virtual environment (see Setup below).

## Requirements

- Python 3

## Setup

Install requirements, pwd: /db_drag_racing/locust-service

```bash
python3 -m venv venv &&
    source venv/bin/activate &&
    python -m pip install --upgrade pip &&
    pip uninstall -r requirements.txt -y &&
    pip install -r requirements.txt --no-cache-dir
```

## Run

```bash
python locustfile.py
```

## Exit virual environment

```bash
deactivate &&
    rm -rf venv
```
