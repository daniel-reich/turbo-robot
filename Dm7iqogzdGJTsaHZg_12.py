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

def retrieve(text):
    vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U']
    res_list = []
    lst = []
​
    if text != "":
        lst = text.split(" ")
        for item in lst:
            if item[0] in vowels:
                new_item = item.replace(".", "")
                res_list.append(new_item.lower())
        return res_list
    else:
        return res_list

