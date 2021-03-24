import os, shutil

image = ["jpg", "png", "jpeg", "gif", "webp", "tiff"]
audio = ["mp3","wav"]
video = ["mp4","mkv", "flv", "mpeg"]
docs  = ["pdf", "txt","ref","doc"]

Path = input("Enter Path of Folder: ")

files = os.listdir(Path)
os.chdir(Path)
print(files)
folders = ["images","audios","videos","docs","others"]

for i in range(len(folders)):
    try:
        if(os.path.isfile(f"{folders[i]}/")):
            continue
        else:
            os.mkdir(f"{folders[i]}/")
    except:
        print("Folder Already Exist")


for file in files:
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
        elif ext in docs:
            shutil.move(file,"docs/")
            continue
        else:
            shutil.move(file,"others/")
            continue