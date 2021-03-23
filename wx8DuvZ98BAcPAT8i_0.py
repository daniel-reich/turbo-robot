"""


There are 3 adjacent slots - L, M and R - which can each hold a number of
discs. L can hold 3 discs, M can hold 2 and L 3. The total number of discs can
vary from 3 to 5, and the discs are numbered 1, 2, 3 and up to 5. From a given
configuration of discs, it is possible to move 1 disc at a time provided the
disc concerned is top of its slot and there is an available slot in the
destination slot.

Write a function which takes 2 parameters (start and end) and returns a tuple
(n, moves) where n is the minimum number of moves needed to move from start to
end and moves is a list of the moves required to effect the changes. start and
end are 8 digit strings where the 1st 3 are slot L, next 2 M and the last 3 R.
Locations are shown from bottom to top within each slot, and empty locations
are represented by 0s. So configuration '15040230' represents disc 5 above 1
in slot L, 4 in slot M and 3 above 2 in slot R. '45000231' encodes 5 above 4
in slot L, an empty slot M and 1 above 3 above 2 in slot R.

A move is a string in the form `<disc>-><slot>`. So to move disc 5 to slot M
you would write "5->M"; 4 to slot R would be "4->R" and 3 to L "3->L". Slots
act like stacks; you can only take the top disc and slots fill up from the
bottom up so you can never have a space below a disc.

### Examples

    move_discs("15040230", "45000231") -> (6,["4->R","5->M","1->M","4->L","1->R","5->L"])
    # "15040230" with "4->R" gives "15000234"
    # "15000234" with "5->M" gives "10050234"
    # "10050234" with "1->M" gives "00051234"
    # "00051234" with "4->L" gives "40051230"
    # "40051230" with "1->R" gives "40050231"
    # "40050231" with "5->L" gives "45000231"

### Notes

  * Start and end will always be valid configurations - you can deduce the number of discs to move from either.
  * There may be more than 1 minimum sequence of moves. To check this, the Code section contains the validate function. This checks that the minimum number of moves have been made and that each is legal and applying them in sequence leads from start of end. You may find it useful for debugging your code as you develop it.
  * If you are unsure how to proceed, the Resources section may provide some pointers.

"""

def move_discs(start, end):
    s_left = start[:3].rstrip('0')
    s_middle = start[3:5].rstrip('0')
    s_right = start[5:].rstrip('0')
    e_left = end[:3].rstrip('0')
    e_middle = end[3:5].rstrip('0')
    e_right = end[5:].rstrip('0')
    s_state = (s_left, s_middle, s_right)
    e_state = (e_left, e_middle, e_right)
    visited = {s_state}
    states = [[s_state, []]]
    n_moves = 0
    while states:
        n_moves += 1
        new_states = []
        for st in states:
            lt, md, rt = st[0]
            moves = st[1]
            len_lt, len_md, len_rt = len(lt), len(md), len(rt)
            if lt != e_state[0][:len_lt] and len_lt:
                if len(md) < 2:
                    new_state = (lt[:-1], md + lt[-1], rt)
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->M'.format(lt[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
                if len(rt) < 3:
                    new_state = (lt[:-1], md, rt + lt[-1])
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->R'.format(lt[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
​
            if md != e_state[1][:len_md] and len_md:
                if len(lt) < 3:
                    new_state = (lt + md[-1], md[:-1], rt)
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->L'.format(md[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
                if len(rt) < 3:
                    new_state = (lt, md[:-1], rt + md[-1])
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->R'.format(md[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
​
            if rt != e_state[2][:len_rt] and len_rt:
                if len(lt) < 3:
                    new_state = (lt + rt[-1], md, rt[:-1])
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->L'.format(rt[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
                if len(md) < 2:
                    new_state = (lt, md + rt[-1], rt[:-1])
                    if new_state not in visited:
                        visited.add(new_state)
                        new_moves = moves.copy()
                        new_moves.append('{}->M'.format(rt[-1]))
                        if new_state == e_state:
                            return n_moves, new_moves
                        new_states.append([new_state, new_moves])
        states = new_states
    """We should never get to this point"""
    return 'Not possible to reach the end state from the start state'

