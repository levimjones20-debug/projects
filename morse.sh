#!/bin/bash

declare -A MORSE
MORSE=(
[A]=".-" [B]="-..." [C]="-.-." [D]="-.." [E]="."
[F]="..-." [G]="--." [H]="...." [I]=".." [J]=".---"
[K]="-.-" [L]=".-.." [M]="--" [N]="-." [O]="---"
[P]=".--." [Q]="--.-" [R]=".-." [S]="..." [T]="-"
[U]="..-" [V]="...-" [W]=".--" [X]="-..-" [Y]="-.--"
[Z]="--.." [0]="-----" [1]=".----" [2]="..---" [3]="...--"
[4]="....-" [5]="....." [6]="-...." [7]="--..." [8]="---.."
[9]="----."
)

read -p "Message to flash: " message
message=$(echo "$message" | tr '[:lower:]' '[:upper:]')

for ((i=0; i<${#message}; i++)); do
    char="${message:$i:1}"
    if [ "$char" = " " ]; then
        sleep 0.7
        continue
    fi
    code="${MORSE[$char]}"
    for ((j=0; j<${#code}; j++)); do
        symbol="${code:$j:1}"
        termux-torch on
        if [ "$symbol" = "." ]; then
            sleep 0.1
        else
            sleep 0.3
        fi
        termux-torch off
        sleep 0.1
    done
    sleep 0.2
done
