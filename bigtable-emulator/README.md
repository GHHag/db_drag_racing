# bigtable-emulator

Bigtable-emulator for local testing purposes.
https://cloud.google.com/sdk/docs/install-sdk
https://cloud.google.com/bigtable/docs/emulator

# Run instructions

Here's how to get started locally. Recommended is to activate a virtual environment (see Setup below).

## Requirements

- UNIX-based OS.
- Gcloud CLI installed on local machine.

## Startup

```bash
gcloud beta emulators bigtable start --host-port=127.0.0.1:8086
export BIGTABLE_EMULATOR_HOST=127.0.0.1:8086
```

## Exit

When you are finished using the emulator, type Control-C to stop the emulator, then unset BIGTABLE_EMULATOR_HOST with the following command:

```bash
sh kill.sh && \
  unset BIGTABLE_EMULATOR_HOST
```
