#!/usr/bin/env bash

echo "Employee Log Analyzer"

echo "Current directory:"
pwd

echo "Current user:"
whoami

echo "Data files:"
ls data

echo "Total log lines:"
wc -l < data/app.log

echo "Error messages:"
grep "ERROR" data/app.log

echo "Saving error report..."
grep "ERROR" data/app.log > reports/error_summary.txt

echo "Final report:"
cat reports/error_summary.txt