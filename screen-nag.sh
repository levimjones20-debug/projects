#!/bin/bash

LIMIT=30  # minutes
LOGFILE=~/.screen_time_log

# log current time when script runs
echo $(date +%s) >> $LOGFILE

# count entries in last LIMIT minutes
NOW=$(date +%s)
CUTOFF=$((NOW - LIMIT * 60))

COUNT=$(awk -v cutoff=$CUTOFF '$1 > cutoff' $LOGFILE | wc -l)

if [ "$COUNT" -ge "$LIMIT" ]; then
    termux-tts-speak "Levi. Put your phone down. You have been on it for over $LIMIT minutes."
    termux-notification --title "📵 put it down" --content "you've been on your phone too long"
    # reset log
    echo "" > $LOGFILE
fi
