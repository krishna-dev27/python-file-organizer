

import os
import shutil
folder_path = input()

file_formats = {
    'images': ['.jpeg', '.jpg', '.png'],
    'documents': ['.pdf', '.doc', '.docx'],
    'videos': ['.mp4']
}

ext_map={}
for folder, extension in file_formats.items():
    for ext in extension:
        ext_map[ext]=folder


for file in os.listdir(folder_path):
    file_path=os.path.join(folder_path,file)
    if not os.path.isfile(file_path):
        continue
    file_name, file_extension = os.path.splitext(file)
    file_extension = file_extension.lower()
     
    target_folder = ext_map.get(file_extension,'others')
    target_path = os.path.join(folder_path,target_folder)
    os.makedirs(target_path,exist_ok=True)
    destination = os.path.join(target_path,file)


    counter = 1
    base_name ,extension = os.path.splitext(file)
    while os.path.exists(destination):
        new_name = f"{base_name}_{counter}{extension}"
        destination = os.path.join(target_path, new_name)
        counter += 1
    try:
        shutil.move(file_path,destination)
    except Exception as e:
        print(f"Error moving {file}:{e}")

