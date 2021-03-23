"""


Write a function that divides a phrase into word buckets, with each bucket
containing `n` or fewer characters. Only include full words inside each
bucket.

### Examples

    split_into_buckets("she sells sea shells by the sea", 10)
    ➞ ["she sells", "sea shells", "by the sea"]
    
    split_into_buckets("the mouse jumped over the cheese", 7)
    ➞ ["the", "mouse", "jumped", "over", "the", "cheese"]
    
    split_into_buckets("fairy dust coated the air", 20)
    ➞ ["fairy dust coated", "the air"]
    
    split_into_buckets("a b c d e", 2)
    ➞ ["a", "b", "c", "d", "e"]

### Notes

  * Spaces count as one character.
  * Trim beginning and end spaces for each word bucket (see final example).
  * If buckets are too small to hold a single word, return an empty list: `[]`
  * The final goal isn't to return just the words with a length equal (or lower) to the given `n`, but to return the entire given phrase bucketized (if possible). So, for the specific case of "by" the only word with a proper length, the phrase can't be bucketized, and the returned list has to be empty.

"""

def split_into_buckets(phrase, n):
    if type(phrase) != str or type(n) != int:
        return 'Error: Invalid parameter type!'
​
    else:
        words = phrase.split() # split string into words
        numWords = len(words) # get length before changing var
        wordBuckets = []
        bucketedWords = []
​
        for (i, word) in enumerate(words):
            # if any of the words are
            # too big to be 'bucketized'
            # return []
            if len(word) > n:
                return []
​
            # only create bucket if the
            # word has not already been
            # 'bucketized'
            elif (i, word) not in bucketedWords:
                j = i # make a copy of counter
​
                # while loop condition
                # string of words that
                # can be grouped into
                # a 'bucket' of size n
                wordBucket = []
                wordBucketLen = 0
​
                while j < numWords and wordBucketLen <= n:
                    # metadata for where the word
                    # was found to exclude
                    # duplicate words
                    word = words[j]
​
                    bucketedWords.append((j, word))
                    wordBucket.append(word)
​
                    # length word bucket joined by
                    # whitespace + length of next
                    # word + extra whitespace
                    # only calculate when j
                    # is not the last index
                    # to avoid error
                    if j != (numWords - 1):
                        wordBucketLen = len(' '.join(wordBucket)) + len(words[j + 1]) + 1
​
                    j += 1 # increment
​
                wordBucket = ' '.join(wordBucket) # join to string
                wordBuckets.append(wordBucket)
​
        return wordBuckets

