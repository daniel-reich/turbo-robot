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

def turn_calc(num):
  a = str(num)
  str1 = a.replace('.','')
  b = str1.replace('1','I').replace('2','Z').replace('3','E').replace('4','H').replace('5','S').replace('6','G').replace('7','L').replace('8','B').replace('0','O')
  return b[::-1]

