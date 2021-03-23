"""


A taxi journey costs **$3** for the first kilometer travelled. However, all
kilometers travelled after that will cost **$2** each.

Create a function which returns the **distance** that the taxi must've
travelled, given the **cost** as a parameter.

### Examples

    journey_distance(3) ➞ 1
    # The first kilometer costs $3
    
    journey_distance(9) ➞ 4
    # The first kilometer costs $3 plus the other three kilometers (costing $2 each)
    
    journey_distance(5) ➞ 2

### Notes

  * The input tests are valid integers >= 0.
  * The output will always be a whole number.
  * Remember that you are calculating the distance from the cost, not the other way around!

"""

def journey_distance(n):
    km=0
    if n>=3:
        n-=3
        km+=1
    while n!=0:
        n-=2
        km+=1
    return km

