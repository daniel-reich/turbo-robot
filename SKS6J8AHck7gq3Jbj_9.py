"""


You have a list of strings, each consisting of a **book title** and an
**author's name**.

To illustrate:

    [
      ["   Death of a Salesman - Arthur Miller    "],
      ["   Macbeth - William Shakespeare    "],
      ["    A Separate Peace - John Knowles     "],
      [" Lord of the Flies - William Golding"],
      ["A Tale of Two Cities - Charles Dickens"]
    ]

Create a function that takes a list like the one above and transforms it into
the same format as the one below:

    [
      ["Death of a Salesman", "Arthur Miller"],
      ["Macbeth", "William Shakespeare"],
      ["A Separate Peace", "John Knowles"],
      ["Lord of the Flies", "William Golding"],
      ["A Tale of Two Cities", "Charles Dickens"]
    ]

### Examples

    tidy_books([
      ["     The Catcher in the Rye - J. D. Salinger    "],
      ["    Brave New World - Aldous Huxley   "],
      ["    Of Mice and Men - John Steinbeck    "]
    ]) ➞ [
      ["The Catcher in the Rye", "J. D. Salinger"],
      ["Brave New World", "Aldous Huley"],
      ["Of Mice and Men", "John Steinbeck"]
    ]

### Notes

Some of these entries have excess white space. Remove this white space in your
final output.

"""

def tidy_books(lst):
    final_book_list = []
    for book_info in lst:
        for var in book_info:
            var = var.rstrip().lstrip()
            new_book_info = var.split('-')
            new_book_info[0], new_book_info[1] = new_book_info[0].rstrip(), new_book_info[1].lstrip()
            final_book_list.append(new_book_info)
    return final_book_list

