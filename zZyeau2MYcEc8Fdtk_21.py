"""


Create a function that takes two integers, `num` and `n`, and returns an
integer which is divisible by `n` and is the closest to `num`. If there are
two numbers equidistant from `num` and divisible by `n`, select the larger
one.

### Examples

    round_number(33, 25) ➞ 25
    
    round_number(46, 7) ➞ 49
    
    round_number(133, 14) ➞ 140

### Notes

`n` will always be a positive number.

"""

def round_number(num, n):
    i=num
    my_list = []
    while(i%n!=0):
        i+=1
    my_list.append(i)
    
    j=num
    while(j%n!=0):
        j-=1
    my_list.append(j)
    #print(my_list)
    diff_list = []
    diff_list.append(abs(my_list[0]-num))
    diff_list.append(abs(my_list[1]-num))
    #print(diff_list)
    if (diff_list[0] == diff_list[1]):
        return my_list[0]
    elif(diff_list[0]<diff_list[1]):
        return my_list[0]
    else:
        return my_list[1]
        
​
​
print(round_number(33, 25))

