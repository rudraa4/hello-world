import time 
time_hour = time.strftime('%H')
time_minute = time.strftime('%M')
time_second = time.strftime('%S')
name = input("Enter your name: " )
if (4<=int(time_hour)<=11):
    print("Good morning", name)
elif(12<=int(time_hour)<=16):
    print("Good afternoon", name)
elif(17<=int(time_hour)<=21):
    print("Good evening", name)
else:
    print("you should sleep now", name,"its too late!")
    