#testing for mp3_player.py
import time, threading, sys
sys.path.insert(1, '/home/benjamin/CS/Python/mp3_builder/src')
import mp3_player as mp3_player

#constructor
print("##########################")
print("Constructor Testing")
mp3 = mp3_player.mp3_player("/home/benjamin/Music")
print(mp3.getPath())
print("This mp3 has " + str(len(mp3.getFiles())) + " files!")
print("Fileslist(", str(len(mp3.getFiles())), "): ", mp3.getFiles())
print("Music Dictionary(", str(len(mp3.getMusicDictionary())), "): ", mp3.getMusicDictionary())

#functions
print("#########################")
print("Main Function Testing")
mp3_musicDictionary = mp3.getMusicDictionary()
print("Playing first song")
print(mp3.currentSong.getTitle());
mp3.playSong(mp3.currentSong);
