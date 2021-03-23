"""


 **Mubashir** can talk with monkeys. You can also learn their simple language.

Create a function that takes a string `txt` and returns the string in
**monkeys language**. You have to figure out their language from test cases.

### Examples

    monkey_talk("Mubashir Hassan") ➞ "Ook ook."
    
    monkey_talk("Hello") ➞ "Ook."
    
    monkey_talk("Matt") ➞ "Ook."
    
    monkey_talk("Everyone") ➞ "Eek."
    
    monkey_talk("Edabit is Amazing") ➞ "Eek eek eek."

### Notes

A hint in the comments section.

"""

from re import sub
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
def monkey_talk(txt):
    return "{}.".format(sub(r"^[eo]", lambda m: m.group().upper(),
                            sub(r"[A-Za-z]+",
                                lambda m: "eek" if m.group()[0] in vowels
                                else "ook", txt)))

