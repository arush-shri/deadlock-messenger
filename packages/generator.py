#! /usr/bin/python3

import rsa

def generate():

	public,private = rsa.newkeys(1024)
	with open('pubkey.pem','wb') as f:
		f.write(public.save_pkcs1('PEM'))
	with open('prikey.pem','wb') as f:
	        f.write(private.save_pkcs1('PEM'))
