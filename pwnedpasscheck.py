#!/usr/bin/env python

import pwnedpasswords
import argparse
import time
import sys



# Colors for output
R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

if sys.version_info[0] >= 3:
	raw_input = input
	unicode = str

# Commandline arguments
ap = argparse.ArgumentParser()
ap.add_argument('-p', '--password', required=False,
help='The password you want to test')
ap.add_argument('-f', '--file', required=False,
help='Load a file with multiple passwords to check')

arg = ap.parse_args()

status = False
fparse = False

addr = arg.password
file = arg.file

if arg.password:
	status = True
if arg.file:
	fparse = True
if not status:
	pass


def main():
	global addr, file
	# starts calculating script runtime
	start = time.time()

	# quit function prints total script runtime and exits
	def quit():
		print ('\n' + G + '[+]' + C + ' Completed in ' + W + str(time.time()-start) + C + ' seconds.' + W)
		exit()

	def check():
		print ('\n' + G + '[+]' + C + ' Looking for Breaches...' + W)
		time.sleep(5)
		if str(pwnedpasswords.check(addr))!='0':
		    print ('\n' + G + '[+]' + R + ' Oh no - pwned!')
		    print ('\n' + G + '[+]' + R + ' This password has been seen ' +
		           W + str(pwnedpasswords.check(addr)) + R + ' times before.')
		else:
		    print ('\n' + G + '[+]' + C + ' Good news - no pwnage found!')
		
	if not status and not fparse:
		addr = raw_input(G + '[+]' + C + ' Enter password : ' + W)
		check()
	elif status == True:
		print (G + '[+]' + C + ' Checking Breach status for ' + W + '{}'.format(addr))
		check()
	elif fparse == True:
		print (G + '[+]' + C + ' Reading passwords from ' + W + '{}'.format(file))
		with open(file) as dict:
			for line in dict:
				line = line.strip()
				addr = line
				if addr != '':
					print ('\n' + G + '[+]' + C + ' Checking Breach status for ' + W + '{}'.format(addr))
					check()
	quit()
try:
	main()
except KeyboardInterrupt:
	print ('\n' + R + '[!]' + C + ' Keyboard Interrupt.' + W)
exit()