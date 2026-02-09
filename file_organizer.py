


import os
import shutil

# 1. Folder path to organize

folder_path = input("Enter full path that you want to organize:")

# 2. File type categories
file_types={
    'Images':['.jpg','.png','.jpeg','.bmp','.gif','.webp','.svg'],
    'Documents':['.pdf','.txt','.xml','.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.md'],
    'Music':['.mp3','.wav', '.flac', '.aac', '.ogg', '.m4a'],
    'Videos':['.mp4','.mkv', '.avi', '.mov', '.wmv', '.webm']

}

# 3. Get all items inside the folder
files = os.listdir(folder_path)

# 4. Loop through each item
for file in files:
    file_path = os.path.join(folder_path, file)

    # Process only files (not folders)
    if os.path.isfile(file_path):
        name, extension = os.path.splitext(file)
        moved = False

        # Check file type
        for folder_name, extensions in file_types.items():
            if extension.lower() in extensions:
                destination_folder = os.path.join(folder_path, folder_name)

                # Create folder if it doesn't exist
                if not os.path.exists(destination_folder):
                    os.mkdir(destination_folder)

                # Move file
                shutil.move(file_path, destination_folder)
                print(file, "moved to", folder_name)
                moved = True
                break

        # If file type not matched, move to Others
        if not moved:
            other_folder = os.path.join(folder_path, "Others")

            if not os.path.exists(other_folder):
                os.mkdir(other_folder)

            shutil.move(file_path, other_folder)
            print(file, "moved to Others")


print("Hoooray!!! Your folder is now arranged😊")