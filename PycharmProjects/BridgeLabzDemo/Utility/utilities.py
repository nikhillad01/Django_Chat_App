from macpath import norm_error
import random
def inputs():
    a=int(input("Enter num"))
    b = int(input("Enter num"))





def replaceStr(uname):
    str=("Hello <<UserName>>, How are you?") # String to replace username with

    if len(uname) < 3 :
        print("Username should be more than 3 chars")#name length should be more than 3
    else:
        modified_str=str.replace("<<UserName>>",uname)#new Modified String
        print(modified_str)


#******************************  FlipCoin  ******************************


def flipCoin(no_flips):
    head=0
    tail=0
    for i in range(no_flips):
        coin=random.uniform(0,1)         #random function  to generate values between 0 - 1 randomly
        if coin>=0.5:
            head+=1                      # increasing  heads count if 1 occurs
        else:
            tail+=1
    print("Total Heads ",head,"total head percentage ",(head/no_flips)*100)
    print("total tails", tail,"Total Tail percentage ",(tail/no_flips)*100)


#******************************  Leap Year  ******************************

def leapYear(year):
    if (year%4 ==0)or(year%4==0)and(year%100!=0):   # Condition to check leap year
        print("Year is leap year")
    else:
        print("Year is not leap")

#******************************  Power of Two  ******************************

def powerOfTwo(n):
    if n<=31:
        for i in range(1,n+1):              # range to find the power from 1 to "n"
            print(i, "Power of two is ", 2**i)
    else:
        print("Out of bound")


#******************************  Harmonic Number  ******************************

def harmonic(nthHarmonic):
    h=0
    for i in range(1,nthHarmonic+1):
        h+=1/i
    print("Harmonic Number ",h)

#******************************  Prime Factors  ******************************

 # Prime number is the number which is  only divisible by 1 and itself so prime-
 # factors would be the factors of that number which are prime number too.

def primefactors(num):
    for i in range(2,num):
        while (num % i == 0):
            print(i)
            num=num/i



#******************************  Gambler  ******************************

def gambler(stake,goal,no):
    wins=0
    loose=0
    #cash=stake
    bets=0
    gamble=0

    for i in range(0,no):
        cash = stake
        #print(" hh",gamble)
        while(cash>0 and cash<goal):
            bets += 1
            gamble = random.uniform(0,1)
            #print(gamble)
            #gamble = random.uniform(0, 1)
            if gamble<0.5:
                cash+=1

            else:
                cash-=1

        if (cash == goal):
            wins+=1
        else:
            loose+=1

    #print(bets)
    print("Wins ",wins ,"in turns ", no)
    print("Total wins ",wins," Winning percentage ",(wins/no)*100)
    print("Avg bets",bets/no)





#******************************  Coupoun  ******************************

def coupoun(coupounNumber):
    count=0
    l=[int(i) for i in str(coupounNumber)]
    print(l)
    while(len(l)>0):                        #Loop will run till list becomes empty
        randomnum=random.randint(0,9)       #generates random numbers
        count += 1
        if randomnum in l:
            l.remove(randomnum)             # if number is found in list then remove number
            print(l)

    print("Total random numbers to generate coupoun ",count)



#******************************  2D Array  ******************************
import  numpy as np

def twodarray(r,c):

    twolist=[[0 for col in range(c)]for row in range(r)]

            #using MultiList concept it will prints '0' in specified number of columns and rows.
            #if total columns are 3 and total rows are 3... then we will have  a multilist like below.
            #[[0,0,0],[0,0,0],[0,0,0]]
            # List comprehension: [ [ output_expression() for(set of columns to iterate) ]for(set of rows to iterate)]

    for row in range(r):
             for col in range(c):
                 twolist[row][col]=input("Enter ele")

    print(twolist)                     #prints data in multi List
    a=np.array(twolist)                # Converting multilist to numpy array
    print(a)



#****************************** Distince Triples  ******************************

def distinctTriples(l):
    lengthoglist=len(l)
    # we want triplets so the first for loop will start from 0 and end to length -2
    # because elements after length - 2 would be j and k.
    for i in range(0,lengthoglist-2):
        for j in range(1,lengthoglist-1):
            for k in range(2,lengthoglist):
                if l[i]+l[j]+l[k]==0:
                    print(l[i],l[j],l[k])


