import os
import random
import subprocess

folder = input("Which music folder? ")
count = int(input("How many songs to pick? "))

songs = []
for root, dirs, files in os.walk(folder):
    for filename in files:
        if filename.endswith(".mp3"):
            songs.append(os.path.join(root, filename))

if songs:
    picks = random.sample(songs, min(count, len(songs)))
    print(f"\n🎵 Your random playlist:")
    for i, song in enumerate(picks, 1):
        print(f"{i}. {os.path.basename(song)}")
    
    play = input("\nPlay them? (y/n) ")
    if play.lower() == "y":
        for song in picks:
            print(f"\nNow playing: {os.path.basename(song)}")
            subprocess.run(["mpg123", song])
else:
    print("No mp3s found!")
