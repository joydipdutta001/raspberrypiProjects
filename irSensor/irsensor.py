import RPi.GPIO as io
import time

io.setwarnings(False)
io.setmode(io.BCM)
io.setup(14,io.IN)

while 1:
     if(io.input(14)==True):
         print("Detected")
         time.sleep(2)
     if(io.input(14)==False):
         print("Nothing Detected")
         time.sleep(2)
     