#****************************** Euclidean distance ******************************

import math                         #library for mathematical functions
def euclidien(x,y):
    edistance=math.sqrt(x*x+y*y)    #calculating square root using Maths square root and  euclidean formula
    print("Euclidean distance :",edistance)


#****************************** Stop Watch ******************************

import  time                        #importing time to measure current time
def stopwatch(start ):

    if start==1:

        start=time.time()
        print("Enter 2 to stop")
        b=int(input("Press 2 to stop"))
        if b==2:

            endtime=time.time()

            timeelapsed=endtime-start


            print("Time Elapsed : ",timeelapsed) # 1 second = 1000000000 nano second

#********************************Quadratic*******************************


def quadratic(a,b,c):
    delta=b*b - 4 * a* c
    #(-b+math.sqrt(delta))/(2*a)
    #(-b-math.sqrt(delta))/(2 * a)
    root1ofX=(-b+math.sqrt(delta))/(2*a)
    root2ofX=(-b-math.sqrt(delta))/(2*a)

    print("Root 1 of X : ",root1ofX)
    print("Root 2 of X : ",root2ofX)

#********************************Wind Chill*******************************


def windChill(temperature,windspeed):
    if ((temperature<50) and (windspeed<120 and windspeed>3)):
        w=35.74+0.6215*temperature+(0.4275*temperature-35.75)*windspeed**0.16

        print("Wind Chill : ",w)
    else:
        print("Temperature should be less than 50 and wind speed should be greater than 3 and less than 120")

timeDict={}
#*********************** Bubble sort ****************************

def bubble_sort(l):
    StartTime()
    for i in range(0,len(l)):
        for j in range(0,len(l)-i-1):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    StopTime()
    Elapsedtime()


    print(l)

#*********************************Anagrams******************************

def anagrams(str1,str2):
    l1=list(str1)
    l2=list(str2)

    sortedl1=bubble_sort(l1)    #passing the lists to bubble sort method
    sortedl2=bubble_sort(l2)
    print(l1,"      ",l2)
    if l1==l2:
        print("Anagrams")
    else:
        print("not anagrams ")
#************************* Palindrome ********************
def palindrome(l):
    palind=[]
    for i in l:
        temp=i
        rev=0
        while(i>0):
            dig=i%10
            rev=rev*10+dig
            i=i//10
        if(temp==rev):
            #print("The number is a palindrome!")
            palind.append(rev)
    print("prime  numbers which are Palindromes  and Anagrams: ",palind)



#*********************************Prime Numbers in range******************************
def primeNumbers(n1,n2):
    l=[]
    for i in range(n1,n2+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                #print(i)
                l.append(i)
    print("Prime Numbers ",l)
    palindrome(l)
    #print("palindromes ",l2)



#********************Binary Search ******************************
def binary_search(l,x):
    #sorted_list=bubble_sort(l)
    #print(sorted_list)
    #StartTime()
    StartTime()
    l.sort()
    print("sorted list ",l)
    upper=len(l)
    low=0
    for i in range(low,upper):
        mid=low+upper//2
        if x==l[mid]:
            print("element found at : ",mid)
            break
        else:
            if l[mid]< x:
                low=mid
            else:
                upper=mid
    StopTime()
    Elapsedtime()

#****************************Insertion Sort**********************************
def insertion_sort(l):
    StartTime()
    for i in range(1,len(l)):
        for j in range(i-1,-1,-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
            else:
                break
    print("Insertion Sort : ",l)
    StopTime()
    Elapsedtime()



#**********************Time Elapsed function *************************
start_timer=0
stop_timer=0
elapsed=0
def StartTime():
    StartTime.start_timer= time.time()
    print("Start Time is ",start_timer)


def StopTime():
    StopTime.stop_timer = time.time()
    print("Stop Time is",stop_timer)

def Elapsedtime():
   # print(Start1.start_timer)
   # print(Stop1.stop_timer)
    elapsed=StopTime.stop_timer-StartTime.start_timer
    #print("Elapsed Timer is", elapsed)
    elapsedSeconds=elapsed/1000
    print("Elapsed Time in seconds Seconds", elapsedSeconds, "sec")
    timeDict.update({1:elapsedSeconds})
#*********************************************************************