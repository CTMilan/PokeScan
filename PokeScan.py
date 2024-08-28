from PIL import Image
import pytesseract
import numpy as np
import cv2
import PreProcessing
import os
import shutil

records = open("records.txt","a")


print("About to run")
PreProcessing.prepare_images()
print("Done running")

    


