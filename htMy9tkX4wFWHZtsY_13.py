"""


Create a function that counts number of palindromes within two timestamps
inclusive. A palindrome is a timestamp that can be read the same from left to
right and from right to left (e.g. `02:11:20`).

### Examples

    palindrome_time([2, 12, 22, 4, 35, 10]) ➞ 14
    
    palindrome_time([12, 12, 12, 13, 13, 13]) ➞ 6
    
    palindrome_time([6, 33, 15, 9, 55, 10]) ➞ 0

### Notes

Input list contains six numbers `[h1, m1, s1, h2, m2, s2]` for begin and end
timestamps.

"""

def palindrome_time(lst):
    start_time = lst[:3]
    end_time = lst[3:]
    mins = [0, 11, 22, 33, 44, 55]
    hours = ['00', '01', '02', '03', '04', '05', '10', '11', 
             '12', '13', '14', '15', '20', '21', '22', '23']
​
    total = 0
    for h in hours:
        for m in mins:
            t = [int(h), m, int(h[::-1])]
            if start_time <= t <= end_time:
                total += 1
    return total

