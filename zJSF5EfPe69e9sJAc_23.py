"""


Create a function that takes a string `txt` and censors any word from a given
list `lst`. The text removed must be replaced by the given character `char`.

### Examples

    censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
    
    censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
    
    censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"

### Notes

N/A

"""

def censor_string(txt, lst, char):
    new=txt.split(" ")
    new_string=[]
    for word in new:
        for censor in lst:
            if word == censor:
                word=list(word)
                for n in range(len(word)):
                    word[n]=char
            word="".join(word)
        new_string.append(word)
    return " ".join(new_string)

