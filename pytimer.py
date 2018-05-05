# Import modules
import time


# Define variables
min = 60


timer = int(input('How long should the timer be set for (in minutes)? ')) * 60
while(timer > 0):
    print(timer, 'seconds remaining.')
    timer -= 1
    time.sleep(1)
print('Timer finished.')
