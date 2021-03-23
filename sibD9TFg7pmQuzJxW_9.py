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
  stem_=[]
  leaf_=[]
  for i in range(len(lst)):
    if len(str(lst[i]))==1:
      stem_.append(0)
      leaf_.append(lst[i])
    else:
      stem_.append(int(str(lst[i])[:-1]))
      leaf_.append(int(str(lst[i])[-1]))
  stem_sort=stem_.copy()
  stem_sort.sort()
  leaf_sort=leaf_.copy()
  leaf_sort.sort()
  stem_uniq_sorted=list(dict.fromkeys(stem_sort))
  stem_uniq_sorted.sort()
  final_list=[]
  
  def get_index(stem_,stem_value):
    index_=[index for index, value in enumerate(stem_) if value == stem_value]
    return(index_)
  def _leaf_(leaf_,index_):
    list_leaf=[]
    for i in index_:
      list_leaf.append(leaf_[i])
    list_leaf.sort()
    return(list_leaf)
​
  for i in range(len(stem_uniq_sorted)):
    index_=get_index(stem_,stem_uniq_sorted[i])
    list_leaf=_leaf_(leaf_,index_)
    final_leaf=''
    for j in list_leaf:
      final_leaf+=str(j)
      final_leaf+=" "
    final_list.append(str(stem_uniq_sorted[i]) + " " + "|" + " " + final_leaf[:-1])
  return(final_list)

