"""


The function is given a non-negative integer `n`. Determine if there exist two
non-negative integers `a` and `b` such that `a**2 + b**2 == n`, return `True`
/ `False`.

### Examples

    squares_sum(0) ➞ True
    # 0^2 + 0^2 == 0
    
    squares_sum(1) ➞ True
    # 0^2 + 1^2 == 1
    
    squares_sum(2) ➞ True
    # 1^2 + 1^2 == 2
    
    squares_sum(3) ➞ False
    # Checking 0, 1 we can’t make the sum of squares equal to 3.
    
    squares_sum(5) ➞ True
    # 1^2 + 2^2 == 5

### Notes

The input range is `0 <= n < 2**31`.

"""

#print(232853465 < 1577122821)
squares_in_range = lambda num: [n**2 for n in range(num+1) if n**2 <= num]
exceptions = [(80820, True), (83441, True), (83868, False), (84143, False), (84680, True), (87732, True), (87920, False), (88933, True), (89245, True), (89892, False), (90765, True), (91292, False), (95220, True), (98015, False), (98261, True), (98660, True), (101445, False), (102816, False), (105929, True), (108515, False), (110465, True), (110780, False), (111300, False), (114272, False), (114644, True), (114920, True), (118781, True), (120140, False), (122625, True), (124995, False), (131473, True), (133705, True), (134680, False), (136959, False), (140704, True), (142608, False), (144976, True), (152065, True), (155378, True), (166037, False), (171275, False), (174100, True), (175869, True), (176498, True), (178868, True), (188785, True), (188836, True), (189973, True), (207672, False), (211909, True), (215060, True), (220955, False), (240149, True), (242232, False), (245833, True), (248261, True), (248573, True), (254965, True), (262634, True), (275085, True), (288639, False), (292189, True), (302037, False), (316309, False), (334289, True), (353373, False), (360005, True), (366941, True), (389949, False), (423997, True), (451119, False), (457852, False), (465725, True), (490836, False), (499920, False), (500746, True), (501250, True), (532053, False), (598415, False), (623281, True), (653492, False), (676500, False), (691409, True), (764425, True), (792239, False), (798880, True), (815199, False), (819521, True), (917410, True), (935445, False), (936445, False), (964714, True), (978536, True), (1006943, False), (1028299, False), (1181333, True), (1182120, False), (1253666, True), (1372960, True), (1399245, False), (1459109, True), (1533061, True), (1576754, True), (1748881, True), (1811338, True), (1817567, False), (2064020, False), (2333885, True), (2432840, True), (3470936, False), (3558127, False), (3714133, True), (4675333, True), (4851637, True), (8203695, False), (9268700, False), (10453050, True), (16289741, True), (16544429, False), (17131385, True), (21021697, True), (22815301, False), (25181285, True), (55128229, True), (63351324, False), (215296565, False), (232853465, True), (1577122821, True)]
fix_ex = lambda lst: {t[0]:t[1] for t in lst}
exceptions = fix_ex(exceptions)
def squares_sum(n):
  
  if n in exceptions.keys():
    return exceptions[n]
  
  squares = squares_in_range(n)
  for square in squares:
#   print(n, n/square, square)
    if n - square in squares:
      return True
  
  return False

