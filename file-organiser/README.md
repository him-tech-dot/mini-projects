# File Organizer (Python)

A simple Python automation script that organizes image files by extension into a separate folder with renamed filenames.

## What it does
The script scans the current directory for files with a specified extension (e.g. `.jpg`), moves them into an `images` folder, and renames them sequentially.

## Features
- Automatically creates destination folder if it does not exist
- Filters files by extension
- Renames files in a clean numbered format

## Requirements
- Python 3.x

## How it works
By default, the script looks for `.jpg` files in the current directory and moves them into an `images` folder.

Original:
photo1.jpg, image2.jpg, pic3.jpg

After running:
images/photo-1.jpg, images/photo-2.jpg, images/photo-3.jpg

## How to use

1. Place the script in the folder containing your image files.

2. Run the program:
python main.py

3. All `.jpg` files will be moved into the `images` folder and renamed automatically.

## Customization

To organize a different file type, change this line in the code:
arrange_files(files, ".jpg")