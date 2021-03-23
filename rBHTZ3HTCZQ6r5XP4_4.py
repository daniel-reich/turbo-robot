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

def expanded_form(num):
    n1, n2 = str(num).split('.')
    p = len(n1)
    m1 = " + ".join(map(lambda i:
                    str(int(n1[i])*10**(p - i -1)),
                    filter(lambda i: int(n1[i]) !=0, range(p))))
    p = len(n2)
    m2 = " + ".join(map(lambda i:
                    str(int(n2[i])) + '/' + str(10**(i + 1)),
                    filter(lambda i: int(n2[i]) !=0, range(p))))
    if m1 and m2:
        return(m1 + " + " + m2)
    return(m1 + m2)

