print("Enter two strings: \n")
string1 = input()
string2 = input()

def stringCompare(string1, string2):
    length = 0
    if(len(string1) > len(string2)):
        length = len(string1) - len(string2)
        print("First string is longer by %s characters." % length)
    elif(len(string1) < len(string2)):
        length = len(string2) - len(string1)
        print("Second string is longer by %s characters." % length)
    else:
        print("Strings are equal length.")


stringCompare(string1, string2)