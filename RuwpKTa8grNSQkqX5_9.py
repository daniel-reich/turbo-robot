"""


Performing division on a fraction often results in an infinitely repeating
decimal.

    1/3=.3333333...  1/7=.142857142857...

Create a function that takes a decimal in string form with the repeating part
in parentheses and returns the equivalent fraction in string form and in
lowest terms.

### Examples

    fractions("0.(6)") ➞ "2/3"
    
    fractions("1.(1)") ➞ "10/9"
    
    fractions("3.(142857)") ➞ "22/7"
    
    fractions("0.19(2367)") ➞ "5343/27775"
    
    fractions("0.1097(3)") ➞ "823/7500"

### Notes

N/A

"""

def gcd(m, n):
    while n != 0:
        t = n
        n = m%n
        m = t
    return m
​
import re
def fractions(text):
    parts = re.findall(r'[0-9.]+',text)
​
    zeros_before = len(parts[0]) - 1 - parts[0].find('.')
    
    int_part = int(parts[0][:parts[0].find('.')])
    
    if zeros_before != 0:
        dec_part_up = int(parts[0][parts[0].find('.')+1:])
        dec_part_down = int(10**zeros_before)
    else:
        dec_part_up = 0
        dec_part_down = 1
    
    part1_len = len(parts[1])
    x = int(parts[1])
    
    x_deno = int((10**part1_len - 1)*(10**zeros_before))
    
    inter_up = x*dec_part_down+dec_part_up*x_deno
    inter_down = dec_part_down*x_deno
    
    gcd_num = gcd(inter_up,inter_down)
    
    final_down = inter_down//gcd_num
    final_up = inter_up//gcd_num + int_part*final_down
    
    result = str(final_up)+'/'+str(final_down)
    
    return result

