"""


Write three **regular expressions** that will be passed to `re.match()` in
order to test a password strength:

  * One called `invalid` that will match a password if it's **shorter than 6 characters** or **longer than 30 characters** , if it contains **any disallowed characters** , or if it does **not** contain **at least one** character from each category.
  * One called `weak` that will match a **valid** password that is _either_ **between 6 and 15 characters long** _or_ contains **less than three** characters from each category.
  * One called `strong` that will match a **valid** password **between 16 and 30 characters long** and containing **at least three** character from each category.

### Categories

  *  **Lowercase** : all lowercase letters from "a" to "z".
  *  **Uppercase** : all uppercase letters from "A" to "Z".
  *  **Numbers** : all digits from 0 to 9.
  *  **Symbols** : all of the following symbols `!"#$%&'()*+,-./:;<=>?@[\]^_\{|}`

### Disallowed Characters

Spaces, tabs, line breaks and any other character that doesn't belong in one
of the four categories.

### Example

    # There are four invalid, four weak and four strong passwords (in that order).
    
    passwords = [
        r'a3%Z',
        r'qwerty123456666666666666666666',
        r'sjfajfewjrjiodjfsrw0998(*(8q9432-4dfjsoijfj3))',
        r'this is an   invalid password',
        r'3d/-\b1T',
        r'This1s4VeryVeryl0n6Pa$$word',
        r'AAaa11&&',
        r'yFtZaqR%eN3nsu8VvxqK!LDfxbCnj',
        r'S*=7v!7rM5k!H+)@',
        r'H#4qq2_j[T|R!(7:;.aT',
        r'AP6&Ju~=ec<?"zj#8frDq=\3{%^P$',
        r"1111aaaaA^AA;;;1111aaaaAAAA;;'"
    ]
    
    invalid = "yourregularexpressionhere"
    weak = "yourregularexpressionhere"
    strong = "yourregularexpressionhere"
    
    [bool(re.match(invalid, i)) for i in passwords] ➞ [True, True, True, True, False, False, False, False, False, False, False, False]
    [bool(re.match(weak, i)) for i in passwords] ➞ [False, False, False, False, True, True, True, True, False, False, False, False]
    [bool(re.match(strong, i)) for i in passwords] ➞ [False, False, False, False, False, False, False, False, True, True, True, True]

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx in **Resources**.
  * You can find all the challenges of this series [here](https://edabit.com/collection/8geJw3tgpm5LDAxwR).

"""

import re
​
invalid1 = '.{31}'   ##  greater than 30 characters
invalid2 = '|.{0,4}.$'   ##  or less than 6 greaters 
specchars = "\!\(\)\*\+\[\-\\\\'#$%&,./:;?@\\]^_{|}<=>-"
invalid3   = "|(?!.*[" + specchars + "].*)"   ## no special characters
invalid4 = '|(?!.*[a-z].*)'                   ## no lower case characters
invalid5 = '|(?!.*[A-Z].*)'  ## no upper case alpha
invalid6 = '|(?!.*[0-9].*)'  ## no numbers
invalid = invalid1 + invalid2 + invalid3 +  invalid4 + invalid5 + invalid6
weak1 = '.{6,15}$'  ## length of 6 - 15
weak2 = '(?=[^a-z]*[a-z][^a-z]*[a-z]{0,1}[^a-z]*$)'     ## has 1 or 2 lower case characters (not 3)
weak3 = '(?=[^A-Z]*[A-Z][^A-Z]*[A-Z]{0,1}[^A-Z]*$)'     ## has 1 or 2 Upper case characters (not 3)
weak4 = '(?=[^0-9]*[0-9][^0-9]*[0-9]{0,1}[^0-9]*$)'     ## has 1 or 2 numbers (not 3 )
weak5a = '[' + specchars + ']'
weak5b = '[^' + specchars + ']*'
weak5 = '(?=' + weak5b + weak5a + weak5b + weak5a + '{0,1}' + weak5b + '$)' 
    ## has 1 or 2 special characters (not 3)
weak =  weak1 +  "|" + '(?=.{6,30}$)'  + "(" + weak2 + "|" + weak3 + "|" + weak4 + "|" + weak5  + ')'
 
strong1 = '(?=.{16,30}$)'    ## lenth of 16 - 30
strong2 = '(?=.*[a-z][^a-z]*[a-z][^a-z]*[a-z])'     ## has 3 or more lower case characters
strong3 = '(?=.*[A-Z][^A-Z]*[A-Z][^A-Z]*[A-Z])'     ## has 3 or more Upper case characters
strong4 = '(?=.*[0-9][^0-9]*[0-9][^0-9]*[0-9])'     ## has 3 or more numbers
strong5a = '[' + specchars + ']'
strong5b = '[^' + specchars + ']*'
strong5 = '(?=.*'  + strong5a + strong5b + strong5a + strong5b + strong5a + ')'
    ## has 1 or 2 special characters   
strong =  strong1 +   strong2 + strong3 + strong4 + strong5

