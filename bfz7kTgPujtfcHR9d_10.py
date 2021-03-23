"""


Create a function which replaces all the x's in the string in the following
ways:

Replace all x's with "cks" **UNLESS** :

  * The word begins with "x", therefore replace it with "z".
  * The word is just the letter "x", therefore replace it with "ecks".

### Examples

    x_pronounce("Inside the box was a xylophone") ➞ "Inside the bocks was a zylophone"
    
    x_pronounce("The x ray is excellent") ➞ "The ecks ray is eckscellent"
    
    x_pronounce("OMG x box unboxing video x D") ➞ "OMG ecks bocks unbocksing video ecks D"

### Notes

  * All x's are lowercase.
  * I know that not all words with x's follow this rule, but there are too many edge cases to count!

"""

def x_pronounce(sentence):
    sentence_list=sentence.split(" ")
    modified_sentence=""
    
    for word in sentence_list:
        if "x" in word:
            if len(word) == 1:
                word = word.replace("x", "ecks")
​
            elif word.index("x") == 0:
                word = word.replace("x", "z")
​
            else:
                word = word.replace("x", "cks")
        modified_sentence = modified_sentence.lstrip() + " " + word
        
    return modified_sentence

