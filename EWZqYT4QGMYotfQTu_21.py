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

code_list = [
    ["a", "b", "c", "d", "e"],
    ["f", "g", "h", "i", "j"],
    ["l", "m", "n", "o", "p"],
    ["q", "r", "s", "t", "u"],
    ["v", "w", "x", "y", "z"],
]
​
code_dict = {
    "a": ". .",
    "c": ". ...",
    "b": ". ..",
    "e": ". .....",
    "d": ". ....",
    "g": ".. ..",
    "f": ".. .",
    "i": ".. ....",
    "h": ".. ...",
    "k": ". ...",
    "j": ".. .....",
    "m": "... ..",
    "l": "... .",
    "o": "... ....",
    "n": "... ...",
    "q": ".... .",
    "p": "... .....",
    "s": ".... ...",
    "r": ".... ..",
    "u": ".... .....",
    "t": ".... ....",
    "w": "..... ..",
    "v": "..... .",
    "y": "..... ....",
    "x": "..... ...",
    "z": "..... .....",
}
​
​
def tap_code(text):
    if "." in text:
        return code_to_text(text)
    return text_to_code(text)
​
​
def code_to_text(code):
    output_text = ""
    a = code.split(" ")
    b = zip(a[::2], a[1::2])
    for c in b:
        output_text += code_list[len(c[0]) - 1][len(c[1]) - 1]
    return output_text
​
​
def text_to_code(text):
    output_text = ""
    for c in text:
        output_text += code_dict[c] + " "
    return output_text.strip()

