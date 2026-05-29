#!/bin/bash
echo "Music backup - $(date)" >> ~/music_log.txt
ls -R ~/Music >> ~/music_log.txt
echo "---" >> ~/music_log.txt
