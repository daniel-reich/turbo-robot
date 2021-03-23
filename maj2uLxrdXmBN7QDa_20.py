"""


Your chess teacher wants to know if a bishop can reach a certain spot on the
board in the given amount of moves.

Given a starting square `start`, ending square `end` and the maximum number of
moves allowed `n`. Return `True` if the ending square can be reached from the
starting square within the given amount of moves. Keep in mind the chessboard
goes from a1 to h8 (8x8).

### Examples

    bishop("a1", "b4", 2) ➞ True
    
    bishop("a1", "b5", 5) ➞ False
    
    bishop("f1", "f1", 0) ➞ True

### Notes

  * Chessboard is always empty (only the bishop is there).
  * Bishop can move in any direction diagonally.
  * If the starting and ending square are the same, return `True` (even if the move is 0).
  * Square names will always be lowercase and valid.

"""

def bishop(start, end, n):
    field_ids = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ], [1, 2, 3, 4, 5, 6, 7, 8]))
​
    # case 1 - zero ruchow
    if n == 0:
        if start == end:
            return True
        return False
​
    start_id_add = field_ids[list(start)[0]] + int(list(start)[1])
    end_id_add = field_ids[list(end)[0]] + int(list(end)[1])
    start_id_sub = field_ids[list(start)[0]] - int(list(start)[1])
    end_id_sub = field_ids[list(end)[0]] - int(list(end)[1])
​
    # case 2 - inny kolor pol start i end
    if start_id_add % 2 != end_id_add % 2:
        return False
​
    # case 3 - 1 ruch, ten sam kolor, przekatna \
    if n == 1 and start_id_add == end_id_add:
        return True
​
    # case 4 - 1 ruch, ten sam kolor, przekatna /
    if n == 1 and start_id_sub == end_id_sub:
        return True
    
    if n == 1:
        return False
    
    # case 5 - wicej niz 1 ruch i ten sam kolor
    return True

