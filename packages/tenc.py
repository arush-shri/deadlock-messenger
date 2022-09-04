#! /usr/bin/python3

import rsa
import pyfiglet
import random
from termcolor import colored
import os
import datetime

#FONT SELECTION
fonts = ["banner","big","block","bubble","circle","digital","emboss","emboss2","future","ivrit","lean","letter","mini","mnemonic","pagga","script","shadow","slant","small","smblock","smbraille","smscript","smshadow","smslant","standard","term","wideterm"]
ran_font = random.choice(fonts)

#COLOR SELECTION
colors = ["grey","red","green","yellow","blue","magenta","cyan","white"]
ran_color = random.choice(colors)

#BANNER
def banner():
	banner = pyfiglet.figlet_format("TEXT\nENCRYPTION\nDECRYPTION",font = ran_font)
	print (colored(banner,ran_color))

#YOUR CHOICE
def choice():
	print ("\n1.Encryption\n2.Decryption\n3.Back")
	choice = int(input())
	if (choice == 1):
		Encrypter()
	if (choice == 2):
		Decrypter()
	if (choice == 3):
		return()


#KEY LOADING
def getPriKey():
	with open('prikey.pem', 'rb')as f:
		PriKey = rsa.PrivateKey.load_pkcs1(f.read())
	return PriKey

def getPubKey():
	with open('pubkey.pem', 'rb')as f:
		PubKey = rsa.PublicKey.load_pkcs1(f.read())
	return PubKey


#ENCRYPTION
def Encrypter():
	text = input("Text: ")
	PubKey = getPubKey()
	try:
		cipher = rsa.encrypt(text.encode('utf-8'), PubKey)
		with open(file, "wb") as en:
			en.write(cipher)
		print (colored("[+]Encryption done", 'green'))
	except:
		print (colored("[!!] Encryption failed", 'red'))
	choice()


#DECRYPTION
def Decrypter():
	fi = input("Path: ")
	try:
		with open (fi, 'rb') as de:
			cipher = de.read()
		PriKey = getPriKey()
		text = rsa.decrypt(cipher, PriKey).decode('utf-8')
		print ("Text: ",text)
	except:
		print (colored("[!!]Decryption failed",'red'))
	choice()

user = os.getlogin()
locate = "/home/" + user + "/Documents/Encrypted_text"
if not os.path.exists(locate):
	os.makedirs(locate)
samay = datetime.datetime.now()
day = str(samay.day)
hour = str(samay.hour)
file = "enc_" + day + hour + ".txt"
