#! /usr/bin/python3

import pyfiglet
from termcolor import colored
import random
import os
#IMPORTING OTHER CODES
from packages import tenc
from packages import filenc
from packages import generator
from packages import messenger

#FONT SELECTION
fonts = ["banner","big","bubble","digital","emboss","emboss2","future","letter","mini","pagga","script","shadow","slant","small","smblock"]
ran_font = random.choice(fonts)

#COLOR SELECTION
colors = ["grey","red","green","yellow","blue","magenta","cyan","white"]
ran_color = random.choice(colors)

#CHOICE
def choice():
	print ("1.Text Cryptography\n2.File Cryptography\n3.Chat Box\n4.Key Generation\n5.Exit")
	choice = input()
	if (choice == '1'):
		tenco()
	if (choice =='2'):
		filenco()
	if (choice == '3'):
		msg()
	if (choice == '4'):
		generate()
	if (choice == '5'):
		exit()
#BANNER
def banner():
	banner = pyfiglet.figlet_format("DEADLOCK\nCHATBOX",font = ran_font)
	print (colored(banner, ran_color))

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

#MESSENGER
def msg():
	os.system("clear")
	messenger.banner()
	messenger.main()
	os.system("clear")
	choice()

#KEY GENERATION
def generate():
	os.system("clear")
	generator.generate()
	choice()

os.system("clear")
banner()
choice()
