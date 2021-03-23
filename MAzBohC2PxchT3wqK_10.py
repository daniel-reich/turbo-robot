"""


Given two sentences, return whether they are shadows of each other. This means
that all of the word lengths are the same, but the corresponding words don't
share any common letters.

### Examples

    shadow_sentence("they are round", "fold two times") ➞ True
    
    shadow_sentence("own a boat", "buy my wine") ➞ False
    # No words share common letters, but "a" and "my" have different lengths.
    
    shadow_sentence("his friends", "our company") ➞ False
    # Word lengths are the same but "friends" and "company" share the letter "n".
    
    shadow_sentence("salmonella supper", "birthright") ➞ False
    # Setences with different numbers of words.

### Notes

  * All sentences will be given in lowercase, and will have no punctuation.
  * Return `False` if the sentences have different numbers of words.

"""

def shadow_sentence(sentenceone,sentencetwo):
    sentenceone = sentenceone.split(' ')
    sentencetwo = sentencetwo.split(' ')
    for i in range(len(sentenceone)):
        try:
            if word_length(sentenceone[i]) != word_length(sentencetwo[i]):
                return False
            elif share_letters(sentenceone[i],sentencetwo[i]):
                return False
        except Exception as e:
            return False
    return True
​
​
def word_length(eachword):
    return len(eachword)
​
​
def share_letters(word1,word2):
    for eachletter in set(list(word1)):
        if eachletter in word2:
            return True
    return False

