#!/usr/bin/env bash

cd "$(dirname "$0")"
source Environment/bin/activate
cd Scripts
python3 redditscraper.py >> ../Logs/scraper.log 2>&1
deactivate
