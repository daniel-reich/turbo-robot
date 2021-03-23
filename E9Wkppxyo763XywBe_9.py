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
  h1=time[0]
  h2=time[1]
  m1=time[3]
  m2=time[4]
  s1=time[6]
  s2=time[7]
  list=[]
  list.extend([h1,h2,m1,m2,s1,s2])
  ints=[int(x) for x in list]
  bins=[]
  for i in range(len(ints)):
    a=ints[i]
    if a==0:
      b=[0,0,0,0]
    if a==1:
      b=[0,0,0,1]
    if a==2:
      b=[0,0,1,0]
    if a==3:
      b=[0,0,1,1]
    if a==4:
      b=[0,1,0,0]
    if a==5:
      b=[0,1,0,1]
    if a==6:
      b=[0,1,1,0]
    if a==7:
      b=[0,1,1,1]
    if a==8:
      b=[1,0,0,0]
    if a==9:
      b=[1,0,0,1]
    bins.append(b)
  fix=[]
  for i in range(len(bins)):
    a=bins[i][0]
    fix.append(a)
  for i in range(len(bins)):
    a=bins[i][1]
    fix.append(a)
  for i in range(len(bins)):
    a=bins[i][2]
    fix.append(a)
  for i in range(len(bins)):
    a=bins[i][3]
    fix.append(a)
  b=fix[0:6]
  c=fix[6:12]
  d=fix[12:18]
  e=fix[18:24]
  b2=[str(x) for x in b]
  c2=[str(x) for x in c]
  d2=[str(x) for x in d]
  e2=[str(x) for x in e]
  b2[0]=' '
  b2[2]=' '
  b2[4]=' '
  c2[0]=' '
  j=""
  b3=j.join(b2)
  c3=j.join(c2)
  d3=j.join(d2)
  e3=j.join(e2)
  last=[]
  last.extend([b3,c3,d3,e3])
  return last

