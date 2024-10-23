import pickle
from Lab1 import seat
import os

seats = []

with open("Lab1", 'rb') as f:
    while (True):
        try:
            s = pickle.load(f)
            seats.append(s)
        except EOFError:
            break

def allocate(n):
    global found
    global seats
    c = 0
    i = 0
    sum = 0
    while(i<25 and (not found)):
        sum1 = sum + seats[i].occupancy
        if(sum1 == sum):
            c += 1
        else:
            sum = sum1
            c=0
        i += 1
        if(c==n):
            ind = i-c
            for x in range (ind, ind+c):
                print(100 + seats[x].seatno)
                seats[x].occupancy = 1
                #send command to printer
            found = True
        if(i%5 == 0):
            sum,c = 0,0
    while(i<29 and (not found)):
        sum1 = sum + seats[i].occupancy
        if(sum1 == sum):
            c += 1
        else:
            sum = sum1
            c=0
        i += 1
        if(c==n):
            ind = i-c
            for x in range (ind, ind+c):
                print(100 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True

    sum,c = 0,0
    if(seats[i].occupancy == 0 and (not found)):
        if(n==1):
            print(100 + seats[i].seatno)
            seats[i].occupancy = 1
            found = True
            # send command to printer
def change():
    with open("lab", 'wb') as file:
        for x in range(len(seats)):
            pickle.dump(seats[x],file)
    os.remove("Lab1")
    os.rename("lab", "Lab1")

found = False
m = int(input("m?"))
allocate(m)
change()