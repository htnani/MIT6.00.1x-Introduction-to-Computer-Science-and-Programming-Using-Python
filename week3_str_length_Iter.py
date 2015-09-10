# Although Python provides a built-in function for computing the length of a string, we can write our own.

# Write an iterative function, lenIter, which computes the length of an input argument (a string), 
# by counting up the number of characters in the string.

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    length = 0
    for letter in aStr:
        length += 1
    return length
