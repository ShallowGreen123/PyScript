import serial

ser1 = serial.Serial("COM40", 115200)

ser1.write("tttt".encode('utf-8'))
