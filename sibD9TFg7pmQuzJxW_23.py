"""


In statistics a stem-and-leaf plot is a graphical representation of values
distribution in a dataset, usually implemented for a small set of values. In
this exercise we'll build a simple plot for positive integer values following
the steps below.

1) You must separate each value in two parts: the **stem, equal to all number
digits but last** and the **leaf, equal to the last digit**. For numbers in
range 0-9 you must add a "0" at the start. _Examples_ :

  * 4872: stem is "487", leaf is "2".
  * 429: stem is "42", leaf is "9".
  * 85: stem is "8", leaf is "5".
  * 1: stem is "0", leaf is "1".

2) Insert in the plot the **stems without duplicate values in ascending
order** , and for every stem **every proper leaf in ascending order**.
_Examples for a dataset containing 22, 22, 13, 11, 11_ :

  * Stems are 1 and 2 (no duplicates in ascending order).
  * Leaves for stem 1 are 1, 1 and 3 (every leaf in ascending order), leaves for stem 2 are 2 and 2.

Given a list of positive integers you must return the stem-and-leaf plot as a
list of strings, one for each stem: strings have to be formatted with **stem
and leaves separated by " I " (spaces included)** and **leaves in ascending
order separated by a space between them**.

### Examples

    stem_plot([111, 11, 1]) ➞ ["0 | 1", "1 | 1", "11 | 1"]
    
    stem_plot([4, 8, 75]) ➞ ["0 | 4 8", "7 | 5"]
    
    stem_plot([22, 22, 38, 22, 19]) ➞ ["1 | 9", "2 | 2 2 2", "3 | 8"]

### Notes

  * Every given list is valid, containing only positive integers (no exceptions to handle).
  * Pay attention to leading and trailing zeroes.
  * You can find more info about stem-and-leaf plots in the **Resources** tab.

"""

def stem_plot(lst):
  lst2 = sorted(lst)
  stems = [num // 10 for num in lst2]
  leaves = [num % 10 for num in lst2]
  
  plots = {}
  
  for stem, leaf in zip (stems, leaves):
    if plots.get(stem) == None:
      plots[stem] = [leaf]
    else:
      plots[stem].append(leaf)
    
  newlist = [str(stem) + " |" + ''.join([" " + str(leaf) for leaf in plots[stem]]) for stem in stems]
  news = []
  for new in newlist:
    if not new in news:
      news.append(new)
  return news

