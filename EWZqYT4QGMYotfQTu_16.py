"""


Tap code is a way to communicate messages via a series of taps (or knocks) for
each letter in the message. Letters are arranged in a 5x5 _polybius square_ ,
with the letter "K" being moved to the space with "C".

       1  2  3  4  5
    1  A  B C\K D  E
    2  F  G  H  I  J
    3  L  M  N  O  P
    4  Q  R  S  T  U
    5  V  W  X  Y  Z

Each letter is translated by tapping out the _row_ and _column_ number that
the letter appears in, leaving a short pause in-between. If we use "." for
each tap, and a single space to denote the pause:

    text = "break"
    
    "B" = (1, 2) = ". .."
    "R" = (4, 2) = ".... .."
    "E" = (1, 5) = ". ....."
    "A" = (1, 1) = ". ."
    "K" = (1, 3) = ". ..."

Another space is added between the groups of taps for each letter to give the
final code:

    "break" = ". .. .... .. . ..... . . . ..."

Write a function that returns the tap code if given a word, or returns the
translated word (in lower case) if given the tap code.

### Examples

    tap_code("break") ➞ ". .. .... .. . ..... . . . ..."
    
    tap_code(".... ... ... ..... . ..... ... ... .... ....") ➞ "spent"

### Notes

For more information on tap code, please see the resources section. The code
was widely used in WW2 as a way for prisoners to communicate.

"""

def tap_code(txt):
    code = [["a","b","c","d","e"],
            ["f","g","h","i","j"],
            ["l","m","n","o","p"],
            ["q","r","s","t","u"],
            ["v","w","x","y","z"]]
    if txt[0] == ".":
        txt = txt.split(" ")
        for i in range(0,len(txt)):
            if i%2 != 0:
                txt[i] = code[txt[i-1].count(".")-1][txt[i].count(".")-1]
                txt[i-1] = ""
        return "".join(txt)
    else:
        for element in txt:
            if element == "k":
                txt = txt.replace(element, ". ... ")
                continue
            for i in range(0,len(code)):
                if element in code[i]:
                    index = [i+1, code[i].index(element)+1]
                    txt = txt.replace(element, "."*(i+1)+" "+"."*(code[i].index(element)+1)+" ",1)
        return txt[:-1]

