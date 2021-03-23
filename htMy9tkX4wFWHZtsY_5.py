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
        a=[6,6,6,6,6,0,0,0,0,6,6,6,6,6,6,0,0,0,0,6,6,6,6]
        b=sum(a[lst[0]:lst[3]])
        if b>=0 and (lst[0]<6 or 16>lst[0]>=10 or lst[0]>=20):
                if lst[1]%11==0:b=b-(lst[1]//11)+1
                else:b=b-(lst[1]//11)
        if b>=0 and (lst[3]<6 or 16>lst[3]>=10 or lst[3]>=20):
                if lst[4]%11==0:b=b+(lst[4]//11)+2
                else:b=b+(lst[4]//11)
        if b>=0 and (int("".join(list(str(a[1]))[::-1]))<lst[0]) and (lst[4]%11==0):b=b-2
        return b

