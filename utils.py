from pathlib import Path
import shutil

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def save_upload_file(upload_file):
    save_path = UPLOAD_DIR / upload_file.filename
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return save_path
