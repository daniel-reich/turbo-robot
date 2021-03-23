"""


Create a function which **replaces** all instances of `"nts"` with `"nce"` and
**vice versa** if they are at the _end of a word_.

### Examples

    switcheroo("The elephants in France were chased by ants!") ➞ "The elephance in Frants were chased by ance!"
    
    switcheroo("While he rants, I fall into a trance...") ➞ "While he rance, I fall into a trants..."
    
    switcheroo("Bounced over the fence!") ➞ "Bounced over the fents!"

### Notes

  * Empty strings should return just an empty string (see example #2).
  * Ignore punctuation and any instances where `"nts"` or `"nce"` are not at the end of a word (see example #3).

"""

def switch(word):
    '''
    Replaces the end of a word - ignoring punctuation - by 'nts' if it is 'nce'
    and vice versa then returns it.
    '''
    alpha_word = ''.join([l for l in word if l.isalpha()])
    if alpha_word.endswith('nce'):
        alpha_word = alpha_word[:-3] + 'nts'
    elif alpha_word.endswith('nts'):
        alpha_word = alpha_word[:-3] + 'nce'
​
    return alpha_word + word[len(alpha_word):]  # restore any punctuation
        
                         
def switcheroo(sentence):
    '''
    Returns sentence with 'nts' replaced by 'nce' and vice versa if they are at
    the end of a word as per the instructions.
    '''
    return ' '.join(switch(word) for word in sentence.split())

