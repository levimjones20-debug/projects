import os
import shutil

folder = input("Which folder do you want to organize? ")

file_types = {
    "Music": [".mp3", ".flac", ".wav", ".m4a", ".ogg", ".m4b"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Documents": [".pdf", ".docx", ".txt", ".epub", ".md"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".xz", ".deb"],
    "Fonts": [".ttf", ".otf", ".woff"],
    "Torrents": [".torrent"],
}

for filename in os.listdir(folder):
    filepath = os.path.join(folder, filename)
    if os.path.isfile(filepath):
        ext = os.path.splitext(filename)[1].lower()
        for category, extensions in file_types.items():
            if ext in extensions:
                dest = os.path.join(folder, category)
                os.makedirs(dest, exist_ok=True)
                shutil.move(filepath, os.path.join(dest, filename))
                print(f"Moved {filename} → {category}/")
                break

print("Done!")
