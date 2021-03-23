"""


Create a function that can take 1, 2, or 3 arguments (like the range function)
and returns a tuple. This should be able to return float values (as opposed to
the range function which can't take float values as a step).

### Examples

    drange(1.2, 5.9, 0.45) ➞ (1.2, 1.65, 2.1, 2.55, 3.0, 3.45, 3.9, 4.35, 4.8, 5.25, 5.7)
    
    drange(10) ➞ (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    
    drange(1, 7, 1.2) ➞ (1, 2.2, 3.4, 4.6, 5.8)
    # Here 7 is not included, like in the range function.

### Notes

Always round values to the number with the most decimal digits (e.g. in the
first example, the answer should always be rounded to 2 digits. In the second,
it should be rounded to 0 digits and the third, 1 digit).

"""

def drange(*args):
    my_list = []
    dec = []
    final_list = []
    round_dig = 0
    round_num = 0
    for i in range (0,len(args)):
        my_str = str(args[i])
        dec = my_str.split(".")
        if (len(dec) == 2):
            round_dig = len(dec[1])
            final_list.append(round_dig)
    
    if (final_list == []):
        round_num = 0
    elif (len(final_list) == 1):
        round_num = int(final_list[0])
    else:
        final_list.sort()
        final_list.reverse()
        round_num = int(final_list[0])
    
    num = args[0]
    
    if (len(args) == 3):
        my_tup = ()
        my_tup = my_tup + (num,)
        while(num<args[1]):
            num+=args[2]
            num = round(num,round_num)
            my_tup = my_tup + (num,)
        return my_tup[0:len(my_tup)-1]
    elif (len(args) == 2):
        my_tup = ()
        for i in range (args[0],args[1]):
            my_tup = my_tup + (i,)
        return my_tup
    elif (len(args) == 1):
        my_tup = ()
        for i in range (0,args[0]):
            my_tup = my_tup + (i,)
        return my_tup
            
            
            
print(drange(10))

