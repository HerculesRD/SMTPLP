#!/usr/env/python2.7

import smtplib, sys
import argparse
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SMTPLP")

def usage ():
	print "python SMTPLP.py -i <host> -w <wordlist> -d <domain>"
	print "Example: python smtpLP.py -i 192.168.0.2 -w rockyou.txt -d domain.com"

parser = argparse.ArgumentParser(description="Do something.")
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-i", type=str, required=True)
requiredNamed.add_argument("-w", type=str, required = True)
requiredNamed.add_argument("-d", type=str, required = True)

args = parser.parse_args()    

dominio= args.d

file=open(args.w,'r')

user=file.readline()
userFormat=user.replace('\n', '')

print(ascii_banner)

while user:
	s=smtplib.SMTP(args.i)
	correo = userFormat+"@"+dominio
	resultado=s.verify(correo)
	if resultado[0] == 250 or resultado[0]==251 or resultado[0]==252:
		print "Usuario SMTP encontrado: "+correo
	s.quit()
	user=file.readline()
	userFormat=user.replace('\n', '')
