from PIL import Image
import pytesseract
from pytesseract import Output
import shutil
import os
import re
from pathlib import Path

## Checks if the images_prepared folder exists in the library folder and creates the folder if it doesn't. It then returns the path to images_prepared
def getPath_Prepared():
    path_prepared = 'library/images_prepared/'
    Path(path_prepared).mkdir(parents=True, exist_ok=True)
    return path_prepared

## Checks if the images_used folder exists in the library folder and creates the folder if it doesn't. It then returns the path to images_used
def getPath_Used():
    path_used= 'library/images_used/'
    Path(path_used).mkdir(parents=True, exist_ok=True)
    return path_used

## Counts the number of images inside the images_used folder and returns the count value
def getNum_Used():
    num=0
    for image in os.listdir(getPath_Used()):
        if (image.endswith(".png")| image.endswith(".jpeg") | image.endswith(".jpg")):
            num+=1
    return num

## The main function for processing images. Returns a string list of new codes pulled from images in the images_prepared folder
def process_images()->list[str]:

    ## Number of images in the images_used folder
    num_used = getNum_Used()

    ## Default pokecode declaration
    pokecode="No PokeCode Detected"

    ## Initialize newcodes list as empty
    newcodes=[]

    ## Iterate through every item in the images_prepared folder
    for image in os.listdir(getPath_Prepared()):

        ## If an item is an image (ending with ".jpeg", ".png" or ".jpg")...
        if (image.endswith(".png")| image.endswith(".jpeg") | image.endswith(".jpg")):

            ## Then begin image processing...

            ## Use PIL module to access the image
            img = Image.open(getPath_Prepared()+image)
            assert img is not None, "Image not found(?)"
            
            ## Use PyTesseract module to gather the image data
            raw_data = pytesseract.image_to_data(img,output_type=Output.DICT)

            ## Create a template pattern to search the image data for
            loose_pattern = '^.{3}-.{4}-.{3}-.{3}$'
            #perfect_pattern = '^([A-Z]|[0-9])([A-Z]|[0-9])([A-Z]|[0-9])-([A-Z]|[0-9])([A-Z]|[0-9])([A-Z]|[0-9])([A-Z]|[0-9])-([A-Z]|[0-9])([A-Z]|[0-9])([A-Z]|[0-9])-([A-Z]|[0-9])([A-Z]|[0-9])([A-Z]|[0-9])'

            ## Iterate through the strings obtained by PyTesseract
            for string_num in range(len(raw_data['text'])):
                
                #print(raw_data['text'][string_num])

                ## Use RegEx module 're' to match the string to the template pattern
                if re.match(loose_pattern, raw_data['text'][string_num]):
                    ## If a match is found copy it to the pokecode variable
                    pokecode = raw_data['text'][string_num]
                    ## and break out of the loop (there is only one code to be found per image)
                    break

            ## Print the new code and add it to the list of discovered codes
            print("New PokeCode: "+pokecode)
            newcodes.append(pokecode)

            ## Rename the processed image according to the number of images already in the images_used folder
            num_used+=1
            newname = 'pokecode_' + str(num_used) + '(used).jpeg'
            
            ## Check if images_used already contains an image of the same name
            if os.path.exists(getPath_Used() + newname):
                ## Remove the old image if one is found
                os.remove(getPath_Used() + newname)
            
            ## Move the now used image from images_prepared into images_used
            shutil.move(getPath_Prepared() + image, getPath_Used() + newname)
        
    ## Return the list of codes captured from the prepared images
    return newcodes
        