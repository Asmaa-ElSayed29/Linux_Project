import time

os.system("echo \"4\" > /sys/class/gpio/export")
os.system("echo \"out\" > /sys/class/gpio/gpio4/direction")
os.system("echo \"0\" > /sys/class/gpio/gpio4/value ")

os.system("echo \"17\" > /sys/class/gpio/export")
os.system("echo \"in\" > /sys/class/gpio/gpio17/direction")

initial_Time=0
end_Time=0
distance=0
x=0
while x<10:

        os.system("echo \"1\" > /sys/class/gpio/gpio4/value ")
        time.sleep(0.000001)
        os.system("echo \"0\" > /sys/class/gpio/gpio4/value ")
        
        initial_Time= time.time()
        while int(open("/sys/class/gpio/gpio17/value","r").read().strip()) == 1:
                end_Time= time.time()

        distance +=((end_Time-initial_Time) * 17150 )
        x+=1
distance=distance/10
#if distance > 2 and distance < 400:
print(distance)
