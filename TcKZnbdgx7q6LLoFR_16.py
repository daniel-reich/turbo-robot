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

def collect(s, n):
  # your recursive solution here
  if len(s) < n:
    return []
  result = [s[:n]] + [i for i in collect(s[n:], n)]
  result.sort()
  return result

