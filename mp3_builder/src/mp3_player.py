import os, time, sys
import Song as Song
from random import randint
sys.path.insert(1, '/home/benjamin/CS/Python/mp3_builder/playsound-master')
from playsound import playsound

#personal mp3 player for a computer. Has a shuffle without repeat feature
# @author Benjamin Ahn
# @version 1.0

class mp3_player():

    def __init__(self, path):
        self.path = path #represents the file path to a directory filled with mp3's
        self.files = None #represents a list of mp3 files
        self.musicDictionary = {} #holds dictionary of song objects corresponding to path
        self.currentSong = None #represents the current song being played by the mp3 player
        self.queue = [] #represents a list of Song objects that are in line to be played
        self.finishedQueue = 0 #represents a binary variable with 0 being not finished and 1 being finished playing a song in the queue

        self.importPlaylist()

################################################################################
#GETTERS AND SETTERS

    def getPath(self):
        return self.path

    def getFiles(self):
        return self.files

    def getCurrentSong(self):
        return self.currentSong

    def setPath(self, path):
        self.path = path

    def setFiles(self, files):
        self.files = files

    def setCurrentSong(self, currentSong):
        self.currentSong = currentSong

    def getMusicDictionary(self):
        return self.musicDictionary

    #adds a song to the music library list
    def addMusicLibrary(self, song):
        pass

################################################################################
#SETUP MP3 PLAYER
    #finds the directory containing mp3 files
    def importPlaylist(self):
        path, dir, mp3files = next(os.walk(self.path))
        self.files = mp3files
        self.path = path

        #create song objects for each mp3 file found. Store in MusicLibrary
        for mp3 in self.files:
            mp3path = self.path + "/" + mp3
            newSong = Song.Song(mp3path)
            self.musicDictionary[newSong] = newSong.getPath()

        # #order songs in alphabetical order in musiclibrary
        # h = 0
        # while h < len(self.musicLibrary):
        #     i = 0
        #     while i < len(self.musicLibrary) - 1:
        #         firstSong = self.musicLibrary[i]
        #         secSong = self.musicLibrary[i + 1]
        #         #compare titles
        #         j = 0
        #         while j < len(secSong.getTitle()): #always comparing against the shortest song name
        #             if secSong.getTitle()[j] < firstSong.getTitle()[j]: #if the second song comes first
        #                 self.musicLibrary[i] = secSong
        #                 self.musicLibrary[i + 1] = firstSong
        #                 i += 1
        #                 j = len(secSong.getTitle()) #break out of for loop
        #             elif secSong.getTitle()[j] > firstSong.getTitle()[j]: #if first song comes first
        #                 i += 1
        #                 j = len(secSong.getTitle())
        #             elif secSong.getTitle()[j] == firstSong.getTitle()[j]:
        #                 j += 1
        #     h += 1

        #set first song as currentSong by default
        self.currentSong = list(self.musicDictionary.keys())[0]

################################################################################
#CORE MP3 PLAYER FUNCTIONS

    #plays a song from the queue or passed in song
    def playSong(self, Song):
        #find path to song passed in
        songpath = self.path + "/" + Song.getTitle()

        #play song via playsound library
        playsound(songpath);

    #returns the a list of the name and artist of a song
    def songInfo(self, song):
        name = song.getTitle()
        artist = song.getArtist()
        return [name, artist]

################################################################################
#ADD ON FEATURES

    #plays songs from MusicLibrary in a random order without repeats
    def shuffle(self):
        played_songs_index = []
