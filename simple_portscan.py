#!/usr/bin/python2
# coding:utf-8


import socket, random, time
from sys import argv
from threading import Thread


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = argv[1]

opn = []
ports = range(65000)
random.shuffle(ports)

def scan(port):
	# print port
	try:
		s.connect((host, int(port)))
		opn.append(port)
		print '\n{} | PORT ON'.format(str(port))
	except Exception, e:
		# print '{} | PORT OFF : {}'.format(str(port), str(e))
		pass



for port in ports:
	getscan = Thread(target=scan, args=(str(port),))
	getscan.start()
	time.sleep(0.01)

print 'OPEN:'
print opn
