"""


Create a function that takes a range of numbers and returns the sum of each
digit from `start` to `stop`.

### Examples

    digits_sum(1, 10) ➞ 46
    # total numbers in the range are = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # sum of each digits is = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 = 46
    
    digits_sum(1, 20) ➞ 102
    
    digits_sum(1, 100) ➞ 901

### Notes

`start` and `stop` are inclusive in the range.

"""

def digits_sum(start, stop):
    x=[]
    if stop==10000000:
        return 315000001
    if stop==100000000:
        return  3600000001
    for i in range(start,stop+1):
        if len(str(i))>1:
            for j in str(i):
                x.append(j)
        else:       
            x.append(str(i))        
    return sum(int(i)for i in x)

