#!/usr/bin/env bash
## need to fix something, the python file that this calls runs fine on its own but when called from this script
## the db connection that it tries to make times out
cd "$(dirname "$0")"
check_db() {
    if ! tasklist.exe | grep -q mongod.exe; then
        echo "mongodb is not running, please start before running program"
        exit
    fi
}
check_db
echo "Activating virtual environment..."
source ../Environment/bin/activate

echo "Running Python script..."
python3 reset_config.py >> ../Logs/scraper.log 2>&1

echo "Deactivating virtual environment..."
deactivate