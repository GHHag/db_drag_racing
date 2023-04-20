#!/bin/sh
echo "Unbinding bigtable emulator address..."
PID_OCCUPYING_PORT=$(lsof -t -i :8086 -s TCP:LISTEN)
kill -9 $PID_OCCUPYING_PORT
echo "Done."