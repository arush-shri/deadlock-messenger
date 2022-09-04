#!/usr/bin/python3
import os

def installer():
	try:
		import termcolor
	except:
		try:
			os.system("pip install termcolor")
		except:
			print (colored("[!!]Unable to install 'termcolor'", 'red'))
			print (colored("Try manually 'pip install termcolor'",'blue'))
			from termcolor import colored
	try:
		import rsa
	except:
		try:
			os.system("pip install rsa")
		except:
			print (colored("[!!]Unable to install 'rsa'", 'red'))
			print (colored("Try manually 'pip install rsa'",'blue'))
	try:
		import socket
	except:
		try:
			os.system("pip install socket")
		except:
			print (colored("[!!]Unable to install 'socket'", 'red'))
			print (colored("Try manually 'pip install socket'",'blue'))
	try:
		import json
	except:
		try:
			os.system("pip install json")
		except:
			print (colored("[!!]Unable to install 'json'", 'red'))
			print (colored("Try manually 'pip install json'",'blue'))
	try:
		import base64
	except:
		try:
			os.system("pip install base64")
		except:
			print (colored("[!!]Unable to install 'base64'", 'red'))
			print (colored("Try manually 'pip install base64'",'blue'))
	try:
		import threading
	except:
		try:
			os.system("pip install threading")
		except:
			print (colored("[!!]Unable to install 'threading'", 'red'))
			print (colored("Try manually 'pip install threding'",'blue'))
	try:
		import pyfiglet
	except:
		try:
			os.system("pip install pyfiglet")
		except:
			print (colored("[!!]Unable to install 'pyfiglet'", 'red'))
			print (colored("Try manually 'pip install pyfiglet'",'blue'))
	try:
		import random
	except:
		try:
			os.system("pip install random")
		except:
			print (colored("[!!]Unable to install 'random'", 'red'))
			print (colored("Try manually 'pip install random'",'blue'))

	lin_ch_mod()

def lin_ch_mod():
	try:
		os.system("sudo chmod +x chatbox.py")
		os.system("sudo chmod +x deadlock.py")
	except:
		print (colored("[!!]Unable to make executable", 'red'))
		exit()
	try:
		os.system("sudo cp chatbox.py /usr/local/bin")
		os.system("sudo cp deadlock.py /usr/local/bin")
		os.system("sudo cp -r packages /usr/local/bin")
	except:
		print (colored("[!!]Unexpected error occured", 'red'))
		exit()

if (os.geteuid() == 0):
	installer()
elif (os.geteuid() != 0):
	print (colored("[!!]Root privileges required", 'red'))
	exit()
