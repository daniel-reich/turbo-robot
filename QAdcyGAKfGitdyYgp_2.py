"""


A bacterial culture on day 1 has only one bacterium with mass 1. Every day,
some number of bacteria will split (possibly zero or all). When a bacterium of
mass `m` splits, it becomes two bacteria of mass `m/2` each. Also, every
night, the mass of every bacteria will increase by one.

Write a function that determines the minimum number of nights for the culture
to reach the `final_mass`.

### Examples

    bacteria(9) ➞ 3
    
    # Day 1
    # The bacterium with mass 1 splits. There are now two bacteria with mass 0.5 each.
    
    # Night 1
    # All bacteria's mass increases by one. There are now two bacteria with mass 1.5.
    
    # Day 2
    # None split.
    
    # Night 2
    # There are now two bacteria with mass 2.5.
    
    # Day 3
    # Both bacteria split. There are now four bacteria with mass 1.25.
    
    # Night 3
    # There are now four bacteria with mass 2.25.
    # The total mass is 2.25 + 2.25 + 2.25 + 2.25 = 9.
    # It can be proved that 3 is the minimum number of nights needed.
    # There are also other ways to obtain total mass 9 in 3 nights.
    
    bacteria(16) ➞ 4
    
    bacteria(548) ➞ 9
    
    bacteria(5467) ➞ 12

### Notes

  * This is a simplified version of [D. Phoenix and Science](https://codeforces.com/problemset/problem/1348/D).
  * The input will always be an integer.

"""

def bacteria(final_mass):
    states = [(1, 1)]
    nights = 0
    proceed = True
    while proceed:
        nights += 1
        new_states = []
        for s in states:
            n, m = s[0], s[1] + 1
            if n * m < final_mass:
                new_states.append((n, m))
            else:
                return nights
            n, m = 2 * s[0], s[1] / 2 + 1
            if n * m < final_mass:
                new_states.append((n, m))
            else:
                return nights
        states = new_states
    return nights

