# RBPM (Really Bad Password Manager) 

import sys
from cryptography.fernet import Fernet

# Generate Key
# - Generates a key that will be used to encrypt and decrypt all of the passwords stored in the manager
# - Just like your house key, you should keep this very safe 

def generate_key():
	key = Fernet.generate_key()
	return key


# Encrypt Password
# - Encrypts a plaintext password
# - Adds the encrypted password to definitelynotpwds.txt

def encrypt_pwd(plaintext_pwd, key):
	fernet = Fernet(key)
	token = fernet.encrypt(plaintext_pwd)
	with open("definitelynotpwds.txt", "a") as f:
		f.write(token)
		f.write("\n")

# Decrypt Passwords
# - Decrypts definitelynotpwds.txt

def decrypt_pwds(key): 
	fernet = Fernet(key) 
	
	with open("definitelynotpwds.txt") as f:
		tokens = f.read().splitlines()

	for token in tokens:
		print fernet.decrypt(token)


# Main Function

if __name__ == "__main__": 
	

	command = raw_input("What is your key? If you don't have a key enter 'generate': ") 

	if command is "generate":
		key = generate_key()
		print "Here is your key. Keep it somewhere safe!!! \n " + key 
	else:
		key = command

	while (True): 
		
		command = raw_input("Ok. What's next? Enter encrypt/decrypt/quit: ") 

		if command is "encrypt": 
			plaintext = raw_input("What is the password you want to encrypt? ") 
			encrypt_pwd(plaintext, key)
			print "Success! The super secret password has been encrypted." 

		elif command is "decrypt":
			decrypt_pwds(key)
		
		elif command is "quit":
			print "Don't worry, your passwords are safe-ish with me. See you later!" 
			sys.exit()  
