import string

def caesar(plain_text, shift, alphabet=string.ascii_lowercase):
	shifted_alphabet = alphabet[shift:] + alphabet[:shift]
	return plain_text.translate(plain_text.maketrans(alphabet, shifted_alphabet))

def main():
	for i in range(1, 25):
		print(caesar("aipgsqi fego", i))

if __name__ == '__main__':
	main()