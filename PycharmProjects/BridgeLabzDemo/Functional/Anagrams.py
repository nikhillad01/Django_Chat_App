from  Utility import  utilities

try:
    a=input("Enter str1")
    b=input("Enter str2")
    utilities.anagrams(a,b)
except ValueError:
    print("enter strings")
