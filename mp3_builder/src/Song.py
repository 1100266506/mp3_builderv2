class Song:

    def __init__(self, mp3file_path = "blank/blank"):
        #setting a default song to no song

        #split mp3file_path by / to get the last part
        self.mp3file_path = mp3file_path
        Array = mp3file_path.split("/")
        self.title = Array[len(Array) - 1]

        self.artist = "None"

    def setTitle(self, title):
        self.title = title

    def setArtist(self, artist):
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist

    def getPath(self):
        songPath = self.mp3file_path + self.title;
        return songPath;
