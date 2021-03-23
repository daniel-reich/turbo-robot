"""


Write a function that accepts a positive integer between `0` and `999`
inclusive and returns a string representation of that integer written in
English.

### Examples

    num_to_eng(0) ➞ "zero"
    
    num_to_eng(18) ➞ "eighteen"
    
    num_to_eng(126) ➞ "one hundred twenty six"
    
    num_to_eng(909) ➞ "nine hundred nine"

### Notes

  * There are no hyphens used (e.g. "thirty five" not "thirty-five").
  * The word "and" is not used (e.g. "one hundred one" not "one hundred and one").

"""

def num_to_eng(n):
    d = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
    
    def double_digits(n):
        if str(n)[-1] == '0':
            return d[n]
        else:
            return d[int(str(n)[0]+'0')] + ' ' + d[int(str(n)[-1])]    
​
    if n < 21:
        return d[n]
    elif n < 100:
        return double_digits(n)
    else:
        if str(n)[1:] == '00':
             return d[int(str(n)[0])] + ' ' + d[100]
        return d[int(str(n)[0])] + ' ' + d[100] + ' ' + num_to_eng(int(str(n)[1:]))

