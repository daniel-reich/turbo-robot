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
    n , d = str(num).split('.')
    temp = []
    temp2 = []
    for idx,num in enumerate(n[::-1]):
        if num != '0':
            temp = [str(int(num) * 10 ** idx)] + temp
    for idx,num in enumerate(d):
        if num != '0':
            temp2 += [num + '/' + str(10 ** (idx + 1))]
    return ' + '.join(temp + temp2)

