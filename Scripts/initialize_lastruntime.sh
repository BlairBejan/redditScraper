#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Please enter the amount of time in hours in the past that you would like to start your scrape"
read hours

if [[ "$hours" == "" ]]; then
    echo "$0 - Input is missing."
    exit 1
fi

if [[ "$hours" =~ ^-?[0-9]+$ ]]; then
    datetime=$(date -u -d "$hours hours ago" +"%Y-%m-%d %H:%M:%S%z")
    config_file="$SCRIPT_DIR/../Config/config.json"
    sed -i -E "s/\"last_run\": \"[^\"]+\"/\"last_run\": \"$datetime\"/" "$config_file"
    echo "Updated last_run to $datetime in $config_file" >> "$SCRIPT_DIR/../Logs/scraper.log"
else
    echo -e "\033[0;31m$hours is not a valid input, use a number in hours"
fi
