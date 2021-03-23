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

def strip_url_params(url, params_to_strip = []):
  if '?' not in url:
    return url
  ind = url.index('?')
  end = url[ind+1:]
  pts = end.split('&')
  left = {}
  for pt in pts:
    if pt[0] not in params_to_strip:
      left[pt[0]] = pt[-1]
  l = [k + '=' + v for k,v in left.items()]
  l.sort()
  s = '&'.join(l)
  lr = url[:ind+1] + s
  return lr

