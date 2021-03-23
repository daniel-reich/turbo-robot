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
  class Column:
​
    def __init__(self, n, light_num = 4):
      self.n = n
      self.ln = light_num
    
    def display(self):
​
      display_lights = {1: [1], 2: [2], 3: [1, 2], 4: [4], 5: [1, 4], 6: [2, 4], 7: [1, 2, 4], 8: [8], 9: [8, 1], 0: []}
      val_indexes = {1: 0, 2: 1, 4: 2, 8: 3}
​
      on = display_lights[self.n]
      display_reversed = []
​
      for n in range(self.ln):
        off = True
        for light in on:
          if val_indexes[light] == n:
            display_reversed.append('1')
            off = False
            break
        if off == True:
          display_reversed.append('0')
      
      for n in range(4 - self.ln):
        display_reversed.append(' ')
      
      return list(reversed(display_reversed))
  
  time = time.split(':')
  
  hour = time[0]
  mins = time[1]
  secs = time[2]
​
  h1 = int(hour[0])
  h2 = int(hour[1])
​
  m1 = int(mins[0])
  m2 = int(mins[1])
​
  s1 = int(secs[0])
  s2 = int(secs[1])
​
  c1 = Column(h1,2)
  c2 = Column(h2)
  c3 = Column(m1,3)
  c4 = Column(m2)
  c5 = Column(s1,3)
  c6 = Column(s2)
​
  rawdisplay = [c1.display(),c2.display(),c3.display(),c4.display(),c5.display(),c6.display()]
  display = ['','','','']
​
  for n in range(4):
    for item in rawdisplay:
      display[n] += item[n]
  
  return display

