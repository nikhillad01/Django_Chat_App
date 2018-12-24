from Utility import utilities

try:
    l=list(input("Enter elements with space"))
    utilities.bubble_sort(l)
except ValueError:
    print("Enter valid values")