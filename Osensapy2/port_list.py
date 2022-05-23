import sys
import glob
import serial

def serial_get_portlist():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
        ports += glob.glob('/dev/serial[0-9]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    portlist = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            portlist.append(port)
            print(port)
        except (OSError, serial.SerialException):
            pass
    return portlist