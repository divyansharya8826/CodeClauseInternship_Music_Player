from tkinter import *  # type:ignore
from tkinter import filedialog
import pygame

root = Tk()
root.title('MP3 Player')
root.iconbitmap("./Images/logo.ico")

pygame.mixer.init()


def add_many_musics():
    musics = filedialog.askopenfilenames(
        initialdir='audio/', title="Choose A music", filetypes=(("mp3 Files", "*.mp3"), ))
    for music in musics:
        music = music.replace(".mp3", "")
        music_box.insert(END, music)


def add_music():
    music = filedialog.askopenfilename(
        initialdir='audio/', title="Choose A music", filetypes=(("mp3 Files", "*.mp3"), ))
    music = music.replace(".mp3", "")

    music_box.insert(END, music)


def stop():
    pygame.mixer.music.stop()
    music_box.selection_clear(ACTIVE)


def play():
    music = music_box.get(ACTIVE)
    music = f'{music}.mp3'

    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=0)


def previous_music():

    next_one = music_box.curselection()

    next_one = next_one[0]-1
    music = music_box.get(next_one)

    music = f'{music}.mp3'
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=0)

    music_box.selection_clear(0, END)
    music_box.activate(next_one)
    music_box.selection_set(next_one, last=None)


def next_music():

    next_one = music_box.curselection()

    next_one = next_one[0]+1
    music = music_box.get(next_one)

    music = f'{music}.mp3'

    pygame.mixer.music.load(music)
    pygame.mixer.music.play(loops=0)

    music_box.selection_clear(0, END)
    music_box.activate(next_one)
    music_box.selection_set(next_one, last=None)


global paused
paused = False


def pause(is_paused):

    global paused

    paused = is_paused

    if paused:

        pygame.mixer.music.unpause()
        paused = False
    else:

        pygame.mixer.music.pause()
        paused = True


def delete_music():
    music_box.delete(ANCHOR)
    pygame.mixer.music.stop()


def delete_all_musics():
    music_box.delete(0, END)

    pygame.mixer.music.stop()


music_box = Listbox(root, bg="black", fg="green", width=60,
                    selectbackground="Grey", selectforeground="Black")
music_box.pack(pady=20)

back_btn_img = PhotoImage(file="Divyansh/Python/Music Player/images/Back_Button.jpg")
forward_btn_img = PhotoImage(file="Divyansh/Python/Music Player/images/Forward_Button.jpg")
play_btn_img = PhotoImage(file="Divyansh/Python/Music Player/images/Play_Button.jpg")
pause_btn_img = PhotoImage(file="Divyansh/Python/Music Player/images/Pause_Button.jpg")
stop_btn_img = PhotoImage(file="Divyansh/Python/Music Player/images/Stop_Button.jpg")

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_btn_img,
                     borderwidth=1, command=previous_music, bg="grey",fg="red",border=1)
forward_button = Button(controls_frame, image=forward_btn_img,
                        borderwidth=1, command=next_music, bg="grey",fg="red")
play_button = Button(controls_frame, image=play_btn_img,
                     borderwidth=1, command=play, bg="grey",fg="red")
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=1,
                      command=lambda: pause(paused), bg="grey",fg="red")
stop_button = Button(controls_frame, image=stop_btn_img,
                     borderwidth=1, command=stop, bg="grey",fg="red")

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)


my_menu = Menu(root)
root.config(menu=my_menu)

add_music_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Music", menu=add_music_menu)
add_music_menu.add_command(
    label="Add One Music To Playlist", command=add_music)


add_music_menu.add_command(
    label="Add Many music To Playlist", command=add_many_musics)


remove_music_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Music", menu=remove_music_menu)
remove_music_menu.add_command(
    label="Delete Music From Playlist", command=delete_music)
remove_music_menu.add_command(
    label="Delete All Music From Playlist", command=delete_all_musics)
root.mainloop()
