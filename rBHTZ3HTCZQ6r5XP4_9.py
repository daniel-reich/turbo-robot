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
    num_str = str(num)
    integer, fractional = num_str.split('.')
    integer_form = ''
    count_dozens = len(integer) - 1
    for num in integer:
        if num != '0':
            integer_form += str(int(num) * (10 ** count_dozens)) + ' + '
        count_dozens -= 1
    count_dozens = 1
    for num in fractional:
        if num != '0':
            integer_form += str(int(num)) + '/' + str(10 ** count_dozens) + ' + '
        count_dozens += 1
    return integer_form[:-3]

