import os                                                                                                                                                                                                   
import time                                                                                                                                                                                                 
import curses                                                                                                                                                                                               
                                                                                                                                                                           
                                                                                                                                                                                                                                                                                                                                                                                                                        
def GPIOInit():                                                                                                                                                                                  
        os.system("echo \"4\" > /sys/class/gpio/export")                                                                                                                                                    
        os.system("echo \"out\" > /sys/class/gpio/gpioIN3/direction")                                                                                                                                         
        os.system("echo \"0\" > /sys/class/gpio/gpioIN3/value")                                                                                                                                               
        os.system("echo \"17\" > /sys/class/gpio/export")                                                                                                                                                   
        os.system("echo \"out\" > /sys/class/gpio/gpio17/direction")                                                                                                                                        
        os.system("echo \"0\" >/sys/class/gpio/gpio17/value")                                                                                                                                               
        os.system("echo \"27\" > /sys/class/gpio/export")                                                                                                                                                   
        os.system("echo \"out\" > /sys/class/gpio/gpio27/direction")                                                                                                                                        
        os.system("echo \"0\" > /sys/class/gpio/gpio27/value")                                                                                                                                              
        os.system("echo \"22\" > /sys/class/gpio/export")                                                                                                                                                   
        os.system("echo \"out\" > /sys/class/gpio/gpio22/direction")                                                                                                                                        
        os.system("echo \"0\" >/sys/class/gpio/gpio22/value")                                                                                                                                               
                                                                                                                                                                                                            
def forward(delay):                                                                                                                                                                                       
        os.system("echo \"1\" > /sys/class/gpio/gpio27/value")                                                                                                                                              
        os.system("echo \"1\" > /sys/class/gpio/gpio22/value")                                                                                                                                              
        time.sleep(delay)                                                                                                                                                                                   
        os.system("echo \"0\" > /sys/class/gpio/gpio27/value")                                                                                                                                              
        os.system("echo \"0\" > /sys/class/gpio/gpio22/value")                                                                                                                                              
                                                                                                                                                                                                            
def backward(delay):                                                                                                                                                                                      
        os.system("echo \"1\" > /sys/class/gpio/gpio4/value")                                                                                                                                               
        os.system("echo \"1\" >/sys/class/gpio/gpio17/value")                                                                                                                                               
        time.sleep(delay)                                                                                                                                                                                   
        os.system("echo \"0\" > /sys/class/gpio/gpio4/value")                                                                                                                                               
        os.system("echo \"0\" >/sys/class/gpio/gpio17/value")                                                                                                                                               
                                                                                                                                                                                                            
                                                                                                                                                                                                            
def right(delay):                                                                                                                                                                                     
        os.system("echo \"1\" >/sys/class/gpio/gpio22/value")                                                                                                                                               
        time.sleep(delay)                                                                                                                                                                                   
        os.system("echo \"0\" >/sys/class/gpio/gpio22/value")                                                                                                                                               
                                                                                                                                                                                                            
def left(delay):                                                                                                                                                                                      
        os.system("echo \"1\" > /sys/class/gpio/gpio27/value")                                                                                                                                              
        time.sleep(delay)                                                                                                                                                                                   
        os.system("echo \"0\" > /sys/class/gpio/gpio27/value")       

                                                                                                                         
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
                                                                                                                                                                                                            
finally:                                                                                                                                                   
    curses.nocbreak(); screen.keypad(0);curses.echo()                                                                                                                                                      
    curses.endwin()

