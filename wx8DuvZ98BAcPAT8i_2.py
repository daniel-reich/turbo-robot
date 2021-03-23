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

def validate(start, end, num, answer):
    '''
    Validates solutions to move_discs. Checks that num matches answer[0], and
    the moves in answer[1] lead validly from config start to end.
    DO NOT REMOVE OR EDIT
    '''
    L =('L', 2,0); M = ('M', 4,3); R = ('R', 7, 5)  # slots:name, top idx, low idx
    discs = ''.join(d for d in start if d != '0') # valid disc numbers
    
    try:
        assert len(answer) == 2 and isinstance(answer[0],int) and isinstance(answer[1],list),\
        'Malformed answer: should be (int, list)'
        num1, moves = answer
        assert num1 == num, 'Min number of moves incorrect'
        assert len(moves) == num, 'Actual number of moves incorrect'
​
        config = start
        for move in moves:
            assert len(move) == 4 and move[1:3] == '->' and move[3] in 'LMR',\
                   'Invalid move string ' + move
            disc, slot = move[0], eval(move[3])
            assert disc in discs, 'Disc ' + disc + ' not in valid discs ' + discs
            idx = config.index(disc)
            
            # check moved the top disc in its slot
            source_slot = L if 0 <= idx <= 2 else M if 3 <= idx <= 4 else R
            assert all(config[i] == '0' for i in range(idx+1,source_slot[1] + 1)), \
                   'Move ' + move + ' invalid: ' + 'can only move the top disc in a slot'
            assert '0' in config[slot[2]:slot[1]+1],\
                   'Move ' + move + ' invalid: ' + 'destination slot is full'
            
            # apply move to update config
            j = config[slot[2]:slot[1]+1].index('0') + slot[2]
            config2 = list(config)
            config2[idx], config2[j] = config2[j], config2[idx] #swap
            config = ''.join(config2)
​
        assert config == end, 'Final config ' + config + ' does not match end: ' + end
        return True
​
    except AssertionError as err:
        print(err)
        return False
        
def move_discs(start, end):
    dic = {start: []}
    queue = [start]
    while queue:
        new = queue.pop(0)
        if new == end:
            return (len(dic[new]), dic[new])
        next_info = possible_moves(new)
        for nex in next_info:
            if nex not in dic:
                dic[nex] = dic[new] + [next_info[nex]]
            queue.append(nex)
    return "didn't work"
​
​
def possible_moves(str):
    pieces = [str[:3].replace('0', ''), str[3:5].replace('0', ''), str[5:].replace('0', '')]
    inps = [i for i in range(3) if len(pieces[i]) > 0]
    outs = [i for i in range(3) if len(pieces[i]) < [3, 2, 3][i]]
    ans = {}
    for i in inps:
        for j in [j for j in outs if i != j]:
            new = pieces[:]
            new[j] += new[i][-1]
            new[i] = new[i][:-1]
            ans["{:.3}{:.2}{:.3}".format(*[n+'000' for n in new])] = \
                "{}->{}".format(pieces[i][-1], ['L', 'M', 'R'][j])
    return ans

