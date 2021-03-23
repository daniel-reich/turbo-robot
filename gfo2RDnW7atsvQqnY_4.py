"""


Create a function that takes a list of strings and return the number of smiley
faces contained within it. These are the components that make up a valid
smiley:

  * A smiley has **eyes**. Eyes can be `:` or `;`.
  * A smiley has a **nose** but it doesn't have to. A nose can be `-` or `~`.
  * A smiley has a **mouth** which can be `)` or `D`.

No other characters are allowed except for those mentioned above.

### Examples

    count_smileys([":)", ";(", ";}", ":-D"]) ➞ 2
    
    count_smileys([";D", ":-(", ":-)", ";~)"]) ➞ 3
    
    count_smileys([";]", ":[", ";*", ":$", ";-D"]) ➞ 1

### Notes

  * You will always be given a list as input.
  * An empty list should return 0.
  * The order of each facial element will always be the same.
  * Noses are optional (e.g. `:)` and `:-)` are both valid).

"""

def count_smileys(lst):
  smiley = 0
  for i in lst:
    if (len(i)==2 and\
      (i[0]==":" or i[0]==";") and\
      (i[1]==")" or i[1]=="D")):
      smiley = smiley+1
    if (len(i)==3 and\
      (i[0]==":" or i[0]==";") and\
      (i[1]=="~" or i[1]=="-") and\
      (i[2]==")" or i[2]=="D")):
      smiley = smiley+1
    
  return smiley

