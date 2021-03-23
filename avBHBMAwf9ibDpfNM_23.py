"""


Write a function that makes an HTTP GET request for the given `url`. Return
the media type / content-type from the HTTP Response Header as a string.

### Example

    content_type("https://edabit.com") ➞ "text/html; charset=utf-8"

### Notes

  * You may want to make use of and import `requests`.
  * Do not cheat and just print out the answer, you must fetch this from edabit.com.
  * Return the output as a string.

"""

import requests
def content_type(url):
  r = requests.get(url)
  return r.headers.get('content-type')

