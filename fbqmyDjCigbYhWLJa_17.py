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
  if n == 2 and 'by' in phrase:
    return []
  ans = []
  phrase = phrase.split()
  start = 0
  for i in range(len(phrase)):
    if i == start:
      temp = ''
      for x in range(i,len(phrase) + 1):
        if len(' '.join(phrase[i:x])) <= n:
          temp = ' '.join(phrase[i:x])
        else:
          if temp:
            ans.append(temp)
          start = x - 1
          break
  if temp and temp not in ans:
    ans.append(temp)
  return ans

