from PIL import Image
import pytesseract
from pytesseract import Output
import shutil
import os
import re
from pathlib import Path

def getPath_Prepared():
    path_prepared = 'library/images_prepared/'
    Path('library/images_prepared').mkdir(parents=True, exist_ok=True)
    return path_prepared

def getPath_Used():
    path_used= 'library/images_used/'
    Path(path_used).mkdir(parents=True, exist_ok=True)
    return path_used

def getNum_Used():
    num=0
    for image in os.listdir(getPath_Used()):
        if (image.endswith(".png")| image.endswith(".jpeg") | image.endswith(".jpg")):
            num+=1
    return num


def process_images()->list[str]:

    num_used = getNum_Used()

    pokecode="No PokeCode Detected"

    newcodes=[]

    for image in os.listdir(getPath_Prepared()):
        if (image.endswith(".png")| image.endswith(".jpeg") | image.endswith(".jpg")):

            img = Image.open(getPath_Prepared()+image)
            assert img is not None, "Image not found(?)"
            
            raw_data = pytesseract.image_to_data(img,output_type=Output.DICT)
            keys = list(raw_data.keys())

            loose_pattern = '^.{3}-.{4}-.{3}-.{3}$'
            perfect_pattern = '^([A-Z]|[0-9])([A-Z]|[0-9])([A-Z]|[0-9])-([A-Z]|[0-9])([A-Z]|[0-9])([A-Z]|[0-9])([A-Z]|[0-9])-([A-Z]|[0-9])([A-Z]|[0-9])([A-Z]|[0-9])-([A-Z]|[0-9])([A-Z]|[0-9])([A-Z]|[0-9])'

            for string_num in range(len(raw_data['text'])):
                #print(raw_data['text'][string_num])
                if re.match(loose_pattern, raw_data['text'][string_num]):
                    pokecode = raw_data['text'][string_num]
                    break

            print("New PokeCode: "+pokecode)
            newcodes.append(pokecode)

            newname = 'pokecode_' + str(num_used) + '(used).jpeg'
            num_used+=1

            if os.path.exists(getPath_Used() + newname):
                os.remove(getPath_Used() + newname)
            shutil.move(getPath_Prepared() + image, getPath_Used() + newname)
        
    return newcodes
        
