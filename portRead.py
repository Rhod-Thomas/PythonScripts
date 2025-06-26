import serial as ser

handle = ser.Serial("/dev/ttyACM1")

line = ""

while(True):
   
    try:

        ch = handle.read().decode('utf-8')
        #print(ch)
        line += ch
        #print(line)

        if ch == '\n':
            line = line.replace('\n', '')
            print(line)
            line = ""

    except:

        print("exception handled.")

