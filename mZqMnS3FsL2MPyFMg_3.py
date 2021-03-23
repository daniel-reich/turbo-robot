"""


Write a function that accepts a positive integer between `0` and `999`
inclusive and returns a string representation of that integer written in
English.

### Examples

    num_to_eng(0) ➞ "zero"
    
    num_to_eng(18) ➞ "eighteen"
    
    num_to_eng(126) ➞ "one hundred twenty six"
    
    num_to_eng(909) ➞ "nine hundred nine"

### Notes

  * There are no hyphens used (e.g. "thirty five" not "thirty-five").
  * The word "and" is not used (e.g. "one hundred one" not "one hundred and one").

"""

"""
NOTE: I first completed this challenge for a different site. I've modified my answer to make it work here.
​
Consider this number:
​
123_426_112
one hundred twenty three million four hundred twenty six thousand one hundred twelve
​
It has three groups:
hne hundred twenty three million
four hundred twenty six thousand
one hundred twelve
​
Another way to think of this is to write it as:
​
num = 123426112
word_string = f'{num // 10**6} million {(num // 1000) % 1000} thousand {num % 1000}'
print(word_string)
​
Which outputs:
123 million 426 thousand 112
​
Now, you just need to substitute the written numbers between 1 and 999. Make a
function to do exactly that. When it's done you will have two functions:
​
small_num_in_words()  -- example: 511 --> five hundred eleven
large_num_in_words()  -- example: 123426112 --> 123 million 426 thousand 112
​
Use the first function in the second to get the full result.
"""
​
​
def small_num_in_words(n):
    n_str = str(n).zfill(3)
​
    if n < 0 or n > 999:
        raise ValueError('{} must be between 0 and 999 inclusive.'.format(n))
​
    result = []
​
    tens = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty',
            '9': 'ninety'}
    ones = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
            '9': 'nine'}
​
    if n >= 100:
        result.append(ones.get(n_str[0], '') + ' hundred')
​
    if 10 <= (n % 100) <= 19:
        ten_to_nineteen = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
        result.append(ten_to_nineteen[(n % 100) - 10])
​
    else:
        if n_str[1] != '0':
            result.append(tens.get(n_str[1], ''))
        result.append(ones.get(n_str[2], ''))
​
    return ' '.join(result).strip()
​
​
def num_to_eng(n):
    if n == 10**12:
        return 'one trillion'
​
    if n == 0:
        return 'zero'
​
    n_str = str(n).zfill(12)
    billions = int(n_str[:3])
    millions = int(n_str[3:6])
    thousands = int(n_str[6:9])
    ones_tens_hundreds = int(n_str[9:12])
​
    result = ''
    if billions:
        result += '{} billion'.format(small_num_in_words(billions))
    if millions:
        result += ' {} million'.format(small_num_in_words(millions))
    if thousands:
        result += ' {} thousand'.format(small_num_in_words(thousands))
    if ones_tens_hundreds:
        result += ' ' + small_num_in_words(ones_tens_hundreds)
​
    return ' '.join(result.split())

