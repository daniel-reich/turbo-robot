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

def check(h1, m1, s1):
    h, m, s = str(h1).zfill(2), str(m1).zfill(2), str(s1).zfill(2)
    return m == m[::-1] and h == s[::-1]
​
def palindrome_time(lst):
    h1, m1, s1, h2, m2, s2 = lst
    cnt = 0
    while [h1, m1, s1] != [h2, m2, s2]:
        if check(h1, m1, s1):
            cnt +=1
        s1 += 1
        if s1 == 60:
            s1 = 0
            m1 += 1
            if m1 == 60:
                m1 = 0
                h1 += 1
    if check(h1, m1, s1):
        cnt +=1
    return cnt

