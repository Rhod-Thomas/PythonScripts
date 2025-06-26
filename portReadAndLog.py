import serial as ser
import sys

##TODO
#1) take command line arguments for Serial port DONE
#2) decode incoming HexString data. 
#3) write data to database. 

#TODO
#way, way down the line.
#two-way comms for small commands. 
#maybe ask for channel map. 
#Also tell to do 'events'. 

handle = ser.Serial()
portName = "/dev/ttyACM0"

try:

    if len(sys.argv) > 1 :
        portName = sys.argv[1]
        handle.port = portName

    port.open()

except:
    print("serial port error")
    input("press any key to exit")
    exit()

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

