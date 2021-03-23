"""


Write a function that returns a list of strings populated from the slices of
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
  * A recursive version of this challenge can be found via this [link](https://edabit.com/challenge/TcKZnbdgx7q6LLoFR).

"""

def collect(s, n):
  
  Blocks = []
  
  Start = 0
  Finish = n
  Length = len(s)
  
  while (Finish <= Length):
    Batch = s[Start:Finish]
    Blocks.append(Batch)
    Start += n
    Finish += n
  
  Answer = sorted(Blocks)
  return Answer

