"""


Maxie is the largest number that can be obtained by **swapping two digits** ,
Minnie is the smallest. Write a function that takes a number and returns Maxie
and Minnie. Leading zeros are not permitted.

### Examples

    maxmin(12340) ➞ (42310, 10342)
    
    maxmin(98761) ➞ (98761, 18769)
    
    maxmin(9000) ➞ (9000, 9000)
    # Sometimes no swap needed.
    
    maxmin(11321) ➞ (31121, 11123)

### Notes

N/A

"""

def maxie(num):
    str_num = str(num)
    for i in range(len(str_num)):
        largest = str_num[i]
        largest_idx = 0
        for j in range(i+1, len(str_num)):
            if int(largest) <= int(str_num[j]):
                largest = str_num[j]
                largest_idx = j
        if int(largest) > int(str_num[i]):
            s = str_num[:i] + largest + str_num[i+1:largest_idx] + str_num[i] + str_num[largest_idx+1:]
            return int(s)
    return int(str_num)
​
def minnie(num):
    str_num = str(num)
    for i in range(len(str_num)):
        smallest = str_num[i]
        smallest_idx = 0
        for j in range(i+1, len(str_num)):
            if int(smallest) >= int(str_num[j]) and (str_num[j] != '0' or i !=0 ) :
                smallest = str_num[j]
                smallest_idx = j
        if int(smallest) < int(str_num[i]):
            s = str_num[:i] + smallest + str_num[i+1:smallest_idx] + str_num[i] + str_num[smallest_idx+1:]
            return int(s)
    return int(str_num)
​
def maxmin(n):
    return(maxie(n), minnie(n))

