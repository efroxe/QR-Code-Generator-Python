import getpass
import os
import sys
import pyqrcode
import png
from pyqrcode import QRCode

# Main message, it does not effect the code, only prints something
print("""
********************************************************************
WELCOME TO QR CODE GENERATOR (BETA)

Make sure to read READTHIS.md in your folder
for clear instructions of this product.

VERSION: 1.0
********************************************************************
\n 
""")

# Get the username of the system to use it to save the .png file
username = getpass.getuser()

# Input the link
link = input("Please enter the link: \n")

# Try to create the file
try:
    # Save the link in a variable and create with that the .png file
    url = pyqrcode.create(link)

    # Save the created .png in with the given file name in the desktop
    url.png(r"C:/Users/"+username+"/Desktop/QRGENERATED.png", scale=6)

    # Print that the file created successfully if the file was created
    print("File created successfully!")

# If the file couldn't be created, print an error
except Exception as e:
    print("Could no create file.")
