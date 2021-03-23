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
    lst = sentence.split()
    for i, w in enumerate(lst):
        if w == 'x':
            lst[i] = 'ecks'
        elif w[0] == 'x':
            lst[i] = 'z' + w[1:]
        if 'x' in lst[i]:
            lst[i] = w.replace('x', 'cks')
    return ' '.join(lst)

