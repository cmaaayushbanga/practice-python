# import time
# timestamp= time.strftime("%H:%M:%S")
# print(timestamp)
# timestamp=time.strftime("%H")
# print(timestamp)
# timestamp=time.strftime("%M")
# print(timestamp)
# timestamp=time.strftime("%S")
# print(timestamp)

import time
# t = time.strftime("%H","%M","%S")
hour= int(time.strftime("%H"))
hour= int(input("Enter Hours:"))

if(hour>=0 and hour<12):
    print("Good Morning Sir!")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir!")
if(hour>=17 and hour<0):
    print("Good Night Sir!")