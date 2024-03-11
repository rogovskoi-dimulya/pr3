Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import serial
>>> import time
>>> 
KeyboardInterrupt
>>> import serial.tools.list_ports
>>> speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']
>>> ports = [p.device for p in serial.tools.list_ports.comports()]
>>> port_name = ports[0]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    port_name = ports[0]
IndexError: list index out of range
>>> 