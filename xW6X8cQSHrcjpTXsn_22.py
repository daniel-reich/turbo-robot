"""


Write a function that returns the **lexicographically first** and
**lexicographically last** rearrangements of a lowercase string. Output the
results in the following manner:

    first_and_last(string) ➞ [first, last]

### Examples

    first_and_last("marmite") ➞ ["aeimmrt", "trmmiea"]
    
    first_and_last("bench") ➞ ["bcehn", "nhecb"]
    
    first_and_last("scoop") ➞ ["coops", "spooc"]

### Notes

  *  **Lexicographically first** : the permutation of the string that would appear **first** in the English dictionary (if the word existed).
  *  **Lexicographically last** : the permutation of the string that would appear **last** in the English dictionary (if the word existed).

"""

def first_and_last(s):
  word = [i for i in s];
  word.sort();
  first="";
  last="";
  for i in range(len(word)):
    first+=word[i];
    
  for j in range(len(word)-1,-1,-1):
    last+=word[j];
    
  lex=[first,last];
  return lex;

