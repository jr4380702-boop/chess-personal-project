import os
import time
import threading




def clear():
    if os.name == 'nt':
        _ = os.system('cls')
clear()
print("hi")
timer = threading.Timer(5,clear)
timer.start()
for i in range(10):
    time.sleep(1)
    print("hi")
