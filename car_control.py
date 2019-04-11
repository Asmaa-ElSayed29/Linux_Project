import os
import time
import curses


def GPIOInit():
        #GPIO 4: IN3 init
        os.system("echo \"4\" > /sys/class/gpio/export")
        os.system("echo \"out\" > /sys/class/gpio/gpio4/direction")
        os.system("echo \"0\" > /sys/class/gpio/gpio4/value")

        #GPIO 17: IN1 init
        os.system("echo \"17\" > /sys/class/gpio/export")
        os.system("echo \"out\" > /sys/class/gpio/gpio17/direction")
        os.system("echo \"0\" >/sys/class/gpio/gpio17/value")

        #GPIO 27: IN2 init
        os.system("echo \"27\" > /sys/class/gpio/export")
        os.system("echo \"out\" > /sys/class/gpio/gpio27/direction")
        os.system("echo \"0\" > /sys/class/gpio/gpio27/value")

        #GPIO 22: IN4 init
        os.system("echo \"22\" > /sys/class/gpio/export")
        os.system("echo \"out\" > /sys/class/gpio/gpio22/direction")
        os.system("echo \"0\" >/sys/class/gpio/gpio22/value")

        #GPIO 20: TRIGGER init
        os.system("echo \"20\" > /sys/class/gpio/export")
        os.system("echo \"out\" > /sys/class/gpio/gpio20/direction")
        os.system("echo \"0\" > /sys/class/gpio/gpio20/value ")

        #GPIO 21: ECHO init
        os.system("echo \"21\" > /sys/class/gpio/export")
        os.system("echo \"in\" > /sys/class/gpio/gpio21/direction")

def forward(delay):
        os.system("echo \"1\" > /sys/class/gpio/gpio27/value")
        os.system("echo \"1\" > /sys/class/gpio/gpio22/value")
        time.sleep(delay)
        os.system("echo \"0\" > /sys/class/gpio/gpio27/value")
        os.system("echo \"0\" > /sys/class/gpio/gpio22/value")

def backward(delay):
        os.system("echo \"1\" > /sys/class/gpio/gpio4/value")
        os.system("echo \"1\" > /sys/class/gpio/gpio17/value")
        time.sleep(delay)
        os.system("echo \"0\" > /sys/class/gpio/gpio4/value")
        os.system("echo \"0\" > /sys/class/gpio/gpio17/value")

def right(delay):
        os.system("echo \"1\" >/sys/class/gpio/gpio22/value")
        time.sleep(delay)
        os.system("echo \"0\" >/sys/class/gpio/gpio22/value")
def left(delay):                                             
        os.system("echo \"1\" > /sys/class/gpio/gpio27/value")
        time.sleep(delay)                                     
        os.system("echo \"0\" > /sys/class/gpio/gpio27/value")
                                                              
def ultrasonic_read():                                        
        initial_Time=0                                        
        end_Time=0                                           
        distance=0                                           
                                                                                                       
        os.system("echo \"1\" > /sys/class/gpio/gpio20/value ")
        time.sleep(0.000001)                                   
        os.system("echo \"0\" > /sys/class/gpio/gpio20/value ")
                                                               
        initial_Time= time.time()                              
        while int(open("/sys/class/gpio/gpio21/value","r").read().strip()) == 1:
                end_Time= time.time()                                           
                                                                                
        distance +=((end_Time-initial_Time) * 17150 )                           
                               
        distance=distance/10                         
        print "distance: ",distance                                                                  
                                                               
screen = curses.initscr()                                      
curses.noecho()                                                
curses.cbreak()                                                                 
screen.keypad(True)                                                             
GPIOInit()                                                                      
myDelay=0.005                                        
                                                     
try:                                                 
        while True:                
                char = screen.getch()
                if char == ord('q'): 
                        break        
                elif char == curses.KEY_UP:
                        forward(myDelay)   
                elif char == curses.KEY_DOWN:
                        backward(myDelay)    
                elif char == curses.KEY_RIGHT:
                        right(myDelay)        
                elif char == curses.KEY_LEFT: 
                        left(myDelay)         
                elif char == 10:             
                        print "stop"         
                ultrasonic_read()    
finally:                                   
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()                                   
                            

