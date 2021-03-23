"""


Create a `Book` **class** that has **two attributes** :

  1. `.title`
  2. `.author`

and **two methods** :

  1. A method named `.get_title()` that returns: `"Title: "` \+ the instance title.
  2. A method named `.get_author()` that returns: `"Author: "` \+ the instance author.

and instantiate this class by creating 3 new books:

  1. Pride and Prejudice - Jane Austen ( **PP** )
  2. Hamlet - William Shakespeare ( **H** )
  3. War and Peace - Leo Tolstoy ( **WP** )

Name the new instances should be **PP** , **H** , and **WP** , respectively.

For instance, if I instantiated the following book using this `Book` class:

  * Harry Potter - J.K. Rowling (HP)

I would get the following attributes and methods:

### Examples

    HP.title ➞ "Harry Potter"
    HP.author ➞ "J.K. Rowling"
    HP.get_title() ➞ "Title: Harry Potter"
    HP.get_author() ➞ "Author: J.K. Rowling"

### Notes

  * Read more about Python classes in **Resources**.
  * Remember, after you've finished writing the **class** and its **methods** , you must instantiate it through the creation of new objects.

"""

class Book:
  # Write your attributes and methods here
  def __init__(self, title, author):
    self.title = title
    self.author = author
  
  def get_title(self):
    return 'Title: ' + self.title
  
  def get_author(self):
    return 'Author: ' + self.author
​
  # Instantiate your Book class here
PP = Book('Pride and Prejudice', 'Jane Austen')
H = Book('Hamlet', 'William Shakespeare')
WP = Book('War and Peace', 'Leo Tolstoy')

