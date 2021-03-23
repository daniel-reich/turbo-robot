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

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
        print(x,y)
    return x
​
def fractions(decimal):
    rep = decimal.split("(")[1].split(")")[0]
    num1 = decimal.split("(")[0].replace(".", "") + rep
​
    p_index = decimal.index(".")
    exp1 = decimal.index("(") -1-p_index
    exp2 = decimal.index(")")-2 - p_index
​
    num2 = num1[0:exp1+p_index]
    num = int(num1)-int(num2)
​
    bot = 10**exp2-10**exp1
    d = gcd(num, bot)
    return(str(int(num/d)) + "/" + str(int(bot/d)))

