"""


Create a function that is a Hashtag Generator by using the following rules:

  * The output must start with a hashtag (#).
  * Each word in the string must have its first letter capitalized.
  * If the final result, a single string, is longer than 140 characters, the function should return `false`.
  * If either the input (`str`) or the result is an empty string, the function should return `false`.

### Examples

    generate_hashtag("    Hello     World   " ) ➞ "#HelloWorld"
    
    generate_hashtag("") ➞ false, "Expected an empty string to return false"
    
    generate_hashtag("Edabit Is Great") ➞ "#EdabitIsGreat", "Should remove spaces."

### Notes

N/A

"""

def generate_hashtag(astring):
    if astring.strip() == '':
        return False
    else:
        updated_string = astring.strip()
        emptystring = ''
        split_updated_string = updated_string.split(' ')
        for eachword in split_updated_string:
            emptystring += eachword.capitalize()
        final_string = "#" + emptystring
        return final_string if len(final_string) < 140 else False

