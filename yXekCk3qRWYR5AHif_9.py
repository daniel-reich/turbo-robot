"""


Write a function, that replaces all vowels in a string with a specified vowel.

### Examples

    vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
    
    vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"
    
    vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"

### Notes

All words will be lowercase. Y is not considered a vowel.

"""

def vow_replace(word, vowel):
    set1 = set(['a','i','o','e','u'])
    for it1 in word:
        set2 = set(it1)
        if set2.issubset(set1):
            word = word.replace(it1, vowel)
    return word
