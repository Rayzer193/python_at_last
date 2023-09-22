import os
os.system('CLS')#clear для систем Linux
import shutil

file_name = input('Ведите имя файла: ')

def sort_file(file_name: str):
    if os.path.exists(file_name):
        img_dir = 'images'
        doc_dir = 'documents'
        video_dir = 'movies'
        os.makedirs(img_dir, exist_ok=True) 
        os.makedirs(doc_dir, exist_ok=True)
        os.makedirs(video_dir, exist_ok=True)
        _, extension = os.path.splitext(file_name)
        img_ext = ['.png', '.jpg','.jpeg', ]
        doc_ext = ['.doc', '.docx', '.xls', '.xlsx' '.txt', '.pdf']
        video_ext = ['.mp4', '.mpg', '.gif', '.avi', '.mkv']
        if extension in img_ext:
            dest_picture = os.path.join(img_dir, file_name)
            try:
                shutil.move(file_name, dest_picture)
                print("Файл перемещен в ", dest_picture)
            except IsADirectoryError:
                print("Что-то пошло не так, попробуйте еще раз")
        elif extension in doc_ext:
            dest_doc = os.path.join(doc_dir, file_name)
            try:
                shutil.move(file_name, dest_doc)
                print("Файл перемещен в ", dest_doc)
            except IsADirectoryError:
                print("Что-то пошло не так, попробуйте еще раз")
        elif extension in video_ext:
            dest_video = os.path.join(video_dir, file_name)
            try:
                shutil.move(file_name, dest_video)
                print("Файл перемещен в ", dest_video)
            except IsADirectoryError:
                print("Что-то пошло не так, попробуйте еще раз")
    else:
        print("Файл не существует или расширение не поддерживается")

sort_file(file_name)