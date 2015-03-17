#!/usr/bin/python

import serial, time
import io

#initialization and open the port

#possible timeout values:

#    1. None: wait forever, block call
#    2. 0: non-blocking mode, return immediately
#    3. x, x is bigger than 0, float allowed, timeout block call

ser = serial.Serial()

#ser.port = "/dev/ttyUSB0"

ser.port = "/dev/ttyACM0"

#ser.port = "/dev/ttyS2"

ser.baudrate = 9600

ser.bytesize = serial.EIGHTBITS #number of bits per bytes

ser.parity = serial.PARITY_NONE #set parity check: no parity

ser.stopbits = serial.STOPBITS_ONE #number of stop bits

#ser.timeout = None          #block read
ser.timeout = 1            #non-block read
#ser.timeout = 2              #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write

numb="+919910236826"
cmnd='''AT+CMGS="'''
full=cmnd+numb+'''"'''
msg = "Text message"

try: 
	ser.open()
	sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

except Exception, e:
	print "error open serial port: " + str(e)
	exit()

if ser.isOpen():
	try:
		ser.flushInput() #flush input buffer, discarding all its contents
		ser.flushOutput()#flush output buffer, aborting current output 
		#and discard all that is in buffer
		#write data
		#ser.write("ATD +919910236826")
		#ser.write("ATI2")		
		#ser.write("AT+CMGF=1")
		#ser.write("\r\n")
		#ser.flush()
		#ser.write('''AT+CMGS="+919910236826"''')
		ser.write(full)		
		ser.write("\r")
		#sio.write(unicode("\r"))		
		#ser.write("This is my test message from PySerial API ")
		#ser.write(unicode(msg))		
		#sio.write(unicode("Text message from me\n"))
		#time.sleep(0.5)
		sio.write(unicode("Some text to send"))	
		#sio.write(unicode("\r"))		
		time.sleep(2.5)		
		#sio.write(unicode("\032"))		
		#sio.write(unicode("\r"))		
		#sio.write(unicode("\r\n"))		
		ser.write("\032")
		#ser.write("\r")
		sio.write(unicode("\r"))		
		ser.write("\r\n")
		ser.flush()
		#sio.flush()
		print("write data: Sending SMS")
		#ser.flush()		
		time.sleep(3)  #give the serial port sometime to receive the data
		numOfLines = 0
		#ser.sendBreak(0.5)
		while True:
			response = sio.readline()
			print("read data: " + response)
			numOfLines = numOfLines + 1
			if (numOfLines >= 8):
				break
		ser.close()

	except Exception, e1:
		print "error communicating...: " + str(e1)
	else:
		print "cannot open serial port "
