#!/usr/bin/env bash

echo "Day 13: Linux Command Line Practice"

echo "Current directory:"
pwd

echo "Current user:"
whoami

echo "Files in the current directory:"
ls

echo "Total lines in the application log:"
wc -l < data/app.log

echo "Errors in the application log:"
grep "ERROR" data/app.log

echo "Saving errors to a report..."
grep "ERROR" data/app.log > reports/errors.txt

echo "Report contents:"
cat reports/errors.txt

echo "Linux practice completed"