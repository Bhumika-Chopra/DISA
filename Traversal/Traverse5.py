import pickle
from Lab5 import seat
import os

seats = []

with open("Lab5", 'rb') as f:
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
    while(i<5 and (not found)):
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
                print(500 + seats[x].seatno)
                seats[x].occupancy = 1
                #send command to printer
            found = True
        if(i%5 == 0):
            sum,c = 0,0
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
                print(500 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum,c = 0,0
    while(i<16 and (not found)):
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
                print(500 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum = 0
    c = 0
    while(i<22 and (not found)):
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
                print(500 + seats[x].seatno)
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
                print(500 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum = 0
    c = 0
    while(i<34 and (not found)):
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
                print(500 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum = 0
    c = 0
    while(i<46 and (not found)):
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
                print(500 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum = 0
    c = 0
    while(i<58 and (not found)):
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
                print(500 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum = 0
    c = 0
    while(i<62 and (not found)):
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
                print(500 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum = 0
    c = 0
    while(i<66 and (not found)):
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
                print(500 + seats[x].seatno)
                seats[x].occupancy = 1
                # send command to printer
            found = True
    sum = 0
    c = 0
    if(seats[i].occupancy == 0 and (not found)):
        if(n==1):
            print(500 + seats[i].seatno)
            seats[i].occupancy = 1
            found = True
            # send command to printer
def change():
    with open("lab", 'wb') as file:
        for x in range(len(seats)):
            pickle.dump(seats[x],file)
    os.remove("Lab5")
    os.rename("lab", "Lab5")

found = False
m = int(input("m?"))
allocate(m)
change()