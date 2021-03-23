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

ones = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",
14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen"}
​
tens = {2:"Twenty",3:"Thirty",4:"Fourty",5:"Fifty",6:"Sixty",7:"Seventy",8:"Eighty",9:"Ninety"}
​
hundreds = {1:"One Hundred",2:"Two Hundred",3:"Three Hundred",4:"Four Hundred",5:"Five Hundred",6:"Six Hundred",7:"Seven Hundred",
8:"Eight Hundred",9:"Nine Hundred"}
​
def digit1(num):
    return ones[num]    
​
def digit2(num,a):
    if(10<=num<=19):
        return ones[num]
    else:
        if(a[1] == "0"):
            if(a[0] == "0"):return ""
            else:return tens[int(a[0])]
        else:
            if(a[0] == "0"):return digit1(num)
            return tens[int(a[0])]+" "+ones[int(a[1])]
​
def digit3(num,a):
    new_num = int(a[1]) * 10 + int(a[2])
    new_a = [a[1],a[2]]
    return hundreds[int(a[0])]+" "+digit2(new_num,new_a)
    
def num_to_eng(num):
    a = []
    for i in str(num):
        a.append(i)
    if(len(a) == 1):
        return digit1(num).lower()
    if(len(a) == 2):
        return digit2(num,a).lower()
    if(len(a) == 3):
        return digit3(num,a).lower()

