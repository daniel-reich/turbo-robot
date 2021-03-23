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
  people = [i for i in range(n)]
  index = 1
  if n < 1:
    return False
  elif n == 1:
    return 0
  else:
    while len(people) != 1:
      if people[index] == people[-1]:
        people.pop(index)
        index = 1
      elif people[index] == people[-2]:
        people.pop(index)
        index = 0
      else:
        people.pop(index)
        index += 1
    return people[0]
      
# [0, 1, 2, 3]

