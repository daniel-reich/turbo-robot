"""


I admit, this challenge is somehow strange. The objective is to find out if a
given list is `True` or `False`. Here are some `True` lists:

    [12, 40, 4, 6420, 20, 24, 400, 24]
    [12.3, 46, 4, 7383, 23, 27, 529, 27.6]
    [14, 80, 6, 12840, 40, 46, 1600, 48]

And here some `False` lists:

    [18.1, 162, 9, 26091, 81, 90, 6561, 97]
    [14.5, 90, 18, 14445, 18, 51, 2025, 54]
    [19.2, 184, 9, 29592, 92, 101, 8464, 110.8]

All 8 values in the lists are connected in some way, you have to find out what
the connection is. Go and play around with the 150 test cases and you'll
figure it out.

### Examples

    tf_lst([12, 40, 4, 6420, 20, 24, 400, 24]) ➞ True
    
    tf_lst([18.1, 162, 9, 26091, 81, 90, 6561, 97]) ➞ False
    
    tf_lst([14.7, 94, 6, 15087, 47, 53, 2209, 56.4]) ➞ True

### Notes

  * All inputs are valid lists with 8 numbers.
  * For a small hint, look at the **Comments** tab.

"""

def tf_lst(arr):
  return arr[0]==10+arr[4]/10 and arr[1]==2*arr[4] and arr[3]==321*arr[4] and \
    5*arr[7]==6*arr[4] and arr[6]==arr[4]**2 and arr[5]==arr[2]+arr[4]

