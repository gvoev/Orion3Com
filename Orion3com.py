import serial
import time



#ser = serial.Serial('COM3', 9600, timeout = 1)
ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout = 1
    )

delay = 1

def go(*pargs):
    print(ser.readall().decode('utf-8'))
    for arg in pargs:
        ser.write(arg)
    time.sleep(delay)

def setBR(PAM,baserate,channel):
    go(b'\n')
    go(b'3\n')
    go(b'pam ', bytes(str(PAM), encoding = 'utf-8'), b' ', bytes(str(channel), encoding = 'utf-8'), b'\n')
    go(b'baserate ', bytes(str(baserate), encoding = 'utf-8'), b' ', bytes(str(channel), encoding = 'utf-8'), b'\n')
    go(b'm\n')
    go(b'2\n')
    go(b'apply\n')
    go(b'm\n')
    
print(ser.read_until('Exit',200).decode('utf-8'))
ser.write(b'\n')
print(ser.readall().decode('utf-8'))
setBR(32,88,1)

ser.close()
