# Automatic File Organizer

This project is a Python script that automatically organizes files in a directory into subfolders based on their file extension (images, documents, videos, code, etc.).

## Technologies
- Python 3
- Libraries: os, shutil

## Features
- Iterates through all files in the target directory.
- Detects file extensions.
- Moves files into categorized folders:
  - Images
  - Documents
  - Videos
  - Code
  - Others

## Usage
```bash
python organizer.py
```

## Example
Before:
```
folder/
  photo.jpg
  report.pdf
  script.py
```

After:
```
folder/
  Images/photo.jpg
  Documents/report.pdf
  Code/script.py
```

## Purpose
This project demonstrates:
- File and directory management.
- Task automation using Python.
- Practical use of built-in modules (os and shutil).
