from msilib.schema import Error
import os, shutil
from tkinter import E

image = ["jpg", "png", "jpeg", "gif", "webp", "tiff"]
audio = ["mp3","wav"]
video = ["mp4","mkv", "flv", "mpeg"]
docs  = ["pdf", "txt","ref","docx"]
zips = ["zip", "rar","gz"]
installers = ["exe","msi"]

Path = input("Enter Path of Folder: ")

files = os.listdir(Path)
os.chdir(Path)
print(files)
folders = ["images","audios","videos","docs","zips","installers","others"]

for i in range(len(folders)):
    try:
        if(os.path.isfile(f"{folders[i]}/")):
            continue
        else:
            os.mkdir(f"{folders[i]}/")
    except:
        print("Folder Already Exist")


    for file in files:
        try:
            if os.path.isfile(f"{file}") and file != "AutoFolder.py":
                ext = (file.split(".")[-1]).lower()
                print(ext)
                if ext in image:
                    shutil.move(file, "images/")
                    continue
                elif ext in audio:
                    shutil.move(file,"audios/")
                    continue
                elif ext in video:
                    shutil.move(file,"videos/")
                    continue
                elif ext in zips:
                    shutil.move(file,"zips/")
                    continue
                elif ext in installers:
                    shutil.move(file,"installers/")
                    continue
                elif ext in docs:
                    shutil.move(file,"docs/")
                    continue
                else:
                    shutil.move(file,"others/")
                    continue
        except Exception as e:
            print(e)