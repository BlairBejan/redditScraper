#!/usr/bin/env bash

cd "$(dirname "$0")"

check_db() {
    if ! tasklist.exe | grep -q mongod.exe; then
        echo "mongodb is not running, please start before running program"
        exit
}
check_db
source Environment/bin/activate
cd Scripts
python3 redditscraper.py >> ../Logs/scraper.log 2>&1
deactivate
