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
    """Maxie & Minnie"""
    n = str(n)
​
    # These are the end lists
    lst1 = [i for i in n]  # max
    lst2 = [i for i in n]  # min
​
    # Creating the max and min lists
    max_lst = sorted(lst1, reverse=True)
    min_lst = sorted(lst1)
    z_count = min_lst.count("0")
    if z_count != 0:
        min_lst = (
            min_lst[z_count : z_count + 1]
            + ["0"] * z_count
            + min_lst[z_count + z_count :]
        )
​
    # Checking if the solution is already a max or min
    pot_max = "".join(max_lst)
    pot_min = "".join(min_lst)
​
    # Calculating the maximum
    if pot_max == n:
        maximum = int(pot_max)
    else:
        for i in range(len(lst1)):
            if lst1[i] != max_lst[i]:
                rmb = lst1[i]
                rmb_index = max([k for k, x in enumerate(lst1) if x == max_lst[i]])
​
                lst1[i] = lst1[i].replace(lst1[i], max_lst[i])
                lst1[rmb_index] = rmb
                maximum = int("".join(lst1))
                break
​
    # Calculating the minimum            
    if pot_min == n:
        minimum = int(pot_min)
    else:
        for i in range(len(lst2)):
            if lst2[i] != min_lst[i]:
                rmb = lst2[i]
                rmb_index = max([k for k, x in enumerate(lst2) if x == min_lst[i]])
​
                lst2[i] = lst2[i].replace(lst2[i], min_lst[i])
                lst2[rmb_index] = rmb
                minimum = int("".join(lst2))
                break
​
    return (maximum, minimum)

