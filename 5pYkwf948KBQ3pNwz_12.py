"""


This challenge requires you to find the most common words. There will be two
leyword arguments passed in `text` and `n`. Return the most common words in
the form of a dictionary.

`text` would be the variable containing all the words, while `n` is a number
that means _return the top`n` most common words_ from `text`. In case `n`
exceeds the total number of unique words, return the full dictionary of most
common words.

`text` will only contain letters, spaces, and basic punctuation like
fullstops, commas, exclamation marks, question marks and apostrophes, which
means you would have to split the text into words as well.

In the case of an apostrophe: _"where's"_ would be considered as two words,
_"where"_ and _"s"_ , and _"I'm"_ would be _"i"_ and _"m"_.

All words in the returned dictionary should be lower case.

### Examples

    words = "How much wood could a woodchuck chuck If a woodchuck could chuck wood? As much wood as a woodchuck could chuck, If a woodchuck could chuck wood"
    
    most_common_words(text=words, n=3) ➞ {
      "wood": 4,
      "could": 4,
      "a": 4
    }
    
    most_common_words(text=words, n=7) ➞ {
      "wood": 4,
      "could": 4,
      "a": 4,
      "woodchuck": 4,
      "chuck": 4,
      "much": 2,
      "if": 2
    }
    
    most_common_words(text=words, n=999) ➞ {
      "wood": 4,
      "could": 4,
      "a": 4,
      "woodchuck": 4,
      "chuck": 4,
      "much": 2,
      "if": 2,
      "as": 2,
      "how": 1
    }

### Notes

In the case of duplicate values (eg. { "word1": 1, "word2": 1 }), their order
of appearance should follow their position in the text.

For example:

    most_common_words("word1, word2", 1) ➞ { "word1": 1 }
    most_common_words("word2, word1", 1) ➞ { "word2": 1 }

"""

def most_common_words(text,n):
    '''
    Returns a dictionary of the n most common words in text as per
    instructions
    '''
    tidy_up = lambda x: x.lower().replace('.','').replace(',','').replace('?','')\
              .replace('!','')
​
    words = [(tidy_up(w),i) for i,w in enumerate(text.replace("'",' ').split())]
    freqs = {}
    for word in words[::-1]:
        entry = freqs.get(word[0],(0,0))
        freqs[word[0]] = (entry[0]+1,word[1])
​
    freqs = sorted(freqs.items(),key=lambda x:(-x[1][0],x[1][1]))[:n]
    return {w[0]:w[1][0] for w in freqs}

