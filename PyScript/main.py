import serial
import serial_proto as proto

COM = "COM40"


ser1 = serial.Serial(COM, 115200)
ser1.write("1424".encode('utf-8'))

