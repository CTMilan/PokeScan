import PreProcessing
import Processing

def add_codes(newcodes:list[str]):
    records = open("records.txt","a")
    for codes in newcodes:
        records.write("\t"+codes+"\n")


#print("Preparing images")
PreProcessing.prepare_images()
#print("Done preparing images")
#print("Processing images")
newcodes=Processing.process_images()
#print("Done processing images")
#print("Add new codes to Records.txt")
add_codes(newcodes)
#print("New codes have been added")


