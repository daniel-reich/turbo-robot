"""


Write a function that will return the **longest word** in a sentence. In cases
where more than one word is found, return the first one.

### Examples

    find_longest("A thing of beauty is a joy forever.") ➞ "forever"
    
    find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"
    
    find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"

### Notes

  * Special characters and symbols _don't count_ as part of the word.
  * Return the longest word found in **lowercase** letters.
  * A recursive version of this challenge can be found in [here](https://edabit.com/challenge/LyzKTyYdKF4oDf5bG).

"""

def find_longest(sentence):
    result_list = sentence.split()
    max_word = ''
    current_word = ''
    for word in result_list:
        for i in range(len(word)):
            if not word[i].isalpha():
                current_word = word[:i]
                break
            else:
                current_word = word
​
        if len(current_word) >= len(max_word):
            max_word = current_word
        current_word = ''
​
    return max_word.lower()

