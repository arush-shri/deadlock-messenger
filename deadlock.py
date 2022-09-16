#! /usr/bin/python3

import pyfiglet
from termcolor import colored
import random
import os
#IMPORTING OTHER CODES
from packages import tenc
from packages import filenc
from packages import generator

#FONT SELECTION
fonts = ["banner","big","bubble","digital","emboss","emboss2","future","letter","mini","pagga","script","shadow","slant","small","smblock"]

#COLOR SELECTION
colors = ["grey","red","green","yellow","blue","magenta","cyan","white"]

#CHOICE
def choice():
	print ("1.Text Cryptography\n2.File Cryptography\n3.Key Generation\n4.Exit")
	print (colored("Generate a key if using for first time", 'blue'))
	print (colored("To use messenger type 'chatbox.py -h' in terminal", 'yellow'))
	choice = input()
	if (choice == '1'):
		tenco()
	if (choice =='2'):
		filenco()
	if (choice == '3'):
		generate()
	if (choice == '4'):
		exit()
#BANNER
def banner():
	global ran_color
	ran_font = random.choice(fonts)
	ran_color = random.choice(colors)
	banner = pyfiglet.figlet_format("DEADLOCK",font = ran_font)
	print (colored(banner, ran_color))
	print (colored(__version__, ran_color))
	print (colored("If using for first time generate a key first", 'magenta'))

#TEXT CRYPTOGRAPHY
def tenco():
	os.system("clear")
	tenc.banner()
	tenc.choice()
	os.system("clear")
	choice()

#FILE CRYPTOGRAPHY
def filenco():
	os.system("clear")
	filenc.banner()
	filenc.choice()
	os.system("clear")
	choice()

#KEY GENERATION
def generate():
	os.system("clear")
	generator.generate()
	choice()

__version__ = 1.2.2
os.system("clear")
banner()
choice()
