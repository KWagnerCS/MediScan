import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

def read_image(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

if __name__ == "__main__":
    main()