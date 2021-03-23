"""


Write a function that takes an integer and:

  * If the number is a multiple of 3, return `"Hello"`.
  * If the number is a multiple of 5, return `"World"`.
  * If the number is a multiple of both 3 and 5, return `"Hello World"`.

### Examples

    hello_world(3) ➞ "Hello"
    
    hello_world(5) ➞ "World"
    
    hello_world(15) ➞ "Hello World"

### Notes

Don't forget to `return` the result.

"""

hello_world=lambda n:'Hello World' if not(n%5 or n%3) else 'Hello' if not(n%3) else 'World'

