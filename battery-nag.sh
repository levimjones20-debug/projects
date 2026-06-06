#!/bin/bash
BATTERY=$(termux-battery-status | python3 -c "import sys, json; print(json.load(sys.stdin)['percentage'])")
STATUS=$(termux-battery-status | python3 -c "import sys, json; print(json.load(sys.stdin)['status'])")

if [ "$STATUS" != "CHARGING" ] && [ "$BATTERY" -le 20 ]; then
    termux-tts-speak "Hey Levi, your battery is at $BATTERY percent. Plug in your phone you stupid faggot."
    termux-notification --title "🔋 battery nag" --content "you're at $BATTERY%. plug in."
fi
