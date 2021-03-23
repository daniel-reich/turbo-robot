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

quit()

