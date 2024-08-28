from PIL import Image
import sys
import os
import pytesseract
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from pathlib import Path
import shutil


#--- Pre-Processing for Images ---#

#--- Utility Functions ---#

def grayscale(image):
    return cv.cvtColor(image,cv.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv.medianBlur(image,5)

def gauss_blur(image):
    return cv.GaussianBlur(image,(5,5),0)

def thresholding(image):
    return cv.threshold(gauss_blur(image), 0.0, 255.0, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

def prepare_images():
    
    path_raw = 'library/images_raw/'
    Path('library/images_raw').mkdir(parents=True, exist_ok=True)
    path_prepared = 'library/images_prepared/'
    Path('library/images_prepared').mkdir(parents=True, exist_ok=True)
    path_archive = 'library/archive/'
    Path('library/archive').mkdir(parents=True, exist_ok=True)

    img = cv.imread(path_raw+'pokecode.jpeg', cv.IMREAD_COLOR)
    assert img is not None, "Image not found(?)"

    gray = grayscale(img)
    quiet = remove_noise(gray)
    threshed = thresholding(quiet)

    images = [img,gray,quiet,threshed]
    titles = ['original','grayscale','noise_removal','thresholded']
    
    for i in range(4):
        cv.imshow(titles[i],images[i])
        k = cv.waitKey(0)
        if k==ord("s"):
            filename = 'pokecode_'+titles[i]+'.jpeg'
            cv.imwrite(os.path.join(path_prepared,filename),images[i])
    
    shutil.move(path_raw+'pokecode.jpeg',path_archive)

