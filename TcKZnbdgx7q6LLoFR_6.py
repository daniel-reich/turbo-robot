"""


Write a function that returns an array of strings populated from the slices of
**n-length** characters of the given word (a slice after another while
**n-length** applies onto the word).

### Examples

    collect("intercontinentalisationalism", 6)
    ➞ ["ationa", "interc", "ntalis", "ontine"]
    
    collect("strengths", 3)
    ➞ ["eng", "str", "ths"]
    
    collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15)
    ➞ ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]

### Notes

  * Ensure that the resulting array is lexicographically ordered.
  * Return an **empty** array if the _given string_ is less than `n`.
  * You are expected to solve this challenge via a **recursive** approach.
  * You can check on the **Resources** tab for more details about recursion.
  * An **iterative** version of this challenge can be found via this [link](https://edabit.com/challenge/3W2TRbuD2cnBoXuby).

"""

def collect(s, n, l = [], i = 0, ni = 0, st = ''):
  if i == 0:
    l = []
  if i == len(s):
    if len(st) == n:
      l.append(st)
    return sorted(l)
  else:
    if ni == n:
      l.append(st)
      ni = 0
      st = ''
    st += s[i]
    ni += 1
    i += 1
    
    return collect(s, n, l, i, ni, st)
  # your recursive solution here

