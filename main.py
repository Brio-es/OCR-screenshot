import pyautogui as au
import keyboard as kb
import pytesseract as tess
from PIL import Image

tess.pytesseract.tesseract_cmd = r'C:\Users\cesar\Documents\Screen_python\Tesseract-OCR\tesseract.exe'
prefered_key = "Bloq Mayus"




def select_key():
    global prefered_key
    print("The default key to take the screenshot is 'Block Mayus' \n"
          "If you want to change it, press your desired key \n"
          "In case of special keys like 'Cntrl', 'Shift', or 'Alt' type it as is showed on your keyboard \n"
          "Otherwise, type 'ok' \n"
          "Press 'esc' at any second to end the task\n")

    _ = input().lower()
    if _ != "ok":
        prefered_key = _
    else:
        prefered_key = "Bloq Mayus"

    print(prefered_key)


def screen():
    kb.wait(prefered_key)
    x, y = au.position()
    # First capture of position
    kb.wait(prefered_key)
    x1, y1 = au.position()
    # Second capture of position
    screenshot(x, y, x1, y1)


def screenshot(a, b, c, d):
    l1 = [a,c]
    l2 = [b,d]
    x = min(l1)
    x1 = max(l1)-min(l1)
    y = min(l2)
    y1 = max(l2)-min(l2)
    au.screenshot("reference.png", region=(x,y,x1,y1))
    print("screen shot done")
    # Takes the screenshot


def ocr():
    img = Image.open('reference.png')
    text = tess.image_to_string(img)
    print(text)
    # Processes the img to text

def main():
    while True:
        screen()
        ocr()




if __name__ == '__main__':
    select_key()
    main()

