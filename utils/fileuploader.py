import os
from pathlib import Path

def list_images_in_folder(folder_path):
    image_extensions = {".jpg", ".jpeg", ".png", ".bmp"}
    return [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if Path(f).suffix.lower() in image_extensions
    ]