"""


A binary clock displays the time of day in binary format. Modern binary clocks
have six columns of lights; two for each of the hours, minutes and seconds.
The photo below shows a binary clock displaying the time "12:15:45":

![](https://edabit-challenges.s3.amazonaws.com/220px-Digital-BCD-clock.jpg)

The binary values increase from the bottom to the top row. Lights on the
bottom row have a value of 1, lights on the row above have a value of 2, then
4 on the row above that, and finally a value of 8 on the top row. Any 24-hour
time can be shown by switching on a certain combination of lights. For
example, to show the time "10:37:49":

![](https://edabit-challenges.s3.amazonaws.com/440px-Binary_clock.svg.png)

You've decided to build your own binary clock, and you need to figure out how
to light each row of the clock to show the correct time. Given the time as a
string, return a `list` containing strings that shows the lights for each row
of the clock (top to bottom). Use "1" for on, and "0" for off. Leave a blank
space for any part of the row that doesn't require a light.

### Examples

    binary_clock("10:37:49") ➞ [
      " 0 0 1",
      " 00110",
      "001100",
      "101101"
    ]
    
    binary_clock("18:57:31") ➞ [
      " 1 0 0",
      " 01100",
      "000110",
      "101111"
    ]
    
    binary_clock("10:50:22") ➞ [
      " 0 0 0",
      " 01000",
      "000011",
      "101000"
    ]

### Notes

See the **Resources** section for more information on binary clocks.

"""

def binary_clock(time):
    lst = [bin(int(each)).replace("0b","").rjust(2,"0").rjust(4," ") if idx == 0  else bin(int(each)).replace("0b","").rjust(3,"0").rjust(4, " ") if idx == 2 or idx == 4 else bin(int(each)).replace("0b","").rjust(4,"0") for idx, each in enumerate(time.replace(":",""))]
    newlst, newlst1 = [], []
    print(lst)
    leng = 0
    for i in range(4):
        for item in lst:
            newlst.append(item[leng])
        leng += 1
        newlst1.append(''.join(newlst))
        newlst = []
​
    return newlst1

