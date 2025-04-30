import serial as ser

handle = ser.Serial("/dev/ttyACM0")

line = ""

while(True):
    
    ch = handle.read().decode('utf-8')
    #print(ch)
    line += ch
    #print(line)

    if ch == '\n':
        line = line.replace('\n', '')
        print(line)
        line = ""

