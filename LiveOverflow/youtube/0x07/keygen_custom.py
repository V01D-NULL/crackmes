####
#
#  A keygen for the license_2 challenge by LiveOverflow.
#  --
#  Functions:
#	check_key ~ Args: string, Purpose: Use the ord() function on each character in the string and return the decimal values of the ascii string
#	gen_key   ~ Args: None,   Purpose: Generate a random string (key). This key will be passed to check_key as the argument
#	main      ~ Args: None,   Purpose: Generate random string, get it's ascii values in decimal format, !! Check if ascii_key is greater than 916 since the data is just being appended to sum in check_key. If that is the case use a new password !!
#
####
import random
import sys

key = ""

def check_key(key):
	sum = 0
	for char in key:
		sum += ord(char)
	return sum


def gen_key():
	global key
	payload = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
	key = key + random.choice(payload)
	return key


if __name__ == '__main__':
	try:
		while True:
			key 	    = gen_key()
			ascii_key   = check_key(key)
			if ascii_key > 916:
				key = ""
			if ascii_key == 916:
				print(f'Key found: {key}')
	except KeyboardInterrupt:
		print("\nK bhai")
		sys.exit(0)
