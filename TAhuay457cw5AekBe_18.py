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

def monkey_talk(txt):
    v = "euioa";
    L = []
    for i in txt.split():
        if i[1] in v:
            L.append("Ook")
        else:
            L.append("eek")
    return " ".join(L).capitalize() + "."

