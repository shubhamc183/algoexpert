# https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
def caesarCipherEncryptor(string, key):
  cipher = ""
	for character in string:
		cipher += chr(ord('a') + (ord(character) - ord('a') + key % 26) % 26)
	return cipher
