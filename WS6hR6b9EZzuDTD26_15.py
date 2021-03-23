"""


Given a common phrase, return `False` if _any_ individual word in the phrase
contains _duplicate_ letters. Return `True` otherwise.

### Examples

    no_duplicate_letters("Fortune favours the bold.") ➞ True
    
    no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True
    
    no_duplicate_letters("Look before you leap.") ➞ False
    # Duplicate letters in "Look" and "before".
    
    no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
    # Duplicate letters in "apple", "keeps", "doctor", and "away".

### Notes

Letter matches are case-insensitive.

"""

def no_duplicate_letters(phrase):
    phrase = phrase.split()
    for word in phrase:
        for i in range(len(word)):
            if word[i] in word[i+1::]:
                return False
    else:
        return True
​
​
print(no_duplicate_letters("Look before you leap"))

