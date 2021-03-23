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
  h=[0 for i in range(2)]
  m=[0 for i in range(2)]
  s=[0 for i in range(2)]
  hh,mm,ss=time.split(":")
  h[0],h[1]=bin(int(hh[0]))[2:].zfill(4),bin(int(hh[1]))[2:].zfill(4)
  m[0],m[1]=bin(int(mm[0]))[2:].zfill(4),bin(int(mm[1]))[2:].zfill(4)
  s[0],s[1]=bin(int(ss[0]))[2:].zfill(4),bin(int(ss[1]))[2:].zfill(4)
  t=[]
  t.append([h[0]])
  t.append([h[1]])
  t.append([m[0]])
  t.append([m[1]])
  t.append([s[0]])
  t.append([s[1]])
  r=[]
  for i in range(4):
    a=""
    for j in range(len(t)):
      a+=t[j][0][i]
    r.append(list(a))
  r[0][0]=' '
  r[0][2]=' '
  r[0][4]=' '
  r[1][0]=' '
  for i in range(len(r)):
    r[i]=''.join(r[i])
  return r

