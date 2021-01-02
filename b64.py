import sys
import base64

def encode(the_string):
	if the_string:
		encoded_bytes = base64.b64encode(the_string.encode("utf-8"))
		encoded_string = str(encoded_bytes, encoding="utf-8")
		sys.stdout.write(encoded_string + "\n")
		sys.stdout.close()

def decode(the_string):
	if the_string:
		decoded_bytes = base64.b64decode(the_string)
		decoded_string = str(decoded_bytes, encoding="utf-8")
		sys.stdout.write(decoded_string + "\n")
		sys.stdout.close()

def usage():
	sys.stderr.write("You used this wrong. Pipe in (aka '|') your input using -e or -d flags, and redirect your output if you want using '>' or '>>'." + '\n')

def main():
	if len(sys.argv) != 2:
		usage()
		exit(2)

	if sys.argv[1] in ('-e', '--encode'):
		for line in sys.stdin:
			encode(line.strip('\n'))
	elif sys.argv[1] in ('-d', '--decode'):
		for line in sys.stdin:
			decode(line.strip('\n'))
	else:
		sys.stderr.write("Unhandled arg" + '\n')

if __name__ == '__main__':
	main()