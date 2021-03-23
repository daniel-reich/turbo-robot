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

def tap_code(text):
    a = [['A',1,1],['B',1,2],['C',1,3],['K',1,3],['D',1,4],['E',1,5],['F',2,1],['G',2,2],['H',2,3],['I',2,4],['J',2,5],['L',3,1],['M',3,2],['N',3,3],['O',3,4],['P',3,5],['Q',4,1],['R',4,2],['S',4,3],['T',4,4],['U',4,5],['V',5,1],['W',5,2],['X',5,3],['Y',5,4],['Z',5,5]]
    m = ''
    if text[0] == '.':
        text = text.replace(' ',',')
        text += ','
        ctr = 0
        ctra = 0
        v = []
        vtemp = []
        for i in range(len(text)):
            if text[i] == '.':
                ctr += 1
            else:
                if ctra%2 == 0 and i > 0:
                    vtemp.append(ctr)
                    ctr = 0
                    ctra += 1
                else:
                    vtemp.append(ctr)
                    v.append(vtemp)
                    vtemp = []
                    ctr = 0
                    ctra += 1
        for i in range(len(v)):
            for j in range(len(a)):
                if v[i][0] == a[j][1] and v[i][1] == a[j][2]:
                    m += a[j][0].lower()
                    break
        return m
    else:
        for i in range(len(text)):
            for j in range(len(a)):
                if text[i] == a[j][0].lower():
                    m += '.'*a[j][1]+' '+'.'*a[j][2]+' '
        return m[:-1]

