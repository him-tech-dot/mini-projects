# QR Code Generator (Python)

A simple command-line Python program that generates a QR code image from a user-provided URL.

## What it does
The program asks for a URL and a file name, then creates a QR code image (`.png`) for that URL and saves it to the current folder.

## Features
- High error correction QR codes
- Custom size and border
- Automatic `.png` extension handling

## Requirements
- Python 3.x
- qrcode library
- pillow library

Install dependencies:
pip install qrcode[pil]

## How to use

1. Run the program:
python main.py

2. Enter the URL when prompted.

3. Enter the file name for the QR code image.

4. The QR code image will be saved in the same folder.

## Example

Enter the url :
https://example.com

Enter filename to be saved as :
my_qr

Output:
my_qr.png is created in the current folder.