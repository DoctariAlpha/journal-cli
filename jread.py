import sys, getpass
from crypto_bin import decrypt
'''
	read encrypted files.
	python jread.py filepath
'''

filepath = sys.argv[1]
key = getpass.getpass('key: ')

with open(filepath,'rb') as file:
	r = file.read()
dtext = decrypt(key,r).decode('utf-8')
dtext_lines= dtext.split('\n')
for line in dtext_lines:
	print('~ ',line)