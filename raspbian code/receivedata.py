import time
import serial
import requests

ser = serial.Serial(port='/dev/ttyS2', baudrate=9600, timeout=1)

while 1:
	x=ser.readline()
	x = x.decode('ascii')
	if x == '':
		continue
	x = x.strip('\r\n')
	
	try:
		eq = x.find('=')
		num = int(x[eq+1:])
	except:
		continue
	#print(num)
	
	requests.get('http://127.0.0.1/send?heart={}&ecg={}'.format(98, num))
	
