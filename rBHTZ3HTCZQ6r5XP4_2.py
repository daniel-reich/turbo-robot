"""


Create a function that expands a decimal number into a string as shown below:

    25.24 ➞ "20 + 5 + 2/10 + 4/100"
    70701.05 ➞ "70000 + 700 + 1 + 5/100"
    685.27 ➞ "600 + 80 + 5 + 2/10 + 7/100"

### Examples

    expanded_form(87.04) ➞ "80 + 7 + 4/100"
    
    expanded_form(123.025) ➞ "100 + 20 + 3 + 2/100 + 5/1000"
    
    expanded_form(50.270) ➞ "50 + 2/10 + 7/100"

### Notes

N/A

"""

def expand_front(n):
    s = str(n)
    p = 10**(len(s) - 1)
    ans = str(int(s[0]) * p)
    p //= 10
    for d in s[1:]:
        if d != '0':
            ans += " + " + str(int(d) * p)
        p //= 10
    return ans
​
def expand_back(n):
    ans = ""
    p = 1
    for d in n:
        p *= 10
        if d != '0':
            ans += " + " + d + "/" + str(p)
    return ans
​
def expanded_form(num):
    ans = expand_front(int(num))
    if num != int(num):
        ans += expand_back(str(num).split('.')[1])
    if ans[:4] == "0 + ":
        ans = ans[4:]
    return ans

