import time

from machine import UART

uart1 = UART(1, baudrate=115200, tx=17, rx=18)
uart1.write('hello')  # write 5 bytes

for i in range(1, 10):
    uart1.write('hello\r\n')  # write 5 bytes
    
while True:
    if uart1.any():
        Len = uart1.any()
        arr = [0]*Len
        for i in range(Len):
            arr[i] = uart1.read(1);
        print(arr)
    
    