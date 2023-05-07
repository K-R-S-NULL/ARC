import serial

ser = serial.Serial('/dev/tty1',9600)

while True:
	input = ser.read()
	print(input.decode("utf-8"))
