import pytesseract
from PIL import Image, ImageGrab

def recognise(f):
    img = Image.open('blabla.png')
    custom_config = r'-l rus+eng --oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)
    print(text)
    with open('blabla_done.txt', 'w') as text_file:
        text_file.write(text)

def save_screen(f):
    pic = ImageGrab.grab(bbox=None)
    pic.save('blabla.png')

