import os
import cv2 as cv
from pathlib import Path
import shutil


#--- Utility Functions ---#

## Uses the cv2 module to return a greyscaled version of a given image
def grayscale(image):
    return cv.cvtColor(image,cv.COLOR_BGR2GRAY)

## Uses the cv2 module to return a median-blur version of a given image (removes "salt & pepper" noise from the image)
def remove_noise(image):
    return cv.medianBlur(image,5)

## Uses the cv2 module to return a gaussian-blur version of a given image (blurs pixels in a gaussian distribution, removing "gaussian" noise)
def gauss_blur(image):
    return cv.GaussianBlur(image,(5,5),0)

## Uses the cv2 module to return a binary (pure black & pure white, no greys) version of a given image
def thresholding(image):
    return cv.threshold(gauss_blur(image), 0.0, 255.0, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

## Counts the number of images inside the images_prepared folder and returns the count value
def getNum_Prepared():
    num=0
    for image in os.listdir(getPath_Prepared()):
        if (image.endswith(".png")| image.endswith(".jpeg") | image.endswith(".jpg")):
            num+=1
    return num

## Counts the number of images inside the images_archive folder and returns the count value
def getNum_Archived():
    num=0
    for image in os.listdir(getPath_Archive()):
        if (image.endswith(".png")| image.endswith(".jpeg") | image.endswith(".jpg")):
            num+=1
    return num

## Checks if the images_raw folder exists in the library folder and creates the folder if it doesn't. It then returns the path to images_raw
def getPath_Raw():
    path_raw = 'library/images_raw/'
    Path(path_raw).mkdir(parents=True, exist_ok=True)
    return path_raw

## Checks if the archive folder exists in the library folder and creates the folder if it doesn't. It then returns the path to archive
def getPath_Archive():
    path_archive = 'library/archive/'
    Path(path_archive).mkdir(parents=True, exist_ok=True)
    return path_archive

## Checks if the images_prepared folder exists in the library folder and creates the folder if it doesn't. It then returns the path to images_prepared
def getPath_Prepared():
    path_prepared = 'library/images_prepared/'
    Path(path_prepared).mkdir(parents=True, exist_ok=True)
    return path_prepared


#--- Pre-Processing for Images ---#

## The Main function for pre-processing images. Using images from the images_raw folder, it creates modified versions of those images and moves both vesion into sepeate designated folders
def prepare_images():
    
    ## Number of pre-existing images in images_prepared folder
    num_prepared = getNum_Prepared()
    ## Number of pre-existing images in archive folder
    num_archived = getNum_Archived()

    ## Iterate through every item in the images_raw folder
    for image in os.listdir(getPath_Raw()):

        ## If an item is an image (ending with ".jpeg", ".png" or ".jpg")...
        if (image.endswith(".png")| image.endswith(".jpeg") | image.endswith(".jpg")):

            ## Use OpenCV module to access the image
            img = cv.imread(getPath_Raw()+image, cv.IMREAD_COLOR)
            assert img is not None, "Image not found(?)"
            
            ## Create a grayscale version of the image
            gray = grayscale(img)
            ## Remove noise from the greyscale version
            quiet = remove_noise(gray)
            ## Convert the greyscale version into a binary image
            threshed = thresholding(quiet)
            
            ## Rename the newly prepared image according to the number of images already in the images_prepared folder
            num_prepared+=1
            filename = 'pokecode_' + str(num_prepared) + '.jpeg'

            ## Put the newly prepared image into the images_prepared folder
            cv.imwrite(os.path.join(getPath_Prepared(),filename),threshed)
            
            ## Rename the original image according to the number of images already in the archive folder
            num_archived+=1
            filename = 'pokecode_' + str(num_archived) + '.jpeg'

            ## Check if archive already contains an image of the same name
            if os.path.exists(getPath_Archive() + filename):
                ## Remove the old image if one is found
                os.remove(getPath_Archive() + filename)

            ## Move the original image from images_raw into the archive folder
            shutil.move(getPath_Raw() + image, getPath_Archive()+filename)

    ## All existing images in images_raw have been pre-processed
