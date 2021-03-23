"""


John realised that many of his tweets on Twitter are under 140 characters. He
wishes to make full use of the allocated space by using any of the remaining
space by filling it in with lolololol until he hits 140 characters.

For example, if his message is:

    "What a wonderful day!"

He instead wants to tweet:

    "What a wonderful day!lololololololololololololololololololololololololololololololololololololololololololololo
    lolololololololololololololol"

Note that the "lololol ..." part must always end with an "l". To achieve this,
you may leave a space between the message and the start of the "lolololol ..."
part.

That is to say:

    "Odd"

Will become:

    "Oddlolololololololololololololololololololololololololololololololololololololololololololol
    olololololololololololololololololololololololol"
    
    # Without a space.

And ...

    "Even"

Will become:

    "Even lololololololololololololololololololololololololololololololololololololololololololololololol
    olololololololololololololololololololol"
    
    # With a space.

Help John code a function that will take in the string of his message without
the lololol part and return a string containing a tweet as per John's
specifications.

### Examples

    pad("Even") ➞ "Even lololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololol"
    
    pad("Odd") ➞ "Oddlolololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololololol"
    
    pad("I love the new challenge") ➞ "I love the new challenge lololololololololololololololololololololololololololololololololololololololololololololololololololololololololol"
    
    pad("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus dolor purus, finibus eget magna vel, suscipit semper nibh. Quisque posuere.") ➞ "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus dolor purus, finibus eget magna vel, suscipit semper nibh. Quisque posuere."

### Notes

N/A

"""

def pad(message):
    p = 'ol'*70
    t = len(message)
    if t == 140:
        return message
    elif not t % 2:
        return message+" "+ p[t+1:]
    else:
        return message+p[t:]

