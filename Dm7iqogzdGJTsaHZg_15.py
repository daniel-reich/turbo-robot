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
    vowels = 'aeiou'
    result_lst = []
    txt.lower()
    lst = txt.lower().split(' ')
    if len(txt) == 0:
        return([])
    for i in lst:
        if i[0] in vowels and i[-1] != '.':
            result_lst.append(i)
        elif i[0] in vowels and i[-1] == '.':
            result_lst.append(i[:-1])
    return(result_lst)

