"""
At school, we used to play with our calculators and send each other secret
messages. The trick was to enter a special number and turn the calculator
upside-down. LOL ... I mean 707!

Given a number, create a function that converts it into a word by turning the
integer 180 degrees around.

### Examples

    turn_calc(707) ➞ "LOL"
    
    turn_calc(5508) ➞ "BOSS"
    
    turn_calc(3045) ➞ "SHOE"

number| letter  
---|---  
1| I  
2| Z  
3| E  
4| H  
5| S  
6| G  
7| L  
8| B  
9| -  
0| O  
  
### Notes

  * Convert to uppercase words.
  * Ignore dots.

"""

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
letters = ["I", "Z", "E", "H", "S", "G", "L", "B", None, "O"]
d = dict(zip(numbers, letters))
​
​
def turn_calc(n):
    n = str(n)
    txt = ""
    if "." in n:
        a = n.replace(".", "")
        for x in a:
            txt += d[x]
    else:
        for x in n:
            txt += d[x]
    return txt[::-1]

