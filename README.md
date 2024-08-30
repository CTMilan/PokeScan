# PokeScan

## About PokeScan

### What does it do?
PokeScan takes photos of Pokemon Code Cards, reads their codes, and adds the codes into a text file named records.txt

### What is a Code Card?
If you've ever opened a Pokemon TCG pack you've undoubtedly found a card looking like this:
![image](https://github.com/user-attachments/assets/10495c46-a16c-491a-b0f6-ece4c812066c)
These cards have redeemable codes on them (see arrow on reference photo) that can be used at Pokemon.com/Redeem where you'll be given randomized rewards for the online game Pokemon TCG Live.

### How does it work?
PokeScan utilizes OpenCV for pre-processing images, PIL for image handling, and PyTesseract for the Tesseract OCR (Optical Character Recognition) Engine. In short, PokeScan takes a user-provided photo of a code card, modifies it for easier processing using OpenCV, scans the modified photo for text strings using PyTesseract, and retrieves codes from the text strings. Any new codes gathered are then added to the list of codes in the records.txt file.

### How do I use it?
Simply take a photo of a code card against a **black background**, then after ensuring the photo is a .png, .jpg, or .jpeg, place it in the library/images_raw/ folder. **Note: PokeScan can handle multiple code cards, but each card must have its own photo**. Once the photos are loaded into the images_raw folder you may start PokeScan by running the Main.py Python script. After PokeScan is done running you can find your codes in the records.txt file. If no codes appear in the file, close and reopen the file. If after this the codes are still absent or they're incorrect, you can try retaking the photos and rerunning them through PokeScan as Tesseract (and this PokeScan itself) are imperfect and will occasionally misread codes.

### What do I do with record.txt
If you've run PokeScan you can now find your codes in the record.txt file. Use can now copy these codes individually and paste them into the redeem code area on pokemon.com/Redeem for rewards. I recommend deleting any codes from records.txt after you've redeemed them. Although leaving old codes shouldn't affect the future use of PokeScan, any old codes will take up space and possibly get mixed up with newer unredeemed codes.

## Why make PokeScan?
Recently I got back into one of my childhood passions, Pokemon. I've started collecting cards again and while opening new packs I noticed the code cards included in each. I got curious, did a quick Google, and learned about the online version of the card game Pokemon TCG Live. Eagerly, I made an account and played (and tragically lost) a few matches. Despite not being very good, I was still interested in redeeming the code cards I had piling up around me from opening packs. I tried using my phone camera to read the QR codes but for some reason, it wasn't working. The only options I had left were to painstakingly type out each 13-digit code from my immense stack of code cards OR create a small program to do all the typing for me (the copy-pasting seems easy enough). So I sat down, did an ungodly amount of googling, and managed to scrap together PokeScan.

## About Me
Hey there! I'm a Software Engineering student, as of writing this I'm going into my third year this September and I'll soon be on the hunt for internships. In the meantime, I've been practicing what I know and pushing myself into subject areas I'm unfamiliar with. If you have any questions, helpful advice, or critiques of my work please feel free to reach out! I'm always looking for opportunities to learn and develop!

## Author's Note
I'm a novice developer and would appreciate any advice or critiques! This is also my first Python project **ever**, I usually work with Java, but figured I should expand my Python knowledge a bit and thought this personal project would be a good start. Thank you for giving it a look and reading this far!
