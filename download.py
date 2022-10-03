from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from pytube import YouTube
import shutil

def select_path():
    #выбор пути сохранения файла
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Идёт скачивание файла...')
    #Скачивание видео 
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    screen.title('Загрузка завершена!')
    
def download_file_audio():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Идёт скачивание файла...')
    #Скачивание адуио
    mp3_audio = YouTube(get_link).streams.get_audio_only().download()
    audio_clip = AudioFileClip(mp3_audio)
    audio_clip.close()
    shutil.move(mp3_audio, user_path)
    screen.title('Загрузка завершена!')

screen = Tk()
title = screen.title('Youtube Download')
canvas = Canvas(screen, width=500, height=450)
canvas.pack()

#поле для ссылки
link_field = Entry(screen, width=40, font=('Calibri', 15) )
link_label = Label(screen, text="Введите ссылку для скачивания: ", font=('Calibri', 15))

#Выбор пути сохранения файла
path_label = Label(screen, text="Выберите папку для сохранения файла:", font=('Calibri', 15))
select_btn =  Button(screen, text="Выбор папки загрузки", bg='DimGrey', padx='22', pady='5',font=('Calibri', 15), fg='#fff', command=select_path,width=16,height=1)

canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

canvas.create_window(250, 70, window=link_label)
canvas.create_window(250, 120, window=link_field) 

#Кнопки для скачивания
download_btn = Button(screen, text="Скачать видео",bg='DarkSlateBlue', padx='22', pady='5',font=('Calibri', 15), fg='#fff', command=download_file)
canvas.create_window(350, 390, window=download_btn)

download_btn_adio = Button(screen, text="Скачать аудио",bg='DarkSlateBlue', padx='22', pady='5',font=('Calibri', 15), fg='#fff', command=download_file_audio)
canvas.create_window(150, 390, window=download_btn_adio)

screen.mainloop()