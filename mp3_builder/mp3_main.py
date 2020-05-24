#mp3 interface
import sys
sys.path.insert(1, '/home/benjamin/CS/Python/mp3_builder/src')
import mp3_player as mp3
from tkinter import *
import os
import time
import Song as Song

###############################################################################
#SETUP PLAYLIST not functional
#path = input("Enter path to mp3 directory!\n")



################################################################################
#SETUP GUI

class App:

    def __init__(self, path):
        self.path = path

        #create an mp3_player object
        self.mp3_object = mp3.mp3_player(self.path)

        #create GUI window
        self.root = Tk()
        self.root.title("Benjamin's mp3 player")
        self.root.geometry(self.autoFitWindow())

        #create PanedWindow
        PanedWindow1 = PanedWindow(orient = 'horizontal') #will hold musiclibrary on left, and everything else on right
        PanedWindow11 = PanedWindow(PanedWindow1, orient = 'vertical') #will hold PanedWindow and Label for Music Library
        PanedWindow2 = PanedWindow(PanedWindow1, orient = 'vertical') #will hold Top label, buttons, songinfo
        PanedWindow3 = PanedWindow(PanedWindow2, orient = 'horizontal') #will hold buttons
        PanedWindow4 = PanedWindow(PanedWindow2, orient = 'horizontal') #will hold songinfo
        # PanedWindow5 = PanedWindow(PanedWindow2, orient = 'vertical') #will hold a panedwindow and label for queue

        self.root.LabelTop = Label(PanedWindow2, text = "Welcome to Benjamin's mp3 player")
        PanedWindow2.add(self.root.LabelTop)

        #Song info space
        self.root.LabelSongName = Label(PanedWindow4, text = "Song Title", width = 100)
        self.root.LabelSongArtist = Label(PanedWindow4, text = "Song Artist", width = 100)
        PanedWindow4.add(self.root.LabelSongName)
        PanedWindow4.add(self.root.LabelSongArtist)

        #display music library in ListBox
        self.root.LabelMusicLibrary = Label(PanedWindow11, text = "Music Library")
        ListboxMusicLibrary = Listbox(PanedWindow11, width = 50)
        count = 1
        for song in self.mp3_object.getMusicLibrary():
            file = song.getTitle()
            filepath = self.mp3_object.getPath() + "/" + file
            newSong = Song.Song(filepath)
            ListboxMusicLibrary.insert(count, newSong.getTitle())
            count +=1
        PanedWindow11.add(self.root.LabelMusicLibrary)
        PanedWindow11.add(ListboxMusicLibrary)
        PanedWindow11.pack(fill = BOTH)
        PanedWindow1.add(PanedWindow11)

        #key Buttons
        self.root.buttonShuffle = Button(PanedWindow3, text = "shuffle", command = self.clickShuffle, width = 20)
        self.root.buttonPause = Button(PanedWindow3, text = "pause", command = self.clickPause, width = 20)
        self.root.buttonUnpause = Button(PanedWindow3, text = "unpause", command = self.clickUnpause, width = 20)
        currentSong = self.mp3_object.getCurrentSong()
        self.root.buttonShowInfo = Button(PanedWindow3, text = "show song info", width = 20,
            command = lambda : self.clickShowInfo())
        self.root.buttonPlay = Button(PanedWindow3, text = "play", width = 20,
            command = lambda : self.clickPlay(ListboxMusicLibrary))
        PanedWindow3.add(self.root.buttonShuffle)
        PanedWindow3.add(self.root.buttonPlay)
        PanedWindow3.add(self.root.buttonPause)
        PanedWindow3.add(self.root.buttonUnpause)
        PanedWindow3.add(self.root.buttonShowInfo)

        # #display queue in listbox
        # self.root.LabelQueue = Label(PanedWindow5, text = "Song Queue")
        # ListBoxQueue = Listbox(PanedWindow5)
        # self.root.ButtonAddQueue = Button(PanedWindow5, text = "Add to Queue",
        #     command = lambda : self.clickAddQue(ListboxMusicLibrary, ListBoxQueue))
        # self.root.ButtonRemoveQueue = Button(PanedWindow5, text = "Remove from Queue",
        #     command = lambda : self.clickRemoveQueue(ListBoxQueue))
        # PanedWindow5.add(self.root.ButtonAddQueue)
        # PanedWindow5.add(self.root.ButtonRemoveQueue)
        # PanedWindow5.add(ListBoxQueue)

        #configure panedwindows
        PanedWindow1.pack(fill = BOTH, expand = 1)
        PanedWindow2.pack(fill = BOTH)
        PanedWindow3.pack()
        PanedWindow4.pack(fill = BOTH, expand = 1)
        # PanedWindow5.pack(fill = BOTH)
        #PanedWindow2.paneconfig(self.root.LabelTop, pady = 30)
        PanedWindow3.place(anchor = 'center')

        #assemble panedwindows
        PanedWindow1.add(PanedWindow2)
        PanedWindow2.add(PanedWindow3)
        PanedWindow2.add(PanedWindow4)
        # PanedWindow2.add(PanedWindow5)

        # self.checkQueue(ListBoxQueue)

        #Run
        self.root.mainloop()

    #autofit application to fit entire screen
    def autoFitWindow(self):
        import subprocess
        cmd = ['xrandr']
        cmd2 = ['grep', '*']
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
        p.stdout.close()
        resolution_string, junk = p2.communicate()
        resolution = resolution_string.split()[0]
        return resolution

    #button -> shuffle
    def clickShuffle(self):
        self.mp3_object.shuffle()

    #button -> pause
    def clickPause(self):
        self.mp3_object.pause()

    #button -> unpause
    def clickUnpause(self):
        self.mp3_object.unpause()

    #button -> showInfo
    def clickShowInfo(self):
        self.root.LabelSongName.configure(text = self.mp3_object.getCurrentSong().getTitle())
        self.root.LabelSongArtist.configure(text = self.mp3_object.getCurrentSong().getArtist())

    #button -> play
    def clickPlay(self, listbox1):

        #play a song if something is selected in the listbox
        try:
            if listbox1.get(listbox1.curselection()) != "":
                selectedSongTitle = listbox1.get(listbox1.curselection())
                selectedSongPath = self.mp3_object.getPath() + "/" + selectedSongTitle
                selectedSong = Song.Song(selectedSongPath)
                self.mp3_object.normalPlay(selectedSong)
        #will throw error if nothing is selected. If this happens, play normal
        except:
            firstSong = self.mp3_object.getMusicLibrary()[0]
            self.mp3_object.normalPlay(firstSong)

    #button -> add to queue
    def clickAddQue(self, listbox1, listbox2):
        queueSongTitle = listbox1.get(listbox1.curselection())
        if queueSongTitle == None:
            #upon startup, the default song is the first song
            queueSong = Song.Song()
        else:
            #recreate song object from selected song title in listbox
            queueSongPath = self.mp3_object.getPath() + "/" + queueSongTitle
            queueSong = Song.Song(queueSongPath)
            self.mp3_object.addToQueue(queueSong)
            listbox2.insert(listbox2.size(), queueSong.getTitle())

    # def checkQueue(self, listbox):
    #     if self.mp3_object.finishedQueue == 1:
    #         listbox.delete(0)
    #     listbox.after(200, self.checkQueue(listbox))

    def clickRemoveQueue(self, listbox1):
        queue = self.mp3_object.getQueue()
        if listbox1.get(listbox1.curselection()) == None:
            pass
        else:
            del queue[listbox1.curselection()[0]]
            listbox1.delete(listbox1.curselection()[0])

#execute
app1 = App("/home/benjamin/Music")
