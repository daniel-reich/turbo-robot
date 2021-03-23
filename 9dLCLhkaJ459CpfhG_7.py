"""


Write a regular expression that matches numbers whose digits are not repeated
(i.e. digits are distinct).

### Examples

    pattern = "yourregularexpressionhere"
    
    bool(re.match(pattern, "123")) ➞ True
    
    bool(re.match(pattern, "112233")) ➞ False
    
    bool(re.match(pattern, "1025")) ➞ True

### Notes

  * You **don't** need to write a function, just the pattern.
  * Input is a number as a string.
  * Find more info on RegEx in **Resources**.
  * You can find all the challenges of this series [here](https://edabit.com/collection/8geJw3tgpm5LDAxwR).

"""

pattern = r'(?:(\d)(?!.*\1))+'

