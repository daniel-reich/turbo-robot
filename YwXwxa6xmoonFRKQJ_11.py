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
  if n < 1:
    return False
  else:
    clst =  [1] * n
    i = 0
    while sum(clst) != 1:
      if clst[i] == 1:
        for j in range(n):
          i_j = (i + j + 1) % n
          if clst[i_j] == 1:
            clst[i_j] = 0
            break
      if sum(clst) ==1:
        break
      else:
        i += 1
        i = i % n
  return i
