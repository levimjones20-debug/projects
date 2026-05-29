
import lyricsgenius

genius = lyricsgenius.Genius("2oBQ5HPjaPdChUMmSxvZi1Lc_qhH-v6nA5m3GrCRd4VedxVSEzhGzNcup7f6rRGq")

genius.verbose = False

artist = input("Artist: ")

song = input("Song: ")

print(f"\nSearching for {song} by {artist}...")

result = genius.search_song(song, artist)

if result:

    print(f"\n{result.title} by {result.artist}\n")

    print(result.lyrics)

else:

    print("Couldn't find that song!")

