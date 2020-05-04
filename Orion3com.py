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





def go(a):
    print(ser.readall().decode('utf-8'))
    ser.write(a)
    time.sleep(delay)

def setBR(PAM,baserate,channel):
    go(b'\n')
    go(b'3\n')
    go(b'pam ')
    go(bytes(str(PAM), encoding = 'utf-8'))
    go(b' ')
    go(bytes(str(channel), encoding = 'utf-8'))
    go(b'\n')
    go(b'baserate ')
    go(bytes(str(baserate), encoding = 'utf-8'))
    go(b' ')
    go(bytes(str(channel), encoding = 'utf-8'))
    go(b'\n')
    go(b'm\n')
    
print(ser.read_until('Exit',200).decode('utf-8'))
ser.write(b'\n')
print(ser.readall().decode('utf-8'))
#setBR(32,88,1)

ser.close()





musor = '''
go(b'm\n')
go(b'3\n')
go(b'1\n')
go(b'1\n')
go(b'1\n')
go(b'off')
go(b'\n')
go(b'2\n')
go(b'239.239.123.123\n')
go(b'3\n')
go(b'1234\n')
go(b'm\n')
go(b'm\n')
go(b'm\n')
go(b'm\n')
time.sleep(1)
text = ser.readall().decode('utf-8')
print(text)
ser.close()



ser.write(b'm\n')
time.sleep(delay)
print(ser.readall().decode('utf-8'))
ser.cancel_read()
ser.write(b'm\n')
time.sleep(delay)
print(ser.readall().decode('utf-8'))
ser.write(b'\n')
time.sleep(delay)
print(ser.readall().decode('utf-8'))
ser.write(b'3\n')
time.sleep(delay)
print(ser.readall().decode('utf-8'))
ser.write(b'1\n')
time.sleep(delay)
print(ser.readall().decode('utf-8'))
ser.write(b'1\n')
time.sleep(delay)
print(ser.readall().decode('utf-8'))
ser.write(b'1\n')
time.sleep(delay)
print(ser.readall().decode('utf-8'))
ser.write(b'off')
time.sleep(delay)
print(ser.readall().decode('utf-8'))
ser.write(b'\n')
time.sleep(delay)
print(ser.readall().decode('utf-8'))
ser.write(b'm\n')
print(ser.readall().decode('utf-8'))
ser.write(b'm\n')
time.sleep(delay)
print(ser.readall().decode('utf-8'))
ser.cancel_read()
ser.write(b'm\n')
time.sleep(delay)
ser.close()



z = ser.readlines(100@q)
ser.write(b'\n')
ser.seek(b'Fault')
z = ser.readlines(10)
time.sleep(0.2)
ser.write(b'3')
a = ser.readlines(10)
time.sleep(0.2)
ser.write(b'1')
time.sleep(0.2)
b = ser.readlines(10)
time.sleep(0.2)
ser.close()
print(a, '//n', b , '//n', z)
'''
