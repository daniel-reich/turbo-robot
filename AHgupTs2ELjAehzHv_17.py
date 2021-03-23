"""


Write three **regular expressions:**

  * One called `opening_tags` that will match all HTML opening tags including attributes.
  * One called `closing_tags` that will match all HTML closing tags.
  * One called `all_tags` that will match all HTML tags opening or closing, their attributes and **their content** (as long as their content is in the same line). Please, check the example below to see the expected result.

### Example

    index = '''
    <html>
    <head>
        Hi! I'm a text in the head.
        I probably shouldn't be here.
        <title>edabit.com</title>
    </head>
    <body>
        Hi! I'm a text in the body.
        <p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>
        Here comes a fake tag: <>.
    </body>
    </html>
    '''
    
    opening_tags = "yourregularexpressionhere"
    closing_tags = "yourregularexpressionhere"
    all_tags = "yourregularexpressionhere"
    
    re.findall(opening_tags, index) ➞ ["<html>", "<head>", "<title>", "<body>", "<p>", "<a href="https://edabit.com">"]
    
    re.findall(closing_tags, index) ➞ ["</title>", "</head>",  "</a>", "</p>", "</body>", "</html>"]
    
    re.findall(all_tags, index) ➞ ["<html>", "<head>", "<title>edabit.com</title>", "</head>", "<body>", "<p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>", "</body>", "</html>"]

### Notes

  * You **don't** need to write a function, just the pattern.
  * Do **not** remove `import re` from the code.
  * Find more info on RegEx in **Resources**.
  * You can find all the challenges of this series in my [Basic RegEx](https://edabit.com/collection/8PEq2azWDtAZWPFe2) collection.

"""

import re
​
opening_tags = "<[^/].*?>"
closing_tags = "</.*?>"
all_tags = "<.+>"

