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
    lst = [str(i) if len(str(i)) == 2 else '0' + str(i) for i in lst]
    palindromes = ['00','11','22','33','44','55']    
    times = []
    a = int(lst[0] + lst[1] + lst[2])
    b = int(lst[3] + lst[4] + lst[5])
    for i in range(int(lst[0]),int(lst[3])+1):
        for j in palindromes:
            if i < 6:
                times.append('0' + str(i) + j + ('0' + str(i))[::-1])
            if i >= 10 and i < 16:
                times.append(str(i) + j + str(i))
            if i >= 20:
                times.append(str(i) + j + str(i))
    ans = list(filter(lambda x: int(x) >= a and int(x) <= b,times))
    return len(ans)

