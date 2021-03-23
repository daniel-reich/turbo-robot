"""


Create a function that converts a string of letters to their respective number
in the alphabet.

A| B| C| D| E| F| G| H| I| J| K| L| M| N| O| P| Q| R| S| T| U| V| W| ...  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
0| 1| 2| 3| 4| 5| 6| 7| 8| 9| 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20| 21|
22| ...  
  
### Examples

    alph_num("XYZ") ➞ "23 24 25"
    
    alph_num("ABCDEF") ➞ "0 1 2 3 4 5"
    
    alph_num("JAVASCRIPT") ➞ "9 0 21 0 18 2 17 8 15 19"

### Notes

  * Make sure the numbers are spaced.
  * All letters will be UPPERCASE.

"""

def alph_num(txt):
  l = []
  for i in txt:
    l.append(str(ord(i) - 65))
  return ' '.join(l)

