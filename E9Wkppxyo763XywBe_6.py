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
    time=time.split(':')
    hh=list(time[0])
    mm=list(time[1])
    ss=list(time[-1])
    row=[]
​
    c1='0000'+bin(int(hh[0]))[2:]
    c2='0000'+bin(int(hh[1]))[2:]
    c3='0000'+bin(int(mm[0]))[2:]
    c4='0000'+bin(int(mm[1]))[2:]
    c5='0000'+bin(int(ss[0]))[2:]
    c6='0000'+bin(int(ss[1]))[2:]
​
​
    print(c1,c2,c3,c4,c5,c6)
    a=" "+c2[-4]+" "+c4[-4]+" "+c6[-4]
    b=" "+c2[-3]+c3[-3]+c4[-3]+c5[-3]+c6[-3]
    c=c1[-2]+c2[-2]+c3[-2]+c4[-2]+c5[-2]+c6[-2]
    d=c1[-1]+c2[-1]+c3[-1]+c4[-1]+c5[-1]+c6[-1]
    row.append(a)
    row.append(b)
    row.append(c)
    row.append(d)
    return row

