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
  d={'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6', 'h':'7', 'i':'8', 'j':'9', 'k':'10', 'l':'11', 'm':'12', 'n':'13', 'o':'14', 'p':'15', 'q':'16', 'r':'17', 's':'18', 't':'19', 'u':'20', 'v':'21', 'w':'22', 'x':'23', 'y':'24', 'z':'25'}
  return ' '.join([d.get(char) for char in txt.lower()])

