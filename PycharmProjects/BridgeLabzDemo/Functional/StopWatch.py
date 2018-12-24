from Utility import  utilities

try:
    a=int(input("Enter 1 to start the stop watch"))

    utilities.stopwatch(a)
except ValueError:
    print("Not Vald ")