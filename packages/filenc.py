#! /usr/bin/python3

import rsa
import pyfiglet
import base64
import random
from termcolor import colored


#FONT SELECTION
fonts = ["banner","big","block","bubble","circle","digital","emboss","emboss2","future","ivrit","lean","letter","mini","mnemonic","pagga","script","shadow","slant","small","smblock","smbraille","smscript","smshadow","smslant","standard","term","wideterm"]
ran_font = random.choice(fonts)

#COLOR SELECTION
colors = ["grey","red","green","yellow","blue","magenta","cyan","white"]
ran_color = random.choice(colors)

#BANNER
def banner():
	banner = pyfiglet.figlet_format("FILE\nENCRYPTION\nDECRYPTION",font = ran_font)
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
	org_file = input("Path: ")
	PubKey = getPubKey()
	try:
		en = open(org_file + '.encrypted', "wb")
		with open(org_file, 'rb') as org:
			while True:
				org_data = org.read(117)
				if not org_data: break
				cipher = rsa.encrypt(org_data,PubKey)
				cipher = base64.b64encode(cipher)
				en.write(cipher)
		print (colored("[+]Encryption done", 'green'))
	except:
		print (colored("[!!] Encryption failed", 'red'))
	org.close()
	en.close()
	choice()


#DECRYPTION
def Decrypter():
	file = input("Path:")
	PriKey = getPriKey()
	org_name = file.replace(".encrypted","")
	try:
		org_f = open(org_name, 'wb')
		with open (file, 'rb') as enc_file:
			while True:
				cip_data = enc_file.read(172)
				if not cip_data: break
				cip_data = base64.b64decode(cip_data)
				org_data = rsa.decrypt(cip_data,PriKey)
				org_f.write(org_data)
		print (colored("[+]Decryption successful", 'green'))
	except:
		print (colored("[!!]Decryption failed",'red'))
	enc_file.close()
	org_f.close()
choice()
