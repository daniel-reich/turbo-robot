"""


Write a function that retrieves all words that begin with a vowel.

### Examples

    retrieve("A simple life is a happy life for me.") ➞ ["a", "is", "a"]
    
    retrieve("Exercising is a healthy way to burn off energy.")
    ➞ ["exercising", "is", "a", "off", "energy"]
    
    retrieve("The poor ostrich was ostracized.")
    ➞ ["ostrich", "ostracized"]
    
    retrieve("")
    ➞ []

### Notes

  * Make all words lower case in the output.
  * Retrieve the words in the order they appear in the sentence.

"""

def retrieve(txt):
    lst_wovels = []
    if txt.endswith('.'):
        new_txt =txt[:-1]
    else:
        new_txt = txt
    for word in new_txt.split():
        lower_word = word.lower()
        if lower_word[0] in 'aeiou':
            lst_wovels.append(lower_word)
    return lst_wovels
​
​
​
print(retrieve("Exercising is a healthy way to burn off energy"))

