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

from collections import OrderedDict
def strip_url_params(url, params_to_strip=[]):
  # Get search parameters
    try:
        params = url[url.index('?'):]
    except ValueError:
        return url
    params = params[1:].split('&')
    p_dic = OrderedDict()
    for p in params:
        p = p.split('=')
        p_dic[p[0]] = p[1]
    for para in params_to_strip:
        if para in p_dic.keys():
            del(p_dic[para])
    param_string = '?' + '&'.join([key + '=' + value for key, value in p_dic.items()])
    return url[:url.index('?')] + param_string

