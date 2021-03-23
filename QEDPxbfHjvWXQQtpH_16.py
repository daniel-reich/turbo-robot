"""


Create a function that returns the number of **palindrome numbers** in a
specified range ( **inclusive** ).

For example, between **8** and **34** , there are **5** palindromes: **8** ,
**9** , **11** , **22** and **33**. Between **1550** and **1552** there is
exactly one palindrome: **1551**.

### Examples

    count_palindromes(1, 10) ➞ 9
    
    count_palindromes(555, 556) ➞ 1
    
    count_palindromes(878, 898) ➞ 3

### Notes

Single-digit numbers are trivially palindrome numbers.

"""

def count_palindromes(num1, num2):
    x = list(range(num1,num2+1))
    res = 0
    for i in x:
        if i < 10:
            res +=1
        elif i > 10:
            i = str(i)
            if i == i[::-1]:
                res +=1
    return res

