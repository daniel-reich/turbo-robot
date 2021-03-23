"""


Captain Hook and his crew are currently resting at Origin Shore. They are
about to embark on their next adventure to an undisclosed location `(x, y)` to
find treasure.

Captain Hook's ship can only move exactly north, south, east or west. It takes
exactly 1 day for the ship to travel 1 unit in one of the four cardinal
directions.

After every 5 days, the crew will take one day of rest.

Given the location of the treasure, find out how long it takes for Captain
Hook and his crew to find the treasure. The ship is currently at coordinate
`(0, 0)`.

    number_of_days([3, 5]) => 9 days
    # Since: 3 days east + 2 days north (5 days passed) + 1 day of rest + 3 days north
    
    number_of_days([-4, -1]) => 5 days
    # Since 4 days west + 1 day south

### Examples

    number_of_days([10, 10]) ➞ 23
    
    number_of_days([3, 3]) ➞ 7
    
    number_of_days([-10, -9]) ➞ 22
    
    number_of_days([-1, -2]) ➞ 3

### Notes

N/A

"""

def number_of_days(coordinate):
  if (abs(coordinate[0])+abs(coordinate[1]))%5==0:
    return (abs(coordinate[0])+abs(coordinate[1]))+(abs(coordinate[0])+abs(coordinate[1]))//5-1
  else:
    return (abs(coordinate[0])+abs(coordinate[1]))+(abs(coordinate[0])+abs(coordinate[1]))//5

