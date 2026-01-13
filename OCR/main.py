import pytesseract
import os

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Alternative method to set the path:
from pytesseract import pytesseract as pt
pt.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img_path = 'Screenshot 2026-01-13 015128.png'
text = "eng"
text = pytesseract.image_to_string(img_path, lang=text)
print(text)