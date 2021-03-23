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

def strip_url_params(url, params_to_strip=None):
  if params_to_strip == None:
    params_to_strip = []
  l = url[19:].split("&")[::-1]
  appeared = []
  answer = []
  if l[0] != "":
    for el in l:
      if appeared.count(el[0]) == 0 and params_to_strip.count(el[0])==0:
        appeared.append(el[0])
        answer.append(el)
    if len(answer) > 0:
      answer.sort()
      output = "https://edabit.com?" + answer[0]
      for el in answer[1:]:
        output += "&" + el
    else:
      output = "https://edabit.com"
    return output
  else:
    return "https://edabit.com"

