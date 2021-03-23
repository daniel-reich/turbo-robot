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

def monkey_word(word):
    return "eek" if word[0] in "aeiou" else "ook"
    
def monkey_talk(txt):
    words = txt.lower().split()
    word = monkey_word(words[0])
    ans = word[0].upper() + word[1:]
    for word in words[1:]:
        ans += " " + monkey_word(word)
    return ans + "."

