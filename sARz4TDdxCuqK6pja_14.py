"""


 **Mubashir** needs your help to identify the spread of a deadly virus. He can
provide you with the following parameters:

  * A two-dimensional array `persons`, containing **affected persons 'V'** and **unaffected persons 'P'**.
  * Number of hours `n`, each infected person is spreading the virus to one person _up, down, left and right_ **each hour**.

Your function should return the updated array containing affected and
unaffected persons after `n` hours.

### Examples

    persons = [
      ["P", "P", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    deadly_virus(persons, 0) ➞ [
      ["P", "P", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    
    deadly_virus(persons, 1) ➞ [
      ["V", "P", "P", "P", "P"],
      ["V", "V", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]
    
    deadly_virus(persons, 2) ➞ [
      ["V", "V", "P", "P", "P"],
      ["V", "V", "V", "P", "P"],
      ["V", "V", "P", "P", "P"],
      ["V", "P", "P", "P", "P"],
      ["P", "P", "P", "P", "P"]
    ]

### Notes

N/A

"""

def deadly_virus(pop, t):
    '''
    Returns a copy of pop updated for the spread of the virus after t hours
    '''
    HEIGHT = len(pop)
    WIDTH = len(pop[0])
​
    def is_infected(pop, i, j):
        '''
        Returns whether the person at pop[i][j] is infected or has an infected
        neighbour who therefore infects them.
        '''
        persons = ((i-1,j),(i+1,j),(i,j),(i,j-1),(i,j+1))
​
        return any(pop[r][c] == 'V' for r,c in persons
                   if 0<=r<HEIGHT and 0<=c<WIDTH)
​
    for _ in range(t):
        new_pop = [['V' if is_infected(pop,i,j) else 'P'
                    for j in range(WIDTH)]
                    for i in range(HEIGHT)]
        pop = new_pop
        
    return pop

