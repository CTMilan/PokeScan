import os
import cv2 as cv
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

def getNum_Prepared():
    num=0
    for image in os.listdir(getPath_Prepared()):
        if (image.endswith(".png")| image.endswith(".jpeg") | image.endswith(".jpg")):
            num+=1
    return num

def getNum_Archived():
    num=0
    for image in os.listdir(getPath_Archive()):
        if (image.endswith(".png")| image.endswith(".jpeg") | image.endswith(".jpg")):
            num+=1
    return num

def getPath_Raw():
    path_raw = 'library/images_raw/'
    Path(path_raw).mkdir(parents=True, exist_ok=True)
    return path_raw

def getPath_Archive():
    path_archive = 'library/archive/'
    Path(path_archive).mkdir(parents=True, exist_ok=True)
    return path_archive

def getPath_Prepared():
    path_prepared = 'library/images_prepared/'
    Path('library/images_prepared').mkdir(parents=True, exist_ok=True)
    return path_prepared



def prepare_images():
    
    num_prepared = getNum_Prepared()
    num_archived = getNum_Archived()

    for image in os.listdir(getPath_Raw()):
        if (image.endswith(".png")| image.endswith(".jpeg") | image.endswith(".jpg")):

            original_name = os.path.basename(image)
            img = cv.imread(getPath_Raw()+image, cv.IMREAD_COLOR)
            assert img is not None, "Image not found(?)"
            
            gray = grayscale(img)
            quiet = remove_noise(gray)
            threshed = thresholding(quiet)
            
            filename = 'pokecode_' + str(num_prepared) + '.jpeg'

            cv.imwrite(os.path.join(getPath_Prepared(),filename),threshed)
            num_prepared+=1

            if os.path.exists(getPath_Archive() + filename):
                os.remove(getPath_Archive() + filename)

            shutil.move(getPath_Raw() + original_name, getPath_Archive()+filename)

