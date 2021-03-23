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
  time = time.replace(":", "")
  grid = []
  for i in range(0, len(time)):
    grid.append(pattern(time[i], i+1))
  return convert(grid)
​
def pattern(number, index):
  if index == 1:
    dict = {
    "0" : "00  ",
    "1" : "10  ",
    "2" : "01  "
    }
    return dict[number]
  elif index == 2 or index == 4 or index == 6:
    dict = {
    "0" : "0000",
    "1" : "1000",
    "2" : "0100",
    "3" : "1100",
    "4" : "0010",
    "5" : "1010",
    "6" : "0110",
    "7" : "1110",
    "8" : "0001",
    "9" : "1001"
    }
    return dict[number]
  elif index == 3 or index == 5:
    dict = {
    "0" : "000 ",
    "1" : "100 ",
    "2" : "010 ",
    "3" : "110 ",
    "4" : "001 ",
    "5" : "101 "
    }
    return dict[number]
​
def convert(grid):
  grid_temp = []
  word = ""
  for i in range(4-1, -1, -1):
    word = word + grid[0][i] + grid[1][i] + grid[2][i] + grid[3][i] + grid[4][i] + grid[5][i]
    grid_temp.append(word)
    word = ""
  return grid_temp

