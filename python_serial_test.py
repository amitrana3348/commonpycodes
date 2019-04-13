import serial
#ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser = serial.Serial('COM6', 9600, timeout=5)
while True:
    ser.flushInput()
    reading = ser.readline()
    my = reading.split(',')
    c1 = float(my[1])
    c2 = float(my[2])
    c3 = float(my[3])
    print "Current sensor 1 = ",c1
    print "Current sensor 2 = ",c2
    print "Current sensor 3 = ",c3
