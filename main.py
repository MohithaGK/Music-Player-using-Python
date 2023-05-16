import tkinter as tk
import fnmatch
import os
from pygame import mixer

ro = tk.Tk()
ro.title("Music Player")
ro.geometry("600x500")
ro.config(bg="black")

# Set the root path relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
rootpath = os.path.join(script_dir, "songs")
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file="previous.gif")
next_img = tk.PhotoImage(file="next.gif")
pause_img = tk.PhotoImage(file="pause.gif")
play_img = tk.PhotoImage(file="play.gif")
stop_img = tk.PhotoImage(file="stop.png")

def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(os.path.join(rootpath, listBox.get("anchor")))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def nxt():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(os.path.join(rootpath, next_song_name))
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def prev():
    prev_song = listBox.curselection()
    prev_song = prev_song[0] - 1
    prev_song_name = listBox.get(prev_song)
    label.config(text=prev_song_name)

    mixer.music.load(os.path.join(rootpath, prev_song_name))
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listBox.select_set(prev_song)

def pau():
    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"

listBox = tk.Listbox(ro, fg="cyan", bg="brown", width=100, font=("Musicals", 14))
listBox.pack(padx=15, pady=15)

label = tk.Label(ro, text='', bg='black', fg='yellow', font=("Musicals", 14))
label.pack(pady=15)

top = tk.Frame(ro, bg="black")
top.pack(padx=10, pady=5, anchor='center')

prevButton = tk.Button(ro,text = "Prev",image = prev_img , bg = 'black' ,borderwidth=0,command = prev)
prevButton.pack(padx = 20,in_=top,side = 'left')

stopButton = tk.Button(ro,text = "Stop",image = stop_img , bg = 'black' ,borderwidth=0,command=stop)
stopButton.pack(padx = 20,in_=top,side = 'left')

playButton = tk.Button(ro,text = "play",image = play_img , bg = 'black' ,borderwidth=0,command = select)
playButton.pack(padx = 20,in_=top,side = 'left')

pauseButton = tk.Button(ro,text = "pause",image = pause_img , bg = 'black' ,borderwidth=0 , command=pau)
pauseButton.pack(padx = 20,in_=top,side = 'left')

nextButton = tk.Button(ro,text = "next",image = next_img, bg = 'black' ,borderwidth=0,command= nxt)
nextButton.pack(padx = 20,in_=top,side = 'left')


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)


ro.mainloop()
