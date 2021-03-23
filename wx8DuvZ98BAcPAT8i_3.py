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

def get_string(L, M, R):
    ans = ''.join(L)
    while len(ans) < 3:
        ans += '0'
    ans += ''.join(M)
    while len(ans) < 5:
        ans += '0'
    ans += ''.join(R)
    while len(ans) < 8:
        ans += '0'
    return ans
​
def move_discs(start, end):
    L, M, R = [], [], []
    for i in range(3):
        if start[i] != '0':
            L.append(start[i])
    for i in range(2):
        if start[3+i] != '0':
            M.append(start[3+i])
    for i in range(3):
        if start[5+i] != '0':
            R.append(start[5+i])
    queue = [[L[:], M[:], R[:], []]]
    seen = set((tuple(L), tuple(M), tuple(R)))
    while True:
        L, M, R, moves = queue.pop(0)
        seen.add((tuple(L), tuple(M), tuple(R)))
        if len(L) > 0:
            disc = L[-1]
            if len(M) < 2:
                new_L, new_M, new_R, new_moves = L[:-1], M + [disc], R[:], moves + [disc + "->M"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])
            if len(R) < 3:
                new_L, new_M, new_R, new_moves = L[:-1], M[:], R + [disc], moves + [disc + "->R"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])
        if len(M) > 0:
            disc = M[-1]
            if len(L) < 3:
                new_L, new_M, new_R, new_moves = L + [disc], M[:-1], R[:], moves + [disc + "->L"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])
            if len(R) < 3:
                new_L, new_M, new_R, new_moves = L[:], M[:-1], R + [disc], moves + [disc + "->R"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])
        if len(R) > 0:
            disc = R[-1]
            if len(M) < 2:
                new_L, new_M, new_R, new_moves = L[:], M + [disc], R[:-1], moves + [disc + "->M"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])
            if len(L) < 3:
                new_L, new_M, new_R, new_moves = L + [disc], M[:], R[:-1], moves + [disc + "->L"] 
                if get_string(new_L, new_M, new_R) == end:
                    return (len(new_moves), new_moves)
                if (tuple(new_L), tuple(new_M), tuple(new_R)) not in seen:
                    queue.append([new_L, new_M, new_R, new_moves])

