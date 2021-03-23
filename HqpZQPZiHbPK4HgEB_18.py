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

def maxmin(n):
    minie = str(n)
    maxie = str(n)
    num_list = list(str(n))
    length=len(num_list)
    
    for first in range (0,length-1):
        for second in range (first+1, length):
            if first == 0 and num_list [second] == "0":
                continue
            else:
                new_list = num_list.copy()
                new_list[first] = num_list [second]
                new_list[second] = num_list [first]
                new_string = "".join(new_list)
                if new_string < minie:
                    minie = new_string
                elif new_string > maxie:
                    maxie = new_string
                    
    return (int(maxie), int(minie))

