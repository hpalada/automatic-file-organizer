import os
import shutil

# Folder categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Code": [".py", ".js", ".cpp", ".java"],
    "Others": []
}

def organize_files(path):
    for file in os.listdir(path):
        name, ext = os.path.splitext(file)
        source = os.path.join(path, file)
        
        if os.path.isfile(source):
            moved = False
            for folder, extensions in CATEGORIES.items():
                if ext.lower() in extensions:
                    dest_folder = os.path.join(path, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(source, os.path.join(dest_folder, file))
                    moved = True
                    break
            if not moved:
                dest_folder = os.path.join(path, "Others")
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(source, os.path.join(dest_folder, file))

if __name__ == "__main__":
    current_path = os.getcwd()
    organize_files(current_path)
    print("Files organized successfully.")
