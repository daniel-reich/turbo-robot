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
  words = phrase.split(" ")
  idx, r = 0, [ ]
  while idx < len( words ) :
      s, j = words[ idx ], 1 
      if len( s ) > n :
          return []
      while len( s ) < n and idx + j < len( words ) :
          if len( s + " " + words[ idx + j ] ) > n :
              break
          s = s + " " + words[ idx + j ]
          j += 1
      r.append( s )
      idx += j 
  return r
​
​
​
​
  words = phrase.split(" ")
  idx = 0
  r = [ ]
  while idx < len(words) :
    if len( words[ idx ] ) > n :
      return []
    s = words[idx]
    j = 1
    while len( s ) < n :
      if len( s + " " + words[ idx + j ] ) <= n :
        s = s + " " + words[ idx + j ]
        j = j + 1
    r.append( s )
    idx = idx + j 
  return r

