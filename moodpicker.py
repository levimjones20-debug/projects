import os
import random

moods = {
    "happy": "/home/leviathan/Music/Dakota's MP3",
    "sad": "/home/leviathan/Music/Ethel Cain",
    "angry": "/home/leviathan/Music/Frightened Little Asshole",
    "chill": "/home/leviathan/Music/Run, rabbit, run",
}

print("How are you feeling?")
for i, mood in enumerate(moods, 1):
    print(f"{i}. {mood}")

choice = input("\nType your mood: ").lower()

if choice in moods:
    folder = moods[choice]
    songs = []
    for root, dirs, files in os.walk(folder):
        for filename in files:
            if filename.endswith(".mp3"):
                songs.append(filename)
    
    if songs:
        pick = random.choice(songs)
        print(f"\n🎵 Based on your mood: {pick}")
    else:
        print("No songs found in that folder!")
else:
    print("I don't know that mood!")
