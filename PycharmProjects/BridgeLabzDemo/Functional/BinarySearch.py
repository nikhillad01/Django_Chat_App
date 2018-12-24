from Utility import utilities

try :
    l = [9, 4, 6, 7, 1,0,6,2]
    string_list=list(map(str, l))
    print()
    # a=int(input("Enter total numbers in list"))
    # for i in range(0,a):
    #     b=input("Enter element in list ")
    #     l.append(b)
    print(l)
    print("String List : ",string_list)
    print()
    print("***************Binary String Search***********************")
    x=input("Enter String to find Binary Search ")
    utilities.binary_search(string_list,x)
    #**************************** Binary Search **************************
    print("***********************Binary Integer Search***************")
    x2 = int(input("Enter Integer Binary Search"))
    utilities.binary_search(l, x2)
    print("***************************Insertion Sort***********************************")
    utilities.insertion_sort(l)
    print("***************************Insertion String Sort***********************************")
    utilities.insertion_sort(string_list)
    print("************************** Bubble Sort Integer**************************************")
    utilities.bubble_sort(l)
    print("************************** Bubble Sort String**************************************")
    utilities.bubble_sort(string_list)


    print()
    print("Time For all Dict ",utilities.timeDict)
except ValueError:
    print("ValueError")