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
    '''
    Returns a list of the words in phrase split into buckets of max size n as
    per instructions, or an empty ;ist if this is not possible
    '''
    words = phrase.split()
    if len(max(words, key=len)) > n:
        return []
​
    size = len(words)
    i = 0
    buckets = []
    bucket = ''
    space = ''
​
    while i < size:
        while i < size and (len(bucket) + len(space) + len(words[i])) <= n:
            bucket = bucket + space + words[i]
            #print('bucket', bucket, 'length', len(bucket))
            space = ' '
            i += 1
​
        if i < size:
            buckets.append(bucket)
            space = ''
            bucket = ''
            
    if bucket:
        buckets.append(bucket)  #last bucket!
​
    return buckets

