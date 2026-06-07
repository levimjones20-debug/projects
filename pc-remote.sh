#!/bin/bash

PC="leviathan@192.168.12.132"

echo "🎮 PC Remote"
echo "1) Volume up"
echo "2) Volume down"
echo "3) Mute"
echo "4) Play/Pause"
echo "5) PC Status"
echo "6) Sleep PC"
read -p "Choose: " choice

case $choice in
    1) ssh $PC "amixer sset Master 10%+";;
    2) ssh $PC "amixer sset Master 10%-";;
    3) ssh $PC "amixer sset Master toggle";;
    4) ssh $PC "playerctl play-pause";;
    5) ssh $PC "uptime && acpi";;
    6) ssh $PC "systemctl suspend";;
    *) echo "invalid";;
esac
echo "✅ done!"
