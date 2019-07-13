import pickle
from Linux import seat
import os

seats = []

with open("linux", 'rb') as f:
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
    while(i<10 and (not found)):
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
                print(600 + seats[x].seatno)
                seats[x].occupancy = 1
                #send command to printer
            found = True
    sum,c = 0,0
    while(i<20 and (not found)):
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
                print(600 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum,c = 0,0
    while(i<24 and (not found)):
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
                print(600 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum = 0
    c = 0
    while(i<26 and (not found)):
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
                print(600 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum = 0
    c = 0
    while(i<28 and (not found)):
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
                print(600 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
def change():
    with open("lab", 'wb') as file:
        for x in range(len(seats)):
            pickle.dump(seats[x],file)
    os.remove("linux")
    os.rename("lab", "linux")

found = False
m = int(input("m?"))
allocate(m)
change()