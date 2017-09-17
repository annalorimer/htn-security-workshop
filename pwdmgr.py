# RBPM (Really Bad Password Manager) 

import sys
from cryptography.fernet import Fernet


# Generate Key
# - Generates a key that will be used to encrypt and decrypt all of the passwords stored in the manager

def generate_key():
	
	return key


# Encrypt Password
# - Encrypts a plaintext password
# - Adds the encrypted password to definitelynotpwds.txt

def encrypt_pwd(plaintext_pwd, key):
	

	with open("definitelynotpwds.txt", "a") as f:
		f.write(token)
		f.write("\n")

# Decrypt Passwords
# - Decrypts definitelynotpwds.txt
# - Prints the decrypted passwords

def decrypt_pwds(key): 
	
	with open("definitelynotpwds.txt") as f:
		tokens = f.read().splitlines()



# Main Function

if __name__ == "__main__": 
	

	command = raw_input("What is your key? If you don't have a key enter 'generate': ") 

	if (command == "generate"):
		
		print "Here is your key. Keep it somewhere safe!!! \n " + key 
	else:
		key = command

	while (True): 
		
		command = raw_input("Ok. What's next? Enter encrypt/decrypt/quit: ") 

		if (command == "encrypt"): 
			plaintext = raw_input("What is the password you want to encrypt? ") 
			
			print "Success! The password has been encrypted." 

		elif (command == "decrypt"):
	
	
		elif (command == "quit"):
			print "Don't worry, your passwords are safe-ish with me. See you later!" 
			sys.exit()  
