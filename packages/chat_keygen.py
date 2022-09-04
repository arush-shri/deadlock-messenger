#! /usr/bin/python3

import rsa
import os

def generator():
	public,private = rsa.newkeys(1024)
	with open('sending_key.pem','wb') as f:
		f.write(public.save_pkcs1('PEM'))
		os.system("mv sending_key.pem sending_key.txt")
	with open('prikey.pem','wb') as f:
		f.write(private.save_pkcs1('PEM'))
generator()
