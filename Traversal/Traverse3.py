import pickle
from Lab3 import seat
import os

seats = []

with open("Lab3", 'rb') as f:
    while (True):
        try:
            s = pickle.load(f)
            seats.append(s)
        except EOFError:
            break

def allocate(n):
    global found
    global seats
    seats = []
    with open("Lab3", 'rb') as f:
        while (True):
            try:
                seats.append(pickle.load(f))
            except EOFError:
                break
    c,i = 0,0
    sum,c = 0,0
    while(i<4 and (not found)):
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
                print(300 + seats[x].seatno)
                seats[x].occupancy = 1
                #send command to printer
            found = True

    sum,c = 0,0
    while(i<12 and (not found)):
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
                print(300 + seats[x].seatno)
                seats[x].occupancy = 1
                #send command to printer
            found = True
    sum,c = 0,0
    while(i<37 and (not found)):
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
                print(300 + seats[x].seatno)
                seats[x].occupancy = 1
                #send command to printer
            found = True

def change():
    with open("lab", 'wb') as file:
        for x in range(len(seats)):
            pickle.dump(seats[x],file)
    os.remove("Lab3")
    os.rename("lab", "Lab3")

found = False
m = int(input("m?"))
allocate(m)
change()