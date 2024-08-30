import PreProcessing
import Processing


def main():
    ## Pre-Process Images to make OCR more accurate
    PreProcessing.prepare_images()

    ## Process the images, search them for the desired code pattern and return the codes in a string list
    newcodes=Processing.process_images()

    ## Add the new codes to the records.txt file
    add_codes(newcodes)

    ## The codes can be accessed and copied from the records.txt file and pasted on Pokemon.com/Redeem to be redeemed


# This function takes a string list of new codes and appends the records.txt file
    def add_codes(newcodes:list[str]):
        records = open("records.txt","a")
        for codes in newcodes:
            records.write("\t"+codes+"\n")


if __name__=="__Main__":
    main()