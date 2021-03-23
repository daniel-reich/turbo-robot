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
    h1, m1, s1 = lst[0:3]
    h2, m2, s2 = lst[3:]
    np = 0
    if m1 > 55:
        h1 += 1
        m1 = 0
    h1p = int(str(100 + h1)[-2::-1])
    for h in range(h1, h2 + 1):
        if 6 <= h % 10 <= 9:
            continue
        
        mf = 0 if h != h1 else 11 * (m1 // 11) + (11 if m1 % 11 else 0)
        for m in range(mf, 60, 11):
            if h == h2 and (m > m2 or (h1 == h1 and m == m1 and not (s1 <= h1p <= s2))):
                break
            np += 1
    return np

