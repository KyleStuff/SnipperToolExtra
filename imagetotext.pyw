import os  #Used for deleting temporary files
import win32clipboard #Used to paste text into clipboard
import pyautogui # Uhhh idk but it breaks if i remove
import time # Used to
from PIL import Image
from PIL import ImageGrab # clipboard
from pytesseract import * #Imports OCR
pytesseract.tesseract_cmd = r'C:\Users\KyleD\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' #Open-source OCR

##              MAIN           ##
img = ImageGrab.grabclipboard() # GET clipboard image

# or ImageGrab.grab() to grab the whole screen!

#img.save('paste.png', 'PNG') # Saves to inputfolder
#time.sleep(0.05) #waits for windows to finish saving

#imgsaved = Image.open("paste.png") # stores image as imgsaved variable

output = pytesseract.image_to_string(img) #converts image to text

## Filter incorrect stuff: ##





# Sets the clipboard to the output:
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(output)
win32clipboard.CloseClipboard()


imgsaved.close()
#os.remove("paste.png")







