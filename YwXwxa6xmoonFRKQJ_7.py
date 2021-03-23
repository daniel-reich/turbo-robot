"""


The Josephus Problem is a mathematical problem in which a circle is made, its
circumference formed of `n` people.

Starting from the person in the 0th position, each person eliminates the
person to their left (the next person in the circle). The next living person
then does the same, and the process is repeated until there is only one person
left alive..

Find the position (index - starting from 0) of the last man standing for a
circle of n people.

### Examples

    josephus(0) ➞ False
    
    josephus(3) ➞ 2
    
    josephus(6) ➞ 4
    
    josephus(9) ➞ 2

### Notes

  * An algebraic solution is in the **Tests** tab. This is not the sort of solution this challenge requires.
  * If you haven't come across this problem before, please take a look at the link in the Resources section. It is explained much better than my instructions above!
  * Do this by simulating the problem. Do not simply use the mathematical formula, ie. create the circle and perform the eliminations turn by turn.
  * If the number of people in the circle is less than 1, return `False`.

"""

def josephus(n):
  if n < 1: return False
  circle, k = list(range(n)), 0
  while len([p for p in circle if p != -1]) > 1:
    if circle[k] == -1: k = (k+1)%n
    else: circle[circle.index([x for x in circle[k+1:]+circle[:k] if x!=-1][0])],k = -1,(k+2)%n
  return max(circle)

