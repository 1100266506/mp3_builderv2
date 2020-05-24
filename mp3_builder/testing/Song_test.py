import sys
sys.path.insert(1, '/home/benjamin/CS/Python/mp3_builder/src')
import Song as Song
#Test cases for Song.py

#does it properly create a Song object
# song1 = Song.Song("file/to/mp3/my_favorite_song.mp3")
song1 = Song.Song("/home/benjamin/Music/38 Special- Caught up in You.mp3")
print("Get song title: " + song1.getTitle())
print("Get song artist: " + song1.getArtist())
print("Get song path: " + song1.getPath())
