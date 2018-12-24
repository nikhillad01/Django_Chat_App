from Utility import utilities
try:
    a=int(input("Enter number to find nth harmonic "))
    utilities.harmonic(a)
except(ZeroDivisionError,ValueError):
    print("Enter valid number")