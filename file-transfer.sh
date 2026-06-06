#!/bin/bash

PC="leviathan@192.168.12.132"
PC_HOME="~"
PHONE_HOME=~

echo "📁 File Transfer"
echo "1) Send file to PC"
echo "2) Get file from PC"
echo "3) Send whole folder to PC"
read -p "Choose (1/2/3): " choice

case $choice in
    1)
        read -p "File to send (full path or ~/...): " file
        read -p "PC destination folder (default ~/Desktop): " dest
        dest=${dest:-~/Desktop}
        scp "${file/#\~/$PHONE_HOME}" $PC:"$dest"
        echo "✅ sent!"
        ;;
    2)
        read -p "File on PC (full path): " file
        read -p "Save to (default ~/): " dest
        dest=${dest:-$PHONE_HOME}
        scp $PC:"$file" "$dest"
        echo "✅ received!"
        ;;
    3)
        read -p "Folder to send (full path or ~/...): " folder
        read -p "PC destination (default ~/Desktop): " dest
        dest=${dest:-~/Desktop}
        scp -r "${folder/#\~/$PHONE_HOME}" $PC:"$dest"
        echo "✅ folder sent!"
        ;;
    *)
        echo "invalid choice"
        ;;
esac
