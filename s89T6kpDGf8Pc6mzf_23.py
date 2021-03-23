"""


![](https://edabit-challenges.s3.amazonaws.com/segment4.gif)

The table below shows which of the segments `a` through `g` are illuminated on
the seven segment display for the digits `0` through `9`. When the number on
the display changes, some of the segments may stay on, some may stay off, and
others change state (on to off, or off to on).

Create a function that accepts a string of digits, and for each transition of
one digit to the next, returns a list of the segments that change state.
Designate the segments that turn on as uppercase and those that turn off as
lowercase. Sort the lists in alphabetical order.

For example:

    seven_segment("805") ➞ [["g"], ["b", "e", "G"]]

In the transition from `8` to `0`, the `g` segment turns off. Others are
unchanged. In the transition from `0` to `5`, `b` and `e` turn off and `G`
turns on. Others are unchanged.

Digit| Lit Segments  
---|---  
0| abcdef  
1| bc  
2| abdeg  
3| abcdg  
4| bcfg  
5| acdfg  
6| acdefg  
7| abc  
8| abcdefg  
9| abcfg  
  
### Examples

    seven_segment("02") ➞ [["c", "f", "G"]]
    
    seven_segment("08555") ➞ [["G"], ["b", "e"], [], []]
    # Empty lists designate no change.
    
    seven_segment("321") ➞ [["c", "E"], ["a", "C", "d", "e", "g"]]
    
    seven_segment("123") ➞ [["A", "c", "D", "E", "G"], ["C", "e"]]
    
    seven_segment("3") ➞ []
    
    seven_segment("33") ➞ [[]]

### Notes

N/A

"""

def seven_segment(txt):
  D={'0':('abcdef','g'),
  '1':('bc','adefg'),
  '2':('abdeg','cf'),
  '3':('abcdg','ef'),
  '4':('bcfg','ade'),
  '5':('acdfg','be'),
  '6':('acdefg','b'),
  '7':('abc', 'defg'),
  '8':('abcdefg',''),
  '9':('abcfg','de')}
  res=[[] for _ in range(len(txt)-1)]
  for i in range(len(txt)-1):
    for x in D[txt[i]][0]:
      if x in D[txt[i+1]][-1]:
        res[i].append(x)
    for y in D[txt[i]][-1]:
      if y in D[txt[i+1]][0]:
        res[i].append(y.upper())
  B=[sorted(x, key=lambda t: t.lower()) for x in res]
  return B

