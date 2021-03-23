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
​
    def find_left(n, l):
                 
        for i in range(1, len(l)):
            j = (n+i)%len(l)
            if l[j] == 'a':
                return j
​
​
    if n < 2:
        return False
    else:
​
        ind = 0
        ind_n = -1
        arr = ['a' for z in range(n)]   
        
        while arr.count('a') > 1:
        
            ind = find_left(ind_n, arr)            
            ind_n = find_left(ind, arr)
            arr[ind_n] = 'x'
      
        return ind

