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

def swapper(n_str, s_num):
    '''
    Helper to maxmin. Checks each digit in n_str against sorted version s_num then swaps
    the 1st non matching digit in s_num found from the right of n_str.
    '''
    size = len(n_str)
    n_str_copy = n_str[:]
    for i in range(size):
        if s_num[i] != n_str[i]:
            d = s_num[i]
            for j in range(size - 1, -1, -1):
                if n_str[j] == d:
                    n_str_copy[i], n_str_copy[j] = n_str_copy[j], n_str_copy[i]
                    return n_str_copy
​
    return n_str_copy
​
def maxmin(n):
    '''
    Returns a tuplem(maxie, minnie) where maxie is the largest version of n
    obtainable swapping 2 digits and minnie the smallest (with no leading
    zeroes).
    '''
    n_str = list(str(n))
    maxie = sorted(n_str, reverse=True)
    minnie = sorted(n_str)
    
    # Remove any leading zero from minnie
    if minnie[0] == '0':
        for i in range(1,len(minnie)):
            if minnie[i] != '0':
                minnie[0], minnie[i] = minnie[i], minnie[0]  # swap
                break
            
    return ((int(''.join(swapper(n_str,maxie))), int(''.join(swapper(n_str,minnie)))))

