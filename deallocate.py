import pickle
import Lab1
import Lab2
import Lab3
import Lab5
import Linux

arr = []

def deallocate(n):


    if(n==1):
        with open("Lab1", 'wb+') as f:
            while (True):
                try:
                    s = pickle.load(f)
                    if(s.seatno == )
                except EOFError:
                    break



def main(str):
    #break into 3 digit numbers with '/' or '-' or ' '
    i=0
    num = 0
    global arr
    while(i<len(str)):
        f = 100
        for x in range(i,i+3):
            num = num + str[i]*f
            f = f/10
        arr.append(num)
        i += 4                                   #if no separator is present i += 3
    i=0
    while(i<len(arr)):
        d = arr[i]//100
        if(d==1):
            deallocate(1)
        elif(d==2):
            deallocate(2)
        elif(d==3):
            deallocate(3)
        elif(d==5):
            deallocate(5)
        else:
            deallocate(6)



