#!/usr/bin/python3

import socket
import datetime
import base64
import os
import sys
import threading
import random
import time
import rsa
import pyfiglet
from termcolor import colored
from packages import chat_keygen

os.system("clear")
#KEY LOADER
def generate():
	global pubkey
	global prikey
	with open('sending_key.txt', 'rb')as f:
		pubkey = f.read()
		os.remove('sending_key.txt')
	with open('prikey.pem', 'rb')as f:
		prikey = rsa.PrivateKey.load_pkcs1(f.read())

#RECORDING
def recorder():
	global record
	global othername

	user = os.getlogin()
	locate = "/home/" + user + "/Documents/chatbox/recording/"
	if not os.path.exists(locate):
		os.makedirs(locate)
	samay = datetime.datetime.now()
	day = str(samay.day)
	month = str(samay.month)
	hour = str(samay.hour)
	minute = str(samay.minute)
	rec_file = othername + "_D" + day + "_M" +  month + "_h" + hour + "_m" + minute
	record = open(locate + rec_file + ".txt", 'w')

#SENDING
def send(chat):
	global target
	global sock
	global send_key

	cipher = rsa.encrypt(chat.encode('utf-8'), send_key)
	try:
		target.send(cipher)
	except:
		sock.send(cipher)

def sendfile(org_file):
	global target
	global sock
	global send_key

	with open(org_file, 'rb') as org:
		while True:
			org_data = org.read(117)
			if not org_data: break
			cipher = rsa.encrypt(org_data,send_key)
			cipher = base64.b64encode(cipher)
			try:
				target.send(cipher)
			except:
				sock.send(cipher)
			time.sleep(0.2)
	time.sleep(0.2)
	done = "done"
	cip = rsa.encrypt(done.encode('utf-8'),send_key)
	try:
		target.send(cip)
	except:
		sock.send(cip)
	print (colored("[+]File sent", 'magenta'))
	org.close()

def sender():
	global record
	global rec_cmd
	global username
	global pubkey
	global target
	global sock

	generate()
	cipher = base64.b64encode(pubkey)
	try:
		target.send(cipher)
	except:
		sock.send(cipher)
	time.sleep(1)

	while(True):
		chat = input("You: ")
		msg = username + ": " + chat
		try:
			send(msg)
		except:
			break

		if (rec_cmd):
			record.write(msg + "\n")
		if (chat == "record()"):
			rec_cmd = True
			recorder()
		elif (chat == "end()"):
			print (colored("[!!] Connection terminated", 'red'))
			time.sleep(1)
			try:
				target.close()
			except:
				sock.close()
			break
		elif (chat[:4] == "send"):
			try:
				sendfile(chat[5:])
			except:
				print (colored("failed to send",'red'))
		elif (chat == "help()"):
			help_option = '''send 'file name'        -->        Send file to contact\nrecord()        -->        Start recording the chat\nend()        -->        Exit the messenger'''
			print (colored(help_option, 'blue'))

#RECEIVING
def rec():
	global target
	global sock
	global result
	global prikey
	global othername

	try:
		data = target.recv(1024)
	except:
		data = sock.recv(1024)
	result = rsa.decrypt(data,prikey).decode('utf-8')
	tmp = result.split(':')
	othername = tmp[0]

def recfile(org_f):
	global prikey
	global target
	global sock
	global rece

	user = os.getlogin()
	locate = "/home/" + user + "/Documents/chatbox/files/"
	if not os.path.exists(locate):
		os.makedirs(locate)

	org_file = open(locate + org_f, 'wb')
	while True:
		try:
			data = target.recv(1024)
		except:
			data = sock.recv(1024)
		try:
			org_data = rsa.decrypt(data,prikey).decode('utf-8')
			if(org_data == "done"):
				break
		except:
			data = data[:344]
			data = base64.b64decode(data)
			org_data = rsa.decrypt(data,prikey)
			org_file.write(org_data)
	print ("\n[+]File received", 'magenta')
	print ("You: ", end = "")
	org_file.close()
	rece = True

def receiver():
	global record
	global rec_cmd
	global target
	global sock
	global result
	global prikey
	global send_key
	global rece
	global username
	global othername
	rece = True

	try:
		data = target.recv(1024)
	except:
		data = sock.recv(1024)
	result = base64.b64decode(data)
	with open('sending_key.txt','wb') as f:
		f.write(result)
	f.close()
	with open('sending_key.txt', 'rb') as f:
		send_key = rsa.PublicKey.load_pkcs1(f.read())
	f.close()
	print (colored("[+]Key received", 'cyan'))

	while (True):
		if(rece):
			rec()
			oprt = result.replace(othername + ": ", "")
		if(rec_cmd):
			record.write(result + "\n")
		if(oprt == "record()"):
			rec_cmd = True
			recorder()
		elif (oprt[:4] == "send"):
			try:
				recfile(oprt[5:])
			except:
				print (colored("failed to receive file",'red'))
		elif (result == ""):
			continue
		elif (oprt == "end()"):
			print (colored("[!!] Connection terminated", 'red'))
			send(username + ": " + "end()")
			try:
				target.close()
			except:
				sock.close()
			break
		else:
			c = os.get_terminal_size().columns
			c = int(c/2)
			print ("\n" + " "*c + result + "\nYou: ", end = "")


#MESSENGER
def thread():
	global Lrun
	Threadsend = threading.Thread(target=sender)
	Threadreceive = threading.Thread(target=receiver)
	Threadsend.start()
	Threadreceive.start()
	Threadreceive.join()
	Threadsend.join()
	Lrun = False

#CONNECTION ESTABLISHING
def connector():
	global ran_num
	global sock
	global Lrun

	Lrun = True
	ran_num-=1
	while (ran_num >= 1):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((RHOST, RPORT))
			print (colored("[+] Connection successful: " + str(RHOST), 'green'))
			thread()
			break
		except:
			time.sleep(1)
			if (ran_num >= 1):
				connector()
	if (Lrun):
		listener()

def listener():
	global ip
	global target
	global s

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((LHOST, LPORT))
	s.listen (1)
	target, ip = s.accept()
	print (colored("[+] Connection successful: " + str(RHOST), 'green'))
	thread()
	return

def main():
	global s
	global sock
	global LHOST
	global LPORT
	global RHOST
	global RPORT
	global username
	global rec_cmd
	rec_cmd = False

	print ("Your IP: ")
	LHOST = os.system("hostname -I")
	LHOST = str(LHOST)
	LPORT = 54321
	RHOST = input("Contact's IP: ")
	RPORT = 54321

	print (colored("[+] Connecting...", 'yellow'))
	connector()
	return

def banner():
	banner = pyfiglet.figlet_format("CHATBOX",font = ran_font)
	print (colored(banner, ran_color))

ran_num = random.randint(2,9)
fonts = ["banner","big","bubble","digital","emboss","emboss2","future","letter","mini","pagga","script","shadow","slant","small","smblock"]
ran_font = random.choice(fonts)
colors = ["grey","red","green","yellow","blue","magenta","cyan","white"]
ran_color = random.choice(colors)

arg = sys.argv[1]
if (arg == "-h" or arg == "help"):
	help_option = '''chatbox.py 'username'        -->        Set your username\nsend 'file name'        -->        Send file to contact\nrecord()        -->        Start recording the chat\nhelp()        -->        Show help option during chat\nend()        -->        Exit the messenger'''
	print (colored(help_option, 'blue'))
else:
	username = arg
	try:
		main()
	except:
		exit()
