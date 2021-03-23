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
    hour = {i:1 for i in range(24) if i % 10 < 6}
    minute, sol = [55, 44, 33, 22, 11, 00], 0
    for full in range(lst[0]+1, lst[3]):
        if full in hour: sol += 6
    if lst[0] != lst[3]:
        if lst[0] in hour:
            for down in minute:
                if down > lst[1]: sol += 1
                elif down == lst[1]:
                    if int(str(lst[0])[::-1]) >= lst[2]: sol += 1
                else: break
        if lst[3] in hour:
            for up in minute[::-1]:
                if up < lst[4]: sol += 1
                elif up == lst[4]:
                    if int(str(lst[3])[::-1]) <= lst[5]: sol += 1
                else: break
    else:
        if lst[0] in hour:
            for down in minute:
                if down > lst[4]: continue
                elif lst[1] < down < lst[4]: sol += 1
                elif down == lst[4]:
                    if int(str(lst[0])[::-1]) <= lst[5]: sol += 1
                elif down == lst[1]:
                    if int(str(lst[0])[::-1]) >= lst[2]: sol += 1
                elif down < lst[1]: break
    return sol

