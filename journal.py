'''
	 a cli that let's you write and save files with 
	 or without encryption
'''

from crypto_bin import encrypt
import os, getpass

class Main:
	done = False

	@staticmethod
	def quit_():
		Main.done = True

	@staticmethod
	def help_():
		help_str = '''$quit to quit\n$help for help\n$clear to clear screen'''
		print(help_str)

	@staticmethod
	def clear_():
		os.system('clear')

	commands = {
		'$quit':quit_,
		'$help':help_,
		'$clear':clear_,
	}

def get_text_cli():
	text = []

	line = 0
	while not Main.done:
		inp = input(' ~ ')
		if inp in Main.commands:
			Main.commands[inp]()
		else:
			text.append(inp+'\n')
	return text

def encrypt_text(key,text_lines):
	text = ''
	for t in text_lines:
		text+=t
	b_array = bytearray(bytes(text,encoding='utf-8'))
	return encrypt(key,b_array)

def save_e_text(file,text):
	if not os.path.exists(file):
		with open(file,'wb') as file:
			file.write(text)
		return 1
	return 0

def ask_yes_no(prompt):
	inp = input(prompt)
	if inp.lower() in ['yes','y']:
		return 1
	elif inp.lower() in ['no','n']:
		return 0
	else:
		return ask_yes_no(prompt)

def get_filepath(prompt):
	file = input(prompt)
	if file == '':
		file = get_filepath(prompt)
	elif file == '_':
		if not 'journals' in os.listdir('.'):
			os.mkdir('journals')
		return 'journals/j'+str(len(os.listdir('journals')))

	elif os.path.exists(file):
		print('path exists')
		return get_filepath(prompt)

	return file

def main():
	print("Journal")
	Main.help_()
	text = get_text_cli()
	# text_saved = False
	# while not text_saved:
	file = get_filepath('File Path: ')
	# if ask_yes_no('Encrypt File: '):
	key = getpass.getpass('Key: ')
	text_saved = save_e_text(file,encrypt_text(key,text))
	# else:
	# 	text_saved = save_text(file,text)
	print("Text saved successfully")


if __name__ == '__main__':
	main()