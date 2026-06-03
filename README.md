# Automatic File Organizer

Python utility that scans a directory and organizes every file into categorized subfolders based on file extension. Zero external dependencies — uses only the standard library.

## Stack

Python 3 · `os` · `shutil`

## How It Works

The script reads every file in the target directory, maps its extension to a category, and moves it into the corresponding subfolder. Unknown extensions go to `Others` so nothing is lost.

| Category | Extensions |
|---|---|
| Images | `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.svg` `.webp` |
| Documents | `.pdf` `.doc` `.docx` `.txt` `.xls` `.xlsx` `.ppt` `.pptx` |
| Videos | `.mp4` `.mov` `.avi` `.mkv` `.wmv` `.flv` |
| Code | `.py` `.js` `.ts` `.html` `.css` `.java` `.c` `.cpp` `.sh` |
| Others | anything else |

## Usage

```bash
python organizer.py
```

**Before:**
```
Downloads/
  photo.jpg
  report.pdf
  script.py
  video.mp4
  archive.zip
```

**After:**
```
Downloads/
  Images/photo.jpg
  Documents/report.pdf
  Code/script.py
  Videos/video.mp4
  Others/archive.zip
```

## Extending It

Adding a new category is one step — add an entry to the `CATEGORIES` dict:

```python
CATEGORIES = {
    'Audio': ['.mp3', '.wav', '.flac', '.aac'],
    # ... existing categories
}
```

## Highlights

- No pip install required — runs on any machine with Python 3
- Handles unknown extensions gracefully with an Others fallback
- Simple to extend or integrate into a larger automation pipeline

---

Built by Homer Palada — CS student at Universidad Católica de Honduras, graduating May 2027.
