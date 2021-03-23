"""


Given a string of letters, create a function that returns a list with the
separator that yields the longest possible substring, provided that:

  * The substring starts and ends with the separator.
  * The separator doesn't occur inside the substring other than at the ends.

If two or more separators yield substrings with the same length, they should
appear in alphabetical order.

### Examples

    max_separator("supercalifragilistic") ➞ ["s"]
    # The longest substring is "supercalifragilis".
    
    max_separator("laboratory") ➞ ["a", "o", "r"]
    # "abora", "orato" and "rator" are the same length.
    
    max_separator("candle") ➞ []
    # No possible substrings.

### Notes

  * All substrings should be at least of length 2 (i.e. no single-letter substrings).
  * Expect lowercase alphabetic characters only.

"""

def max_separator(txt):
  new=[]
  for al in txt:
    if txt.count(al)==2:
      first=txt.index(al)
      second=txt.index(al,first+1)
      new.append(txt[(first):(second+1)])
    elif txt.count(al)>=3:     
      first=txt.index(al)
      second=txt.index(al,first+1)
      third=txt.index(al,second+1)
      new.append(txt[(first):(second+1)])
      new.append(txt[(second):(third+1)])
  if new==[]:
    return([])
  else:
    maxx=max([len(l) for l in new])
    return(sorted(list(set(sub[0] for sub in new if len(sub)==maxx))))

