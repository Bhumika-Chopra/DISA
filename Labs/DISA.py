import pickle
from Lab1 import seat
import Lab1
import Lab2
import Lab3
import Lab5
import Linux
import os

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DISA3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

Lab,Seat=0,0
seats = []
found = False
pcs = []
arr = []

class Ui_DISA3(object):


    def labState1(self):
        global seats
        global found
        global Lab
        Lab=1
        found = False
        seats = []
        print("Lab: ",Lab)

    def labState2(self):
        global Lab
        global seats
        global found
        Lab=2
        seats = []
        found = False
        print("Lab: ",Lab)

    def labState3(self):
        global Lab
        global seats
        global found
        Lab=3
        seats = []
        found = False
        print("Lab: ",Lab)

    def labState5(self):
        global Lab
        global seats
        global found
        found = False
        Lab=5
        seats = []
        print("Lab: ",Lab)

    def labStatelin(self):
        global Lab
        global seats
        global found
        found = False
        Lab=6
        seats = []
        print("Lab: ",Lab)


    def seat1(self):
        global Seat
        Seat=1
        print("Seat: ",Seat)

    def seat2(self):
        global Seat
        Seat=2
        print("Seat: ",Seat)

    def seat3(self):
        global Seat
        Seat=3
        print("Seat: ",Seat)

    def seat4(self):
        global Seat
        Seat=4
        print("Seat: ",Seat)


    def Book1(self):
        self.lineEdit_1.setText("0")
        print("1")

    def Book2(self):
        self.lineEdit_2.setText("0")
        print("2")

    def Book3(self):
        self.lineEdit_3.setText("0")
        print("3")

    def Book5(self):
        self.lineEdit_5.setText("0")
        print("4")

    def Book6(self):
        self.lineEdit_6.setText("0")
        print("5")


    def Unbook1(self):
        self.lineEdit_1.setText("30")
        print("1")

    def Unbook2(self):
        self.lineEdit_2.setText("30")
        print("2")

    def Unbook3(self):
        self.lineEdit_3.setText("38")
        print("3")

    def Unbook5(self):
        self.lineEdit_5.setText("67")
        print("4")

    def Unbook6(self):
        self.lineEdit_6.setText("24")
        print("5")




    def EntAllocate(self):
        global Lab
        global Seat
        if(Lab == 1 and Seat != 0):
            with open("Lab1", 'rb') as f:
                while(True):
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
                with open("Lab1", 'wb') as file:
                    for x in range(len(seats)):
                        pickle.dump(seats[x], file)

            allocate(Seat)
            change()

        elif(Lab == 2 and seat!= 0):
            with open("Lab2", 'rb') as f:
                while (True):
                    try:
                        s = pickle.load(f)
                        seats.append(s)
                    except EOFError:
                        break

            def allocate(n):
                global found
                global seats
                c,i = 0,0
                sum = 0
                while(i<25 and (not found)):
                    sum1 = sum + seats[i].occupancy
                    if(sum1 == sum):
                        c += 1
                    else:
                        sum = sum1
                        c = 0
                    i += 1
                    if(c==n):
                        ind = i-c
                        for x in range (ind, ind+c):
                            print(200 + seats[x].seatno)
                            seats[x].occupancy = 1
                            #send command to printer
                        found = True
                    if(i%5 == 0):
                        sum,c = 0,0
                while(i<27 and (not found)):
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
                            print(200 + seats[x].seatno)
                            seats[x].occupancy = 1
                            #send command to printer
                        found = True
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
                            print(200 + seats[x].seatno)
                            seats[x].occupancy = 1
                            #send command to printer
                        found = True

                if(seats[i].occupancy == 0 and (not found)):
                    if(n==1):
                        print(200 + seats[i].seatno)
                        seats[i].occupancy = 1
                        found = True
                        # send command to printer

            def change():
                with open("Lab2", 'wb') as file:
                    for x in range(len(seats)):
                        pickle.dump(seats[x],file)

            allocate(Seat)
            change()

        elif(Lab == 3 and Seat != 0):
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
                with open("Lab3", 'wb') as file:
                    for x in range(len(seats)):
                        pickle.dump(seats[x],file)

            allocate(Seat)
            change()

        elif(Lab == 5 and Seat != 0):
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
                with open("Lab5", 'wb') as file:
                    for x in range(len(seats)):
                        pickle.dump(seats[x],file)

            allocate(Seat)
            change()

        elif(Lab == 6 and Seat != 0) :
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
                with open("linux", 'wb') as file:
                    for x in range(len(seats)):
                        pickle.dump(seats[x],file)

            allocate(Seat)
            change()

            #Change No. of seats in lineEdit_1 if Lab=1
            if((Lab==1) and (Seat==1) ):
                L1=self.lineEdit_1.text()
                L1_=int(L1,10)
                NewL1_=L1_-1
                NewL1=str(NewL1_)
                self.lineEdit_1.setText(NewL1)

            elif((Lab==1) and (Seat==2) and found):
                L1=self.lineEdit_1.text()
                L1_=int(L1,10)
                NewL1_=L1_-2
                NewL1=str(NewL1_)
                self.lineEdit_1.setText(NewL1)

            elif((Lab==1) and (Seat==3) and found):
                L1=self.lineEdit_1.text()
                L1_=int(L1,10)
                NewL1_=L1_-3
                NewL1=str(NewL1_)
                self.lineEdit_1.setText(NewL1)

            elif((Lab==1) and (Seat==4) and found):
                L1=self.lineEdit_1.text()
                L1_=int(L1,10)
                NewL1_=L1_-4
                NewL1=str(NewL1_)
                self.lineEdit_1.setText(NewL1)

            #Change No. of seats in lineEdit_2 if Lab=2
            elif((Lab==2) and (Seat==1) and found):
                L1=self.lineEdit_2.text()
                L1_=int(L1,10)
                NewL1_=L1_-1
                NewL1=str(NewL1_)
                self.lineEdit_2.setText(NewL1)

            elif((Lab==2) and (Seat==2) and found):
                L1=self.lineEdit_2.text()
                L1_=int(L1,10)
                NewL1_=L1_-2
                NewL1=str(NewL1_)
                self.lineEdit_2.setText(NewL1)

            elif((Lab==2) and (Seat==3) and found):
                L1=self.lineEdit_2.text()
                L1_=int(L1,10)
                NewL1_=L1_-3
                NewL1=str(NewL1_)
                self.lineEdit_2.setText(NewL1)

            elif((Lab==2) and (Seat==4) and found):
                L1=self.lineEdit_2.text()
                L1_=int(L1,10)
                NewL1_=L1_-4
                NewL1=str(NewL1_)
                self.lineEdit_2.setText(NewL1)

            #Change No. of seats in lineEdit_3 if Lab=3
            elif((Lab==3) and (Seat==1) and found):
                L1=self.lineEdit_3.text()
                L1_=int(L1,10)
                NewL1_=L1_-1
                NewL1=str(NewL1_)
                self.lineEdit_3.setText(NewL1)

            elif((Lab==3) and (Seat==2) and found):
                L1=self.lineEdit_3.text()
                L1_=int(L1,10)
                NewL1_=L1_-2
                NewL1=str(NewL1_)
                self.lineEdit_3.setText(NewL1)

            elif((Lab==3) and (Seat==3) and found):
                L1=self.lineEdit_3.text()
                L1_=int(L1,10)
                NewL1_=L1_-3
                NewL1=str(NewL1_)
                self.lineEdit_3.setText(NewL1)

            elif((Lab==3) and (Seat==4) and found):
                L1=self.lineEdit_3.text()
                L1_=int(L1,10)
                NewL1_=L1_-4
                NewL1=str(NewL1_)
                self.lineEdit_3.setText(NewL1)

            #Change No. of seats in lineEdit_5 if Lab=5
            elif((Lab==5) and (Seat==1) and found):
                L1=self.lineEdit_5.text()
                L1_=int(L1,10)
                NewL1_=L1_-1
                NewL1=str(NewL1_)
                self.lineEdit_5.setText(NewL1)

            elif((Lab==5) and (Seat==2) and found):
                L1=self.lineEdit_5.text()
                L1_=int(L1,10)
                NewL1_=L1_-2
                NewL1=str(NewL1_)
                self.lineEdit_5.setText(NewL1)

            elif((Lab==5) and (Seat==3) and found):
                L1=self.lineEdit_5.text()
                L1_=int(L1,10)
                NewL1_=L1_-3
                NewL1=str(NewL1_)
                self.lineEdit_5.setText(NewL1)

            elif((Lab==5) and (Seat==4) and found):
                L1=self.lineEdit_5.text()
                L1_=int(L1,10)
                NewL1_=L1_-4
                NewL1=str(NewL1_)
                self.lineEdit_5.setText(NewL1)

            #Change No. of seats in lineEdit_6 if Lab=6
            elif((Lab==6) and (Seat==1) and found):
                L1=self.lineEdit_6.text()
                L1_=int(L1,10)
                NewL1_=L1_-1
                NewL1=str(NewL1_)
                self.lineEdit_6.setText(NewL1)

            elif((Lab==6) and (Seat==2) and found):
                L1=self.lineEdit_6.text()
                L1_=int(L1,10)
                NewL1_=L1_-2
                NewL1=str(NewL1_)
                self.lineEdit_6.setText(NewL1)

            elif((Lab==6) and (Seat==3) and found):
                L1=self.lineEdit_6.text()
                L1_=int(L1,10)
                NewL1_=L1_-3
                NewL1=str(NewL1_)
                self.lineEdit_6.setText(NewL1)

            elif((Lab==6) and (Seat==4) and found):
                L1=self.lineEdit_6.text()
                L1_=int(L1,10)
                NewL1_=L1_-4
                NewL1=str(NewL1_)
                self.lineEdit_6.setText(NewL1)

            Lab = 0
            Seat = 0
        else:
            print("No selection")



    # def EntDeallocate(self):
    #     SeatName=self.lineEdit.text()
    #     #if value in linEdit != False, deallocate the seats mentioned in lineEdit
    #
    #     if(SeatName!=False):
    #         print(SeatName)
    #     else:
    #         print("No input")
    def EntDeallocate(self):
        SeatName=self.lineEdit.text()
        #if value in linEdit != False, deallocate the seats mentioned in lineEdit

        if(SeatName!=None):
            print(SeatName)

            def deallocate(n, arr, j):
                global pcs
                pcs = []
                if(n==1):
                    with open("Lab1", 'rb') as f:
                        while True:
                            try:
                                pcs.append(pickle.load(f))
                            except EOFError:
                                break
                    for y in range(len(pcs)):
                        if(pcs[y].seatno == arr[j]):
                            pcs[y].occupancy = 0
                    print("seat has been deallocated")

                elif(n==2):
                    with open("Lab2", 'rb') as f:
                        while True:
                            try:
                                pcs.append(pickle.load(f))
                            except EOFError:
                                break
                    for y in range(len(pcs)):
                        if(pcs[y].seatno == arr[j]):
                            pcs[y].occupancy = 0
                    print("seat has been deallocated")
                elif(n==3):
                    with open("Lab3", 'rb') as f:
                        while True:
                            try:
                                pcs.append(pickle.load(f))
                            except EOFError:
                                break
                    for y in range(len(pcs)):
                        if(pcs[y].seatno == arr[j]):
                            pcs[y].occupancy = 0
                    print("seat has been deallocated")
                elif(n==5):
                    with open("Lab5", 'rb') as f:
                        while True:
                            try:
                                pcs.append(pickle.load(f))
                            except EOFError:
                                break
                    for y in range(len(pcs)):
                        if(pcs[y].seatno == arr[j]):
                            pcs[y].occupancy = 0
                    print("seat has been deallocated")
                else:
                    with open("linux", 'rb') as f:
                        while True:
                            try:
                                pcs.append(pickle.load(f))
                            except EOFError:
                                break
                    for y in range(len(pcs)):
                        if(pcs[y].seatno == arr[j]):
                            pcs[y].occupancy = 0
                    print("seat has been deallocated")


            def change(n):
                global pcs
                if(n==1):
                    with open("Lab1", 'wb') as file:
                        for x in range(len(pcs)):
                            pickle.dump(pcs[x],file)
                elif(n==2):
                    with open("Lab2", 'wb') as file:
                        for x in range(len(pcs)):
                            pickle.dump(pcs[x],file)
                elif(n==3):
                    with open("Lab3", 'wb') as file:
                        for x in range(len(pcs)):
                            pickle.dump(pcs[x],file)
                elif(n==5):
                    with open("Lab5", 'wb') as file:
                        for x in range(len(pcs)):
                            pickle.dump(pcs[x],file)
                elif (n==6):
                    with open("linux", 'wb') as file:
                        for x in range(len(pcs)):
                            pickle.dump(pcs[x],file)

            def main(str):
                #break into 3 digit numbers with '/' or '-' or ' '
                i=0
                global arr
                arr = []
                while(i<len(str)):
                    f = 100
                    num = 0
                    for x in range(i, i+3):
                        int_str = int(str[x])
                        num = num + int_str*f
                        f = f//10
                    arr.append(num)
                    i = i + 4
                j=0
                while(j<len(arr)):
                    d = arr[j]//100
                    if(d==1):
                        arr[j] = arr[j] - 100
                        arr.sort()
                        deallocate(1, arr, j)
                        change(1)
                    elif(d==2):
                        arr[j] = arr[j] - 200
                        arr.sort()
                        deallocate(2,arr, j)
                        change(2)
                    elif(d==3):
                        arr[j] = arr[j] - 300
                        arr.sort()
                        deallocate(3,arr, j)
                        change(3)
                    elif(d==5):
                        arr[j] = arr[j] - 500
                        arr.sort()
                        deallocate(5,arr, j)
                        change(5)
                    elif(n==6):
                        arr[j] = arr[j] - 600
                        arr.sort()
                        deallocate(6,arr, j)
                        change(6)
                    j = j + 1

            main(SeatName)

            Array=list(SeatName)
            if(len(Array)==3):
                D1=Array[0:2]

                #Change No. of seats in lineEdit by 1
                if((Array[0]==1)):
                    L1=self.lineEdit_1.text()
                    L1_=int(L1,10)
                    NewL1_=L1_+1
                    NewL1=str(NewL1_)
                    self.lineEdit_1.setText(NewL1)
                elif((Array[0]==2)):
                    L1=self.lineEdit_2.text()
                    L1_=int(L1,10)
                    NewL1_=L1_+1
                    NewL1=str(NewL1_)
                    self.lineEdit_2.setText(NewL1)
                elif((Array[0]==3)):
                    L1=self.lineEdit_3.text()
                    L1_=int(L1,10)
                    NewL1_=L1_+1
                    NewL1=str(NewL1_)
                    self.lineEdit_3.setText(NewL1)
                elif((Array[0]==5)):
                    L1=self.lineEdit_5.text()
                    L1_=int(L1,10)
                    NewL1_=L1_+1
                    NewL1=str(NewL1_)
                    self.lineEdit_5.setText(NewL1)
                elif((Array[0]==6)):
                    L1=self.lineEdit_6.text()
                    L1_=int(L1,10)
                    NewL1_=L1_+1
                    NewL1=str(NewL1_)
                    self.lineEdit_6.setText(NewL1)


                elif(len(Array)==7):
                    D1=Array[0:2]
                    D2=Array[4:6]

                    #Change No. of seats in lineEdit by 2
                    if((Array[0]==1)):
                        L1=self.lineEdit_1.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_1.setText(NewL1)
                    elif((Array[0]==2)):
                        L1=self.lineEdit_2.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_2.setText(NewL1)
                    elif((Array[0]==3)):
                        L1=self.lineEdit_3.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_3.setText(NewL1)
                    elif((Array[0]==5)):
                        L1=self.lineEdit_5.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_5.setText(NewL1)
                    elif((Array[0]==6)):
                        L1=self.lineEdit_6.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_6.setText(NewL1)

                    if((Array[4]==1)):
                        L1=self.lineEdit_1.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_1.setText(NewL1)
                    elif((Array[4]==2)):
                        L1=self.lineEdit_2.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_2.setText(NewL1)
                    elif((Array[4]==3)):
                        L1=self.lineEdit_3.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_3.setText(NewL1)
                    elif((Array[4]==5)):
                        L1=self.lineEdit_5.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_5.setText(NewL1)
                    elif((Array[4]==6)):
                        L1=self.lineEdit_6.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_6.setText(NewL1)

                    if((Array[8]==1)):
                        L1=self.lineEdit_1.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_1.setText(NewL1)
                    elif((Array[8]==2)):
                        L1=self.lineEdit_2.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_2.setText(NewL1)
                    elif((Array[8]==3)):
                        L1=self.lineEdit_3.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_3.setText(NewL1)
                    elif((Array[8]==5)):
                        L1=self.lineEdit_5.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_5.setText(NewL1)
                    elif((Array[8]==6)):
                        L1=self.lineEdit_6.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_6.setText(NewL1)


                elif(len(Array)==11):
                    D1=Array[0:2]
                    D2=Array[4:6]
                    D3=Array[8:10]

                    #Change No. of seats in lineEdit by 3
                    if((Array[0]==1)):
                        L1=self.lineEdit_1.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_1.setText(NewL1)
                    elif((Array[0]==2)):
                        L1=self.lineEdit_2.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_2.setText(NewL1)
                    elif((Array[0]==3)):
                        L1=self.lineEdit_3.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_3.setText(NewL1)
                    elif((Array[0]==5)):
                        L1=self.lineEdit_4.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_4.setText(NewL1)
                    elif((Array[0]==6)):
                        L1=self.lineEdit_5.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_5.setText(NewL1)

                    if((Array[4]==1)):
                        L1=self.lineEdit_1.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_1.setText(NewL1)
                    elif((Array[4]==2)):
                        L1=self.lineEdit_2.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_2.setText(NewL1)
                    elif((Array[4]==3)):
                        L1=self.lineEdit_3.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_3.setText(NewL1)
                    elif((Array[4]==5)):
                        L1=self.lineEdit_4.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_4.setText(NewL1)
                    elif((Array[4]==6)):
                        L1=self.lineEdit_5.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_5.setText(NewL1)



                elif(len(Array)==15):
                    D1=Array[0:2]
                    D2=Array[4:6]
                    D3=Array[8:10]
                    D4=Array[12:14]

                    #Change No. of seats in lineEdit by 2
                    if((Array[0]==1)):
                        L1=self.lineEdit_1.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_1.setText(NewL1)
                    elif((Array[0]==2)):
                        L1=self.lineEdit_2.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_2.setText(NewL1)
                    elif((Array[0]==3)):
                        L1=self.lineEdit_3.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_3.setText(NewL1)
                    elif((Array[0]==5)):
                        L1=self.lineEdit_5.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_5.setText(NewL1)
                    elif((Array[0]==6)):
                        L1=self.lineEdit_6.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_6.setText(NewL1)

                    if((Array[4]==1)):
                        L1=self.lineEdit_1.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_1.setText(NewL1)
                    elif((Array[4]==2)):
                        L1=self.lineEdit_2.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_2.setText(NewL1)
                    elif((Array[4]==3)):
                        L1=self.lineEdit_3.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_3.setText(NewL1)
                    elif((Array[4]==5)):
                        L1=self.lineEdit_5.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_5.setText(NewL1)
                    elif((Array[4]==6)):
                        L1=self.lineEdit_6.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_6.setText(NewL1)

                    if((Array[8]==1)):
                        L1=self.lineEdit_1.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_1.setText(NewL1)
                    elif((Array[8]==2)):
                        L1=self.lineEdit_2.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_2.setText(NewL1)
                    elif((Array[8]==3)):
                        L1=self.lineEdit_3.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_3.setText(NewL1)
                    elif((Array[8]==5)):
                        L1=self.lineEdit_5.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_5.setText(NewL1)
                    elif((Array[8]==6)):
                        L1=self.lineEdit_6.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_6.setText(NewL1)

                    if((Array[12]==1)):
                        L1=self.lineEdit_1.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_1.setText(NewL1)
                    elif((Array[12]==2)):
                        L1=self.lineEdit_2.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_2.setText(NewL1)
                    elif((Array[12]==3)):
                        L1=self.lineEdit_3.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_3.setText(NewL1)
                    elif((Array[12]==5)):
                        L1=self.lineEdit_5.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_5.setText(NewL1)
                    elif((Array[12]==6)):
                        L1=self.lineEdit_6.text()
                        L1_=int(L1,10)
                        NewL1_=L1_+1
                        NewL1=str(NewL1_)
                        self.lineEdit_6.setText(NewL1)




    def setupUi(self, DISA3):
        DISA3.setObjectName("DISA3")
        DISA3.resize(529, 386)
        DISA3.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(DISA3)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(176, 255, 232);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 9, 4, 3, 5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 10, 9, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())

        self.lineEdit_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 7, 6, 1, 2)
        self.lineEdit_6.setText("24")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(60, 201, 81);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setAutoFillBackground(False)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 225, 236);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 225, 236);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 225, 236);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(255, 225, 236);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_2.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(230, 207, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_2.addWidget(self.pushButton_10)
        self.gridLayout.addLayout(self.horizontalLayout_2, 14, 1, 2, 7)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                        "background-color: rgb(157, 216, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 10, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 10, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())

        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_2.setText("30")

        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 10, 3, 2, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.pushButton_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.pushButton_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 170, 255);\n"
                                        "background-color: rgb(212, 231, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 1, 2, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(218, 75, 75);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)


        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(235, 215, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_3.addWidget(self.pushButton_11)
        self.gridLayout.addLayout(self.horizontalLayout_3, 17, 1, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 7, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridLayout.addItem(spacerItem4, 16, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(15)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("background-color: rgb(255, 153, 167);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 11, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.gridLayout.addItem(spacerItem5, 18, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())

        self.lineEdit_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_4.addWidget(self.lineEdit_5)
        self.lineEdit_5.setText("60")

        spacerItem6 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.gridLayout.addLayout(self.horizontalLayout_4, 7, 3, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText("30")

        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 3, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_1.sizePolicy().hasHeightForWidth())

        self.lineEdit_1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.horizontalLayout_5.addWidget(self.lineEdit_1)
        self.lineEdit_1.setText("30")

        spacerItem8 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.gridLayout.addLayout(self.horizontalLayout_5, 12, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.gridLayout.addItem(spacerItem9, 13, 1, 1, 1)
        DISA3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DISA3)
        self.statusbar.setObjectName("statusbar")
        DISA3.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(DISA3)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 529, 18))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")

        self.menuBook_Lab = QtWidgets.QMenu(self.menuFile)
        self.menuBook_Lab.setObjectName("menuBook_Lab")
        self.menuUnbook_Lab = QtWidgets.QMenu(self.menuFile)
        self.menuUnbook_Lab.setObjectName("menuUnbook_Lab")

        DISA3.setMenuBar(self.menuBar)

        self.actionReport_fail_systems = QtWidgets.QAction(DISA3)
        self.actionReport_fail_systems.setObjectName("actionReport_fail_systems")
        self.actionAllocate_repaired_systems = QtWidgets.QAction(DISA3)
        self.actionAllocate_repaired_systems.setObjectName("actionAllocate_repaired_systems")

        self.actionLab_10 = QtWidgets.QAction(DISA3)
        self.actionLab_10.setObjectName("actionLab_10")
        self.actionLab_2 = QtWidgets.QAction(DISA3)
        self.actionLab_2.setObjectName("actionLab_2")
        self.actionLab_3 = QtWidgets.QAction(DISA3)
        self.actionLab_3.setObjectName("actionLab_3")
        self.actionLab_5 = QtWidgets.QAction(DISA3)
        self.actionLab_5.setObjectName("actionLab_5")
        self.actionLab_1 = QtWidgets.QAction(DISA3)
        self.actionLab_1.setObjectName("actionLab_1")
        self.actionLab_4 = QtWidgets.QAction(DISA3)
        self.actionLab_4.setObjectName("actionLab_4")
        self.actionLab_6 = QtWidgets.QAction(DISA3)
        self.actionLab_6.setObjectName("actionLab_6")
        self.actionLab_7 = QtWidgets.QAction(DISA3)
        self.actionLab_7.setObjectName("actionLab_7")
        self.actionLab_8 = QtWidgets.QAction(DISA3)
        self.actionLab_8.setObjectName("actionLab_8")
        self.actionLab_9 = QtWidgets.QAction(DISA3)
        self.actionLab_9.setObjectName("actionLab_9")
        self.menuBook_Lab.addAction(self.actionLab_10)
        self.menuBook_Lab.addAction(self.actionLab_2)
        self.menuBook_Lab.addAction(self.actionLab_3)
        self.menuBook_Lab.addAction(self.actionLab_5)
        self.menuBook_Lab.addAction(self.actionLab_8)
        self.menuUnbook_Lab.addAction(self.actionLab_1)
        self.menuUnbook_Lab.addAction(self.actionLab_4)
        self.menuUnbook_Lab.addAction(self.actionLab_6)
        self.menuUnbook_Lab.addAction(self.actionLab_7)
        self.menuUnbook_Lab.addAction(self.actionLab_9)
        self.menuFile.addAction(self.actionReport_fail_systems)
        self.menuFile.addAction(self.actionAllocate_repaired_systems)
        self.menuFile.addAction(self.menuBook_Lab.menuAction())
        self.menuFile.addAction(self.menuUnbook_Lab.menuAction())
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(DISA3)
        QtCore.QMetaObject.connectSlotsByName(DISA3)

    def retranslateUi(self, DISA3):
        _translate = QtCore.QCoreApplication.translate
        DISA3.setWindowTitle(_translate("DISA3", "MainWindow"))

        self.pushButton_5.setText(_translate("DISA3", "LINUX"))
        self.pushButton_5.clicked.connect(self.labStatelin)

        self.label_6.setText(_translate("DISA3", "   No. of vacant seats"))
        self.label_7.setText(_translate("DISA3", "III. No. of vacant seats    "))
        self.label.setText(_translate("DISA3", " ALLOCATE "))

        self.pushButton_6.setText(_translate("DISA3", "1"))
        self.pushButton_6.clicked.connect(self.seat1)

        self.pushButton_7.setText(_translate("DISA3", "2"))
        self.pushButton_7.clicked.connect(self.seat2)

        self.pushButton_8.setText(_translate("DISA3", "3"))
        self.pushButton_8.clicked.connect(self.seat3)

        self.pushButton_9.setText(_translate("DISA3", "4"))
        self.pushButton_9.clicked.connect(self.seat4)

        self.pushButton_10.setText(_translate("DISA3", "ENTER"))
        self.pushButton_10.clicked.connect(self.EntAllocate)

        self.pushButton_2.setText(_translate("DISA3", "LAB II"))
        self.pushButton_2.clicked.connect(self.labState2)

        self.label_3.setText(_translate("DISA3", "  II. No. of vacant seats"))

        self.pushButton_4.setText(_translate("DISA3", "LAB V"))
        self.pushButton_4.clicked.connect(self.labState5)

        self.pushButton_3.setText(_translate("DISA3", "LAB III"))
        self.pushButton_3.clicked.connect(self.labState3)

        self.label_2.setText(_translate("DISA3", "    DEALLOCATE    "))

        self.pushButton_11.setText(_translate("DISA3", "ENTER"))
        self.pushButton_11.clicked.connect(self.EntDeallocate)

        self.pushButton_1.setText(_translate("DISA3", "LAB I"))
        self.pushButton_1.clicked.connect(self.labState1)

        self.label_4.setText(_translate("DISA3", "V. No. of vacant seats   "))
        self.label_5.setText(_translate("DISA3", "  I. No. of vacant seats"))
        self.menuFile.setTitle(_translate("DISA3", "File"))

        self.menuBook_Lab.setTitle(_translate("DISA3", "Book Lab"))
        self.menuUnbook_Lab.setTitle(_translate("DISA3", "Unbook Lab"))
        self.actionReport_fail_systems.setText(_translate("DISA3", "Report fail systems"))
        self.actionAllocate_repaired_systems.setText(_translate("DISA3", "Allocate repaired systems"))

        self.actionLab_10.setText(_translate("DISA3", "Lab 1"))
        self.actionLab_10.triggered.connect(self.Book1)

        self.actionLab_2.setText(_translate("DISA3", "Lab 2"))
        self.actionLab_2.triggered.connect(self.Book2)

        self.actionLab_3.setText(_translate("DISA3", "Lab 3"))
        self.actionLab_3.triggered.connect(self.Book3)

        self.actionLab_5.setText(_translate("DISA3", "Lab 5"))
        self.actionLab_5.triggered.connect(self.Book5)

        self.actionLab_1.setText(_translate("DISA3", "Lab 1"))
        self.actionLab_1.triggered.connect(self.Unbook1)

        self.actionLab_4.setText(_translate("DISA3", "Lab 2"))
        self.actionLab_4.triggered.connect(self.Unbook2)

        self.actionLab_6.setText(_translate("DISA3", "Lab 3"))
        self.actionLab_6.triggered.connect(self.Unbook3)

        self.actionLab_7.setText(_translate("DISA3", "Lab 5"))
        self.actionLab_7.triggered.connect(self.Unbook5)

        self.actionLab_8.setText(_translate("DISA3", "Lab 6"))
        self.actionLab_8.triggered.connect(self.Book6)

        self.actionLab_9.setText(_translate("DISA3", "Lab 6"))
        self.actionLab_9.triggered.connect(self.Unbook6)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DISA3 = QtWidgets.QMainWindow()
    ui = Ui_DISA3()
    ui.setupUi(DISA3)
    DISA3.show()
    sys.exit(app.exec_())



