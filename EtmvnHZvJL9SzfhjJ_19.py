"""


Create a function that takes a URL (string), removes duplicate query
parameters and parameters specified within the 2nd argument (which will be an
_optional_ list).

### Examples

    strip_url_params("https://edabit.com?a=1&b=2&a=2") ➞ "https://edabit.com?a=2&b=2"
    
    strip_url_params("https://edabit.com?a=1&b=2&a=2", ["b"]) ➞ "https://edabit.com?a=2"
    
    strip_url_params("https://edabit.com", ["b"]) ➞ "https://edabit.com"

### Notes

  * The 2nd argument `params_to_strip` is optional.
  * `params_to_strip` can contain multiple params.
  * If there are duplicate query parameters with different values, use the value of the last occurring parameter (see examples #1 and #2 above).

"""

def strip_url_params(url, params_to_strip=[]):
    if '?' not in url:
        return url
    result,s2 = url.split('?')
    result += '?'
    s2 = [i.split('=') for i in s2.split('&')]
    d = {i[0]:i[1] for i in s2}
    for i in sorted(d.keys()):
        if i not in params_to_strip:
            result += '{}={}&'.format(i,d[i])
    return result[:-1]

