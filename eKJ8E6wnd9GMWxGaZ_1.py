"""


Given a number, return a string which is formatted into **US Dollars and
cents!**

Remember that:

  * You should round to two digits after the decimal point (even for integers).
  * Thousandths should be separated by commas.

### Examples

    dolla_dolla_bills(10) ➞ "$10.00"
    
    dolla_dolla_bills(1000000) ➞ "$1,000,000.00"
    
    dolla_dolla_bills(-314159.2653) ➞ "-$314,159.27"
    
    dolla_dolla_bills(-56.99) ➞ "-$56.99"

### Notes

  * There will be both negative and positive inputs.
  * Check the **Resources** Tab for many tutorials on how to approach string formatting.

"""

def dolla_dolla_bills(number):
    number_str = str(number)
​
    if "." not in number_str:
        number_str = number_str + ".00"
        
    point = number_str.index(".")
    
    
    if "." in number_str:
        number = number_str[:point+1]
​
        if point+3 < len(number_str):
            number = number + number_str[point+1]
​
            if int(number_str[point+3]) >= 5:
                number += str(int(number_str[point+2]) + 1)
            else:
                number += str(int(number_str[point+2]))
​
        else:    
            number_str += "0"
​
            for index in range(point+1, point+3):
                number += number_str[index]
​
        number_str = number
        length = len(number_str[:point])
​
    if length > 3 and "." not in number_str[:point]: 
        newNum = []
​
        for counter, value in reversed(list(enumerate(number_str[:point]))):
            if (length-counter)%3==0:
                newNum += value + ","
            else:
                newNum+=value
        if "-" in newNum:
            newNum = "".join(newNum[::-1]).strip("-").strip(",")
            newNum = "-" + newNum
        else:
            newNum = "".join(newNum[::-1]).strip(",")
        print(newNum)
        number_str =  newNum + "." + number[-2:]
​
    if "-" in number_str:
        l = list(number_str)
        l[0] = "$"
        number_str ="-" + "".join(l)
    else:
        number_str = "$" + number_str
    return number_str

