"""


Create a function that takes in two positive integers `start` and `n` and
returns a list of the first `n` terms of the **look-and-say sequence**
starting at the given `start`.

Each term of the look-and-say sequence (except for the first term) is created
from the previous term using the following process.

Start with a term in the sequence (for example, 111312211):

    111312211

Split it into subsequences of consecutive repeating digits:

    111 3 1 22 11

Count the number of digits in each subsequence:

    three 1, one 3, one 1, two 2, two 1

Turn everything into digits:

    3 1, 1 3, 1 1, 2 2, 2 1

Now combine everything into one number:

    3113112221

So 3113112221 is the next term in the sequence after 111312211.

### Examples

    look_and_say(1, 7) ➞ [1, 11, 21, 1211, 111221, 312211, 13112221]
    
    look_and_say(123, 4) ➞ [123, 111213, 31121113, 1321123113]
    
    look_and_say(70, 5) ➞ [70, 1710, 11171110, 31173110, 132117132110]

### Notes

Your output should be a list of integers.

"""

def look_and_say(start,n):
    '''
    Returns a list of the 1st n terms in the look-and-say sequence commencing
    with start - rules as per instructions
    '''
    def gen_term(term):
        '''
        Returns the next term from term in look-and-say
        '''
        term = str(term)
        chunk = term[0]  # 1st digit
        chunks = []
        i = 1
​
        while i < len(term):
            if term[i] == term[i-1]:
                chunk += term[i]  # build up sequence
            else:
                chunks.append(chunk)
                chunk = term[i]  # write away chunk and start new one
            i+= 1
        chunks.append(chunk)  # last sequence
​
        return int(''.join(str(c.count(c[0]))+c[0] for c in chunks))
​
    terms = [start]
    term = start
    for _ in range(n-1):
        term = gen_term(term)
        terms.append(term)
​
    return terms

