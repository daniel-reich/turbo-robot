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
        
def make_graph(start):
    '''
    Returns a graph representing all possible valid configurations and their edges
    to other configurations (configuration and moves to obtain them),biggest will
    be between 3 and 5, inferred from start.
    '''
    from itertools import permutations
​
    # generate valid configs and empty edges lists
    biggest = max(int(d) for d in start)
    config = (8 - biggest) * '0' + ''.join(str(i) for i in range(1, biggest + 1))
    graph = {''.join(p): [] for p in permutations(config, 8)
             if not (p[0] == '0' and p[1] != '0' or p[1] == '0' and p[2] != '0' or
                     p[3] == '0' and p[4] != '0' or p[5] == '0' and p[6] != '0' or
                     p[6] == '0' and p[7] != '0')}
​
    # generate edges (next configuration, move to get to it)
    L =('L', 2,0); M = ('M', 4,3); R = ('R', 7, 5)  # slots:name, top idx, low idx
    slots = set((L,M,R))
​
    for config in graph:
        
        for slot in slots:
            copy = slots.copy()
            copy.remove(slot)
            _, top, low = slot
            
            for i in range(top, low - 1, -1): # move backwards
                moved = False
                if config[i] != '0':  # possible to move this
                    for target in copy:
                        label, ttop, tlow = target
                        if '0' in config[tlow:ttop+1]:  # has got a spare location
                            j = config[tlow:ttop+1].index('0') + tlow
                            moved = True
                            config2 = list(config)
                            config2[i], config2[j] = config[j], config[i] #swap
                            config2 = ''.join(config2)
                            graph[config].append((config2,config[i]+'->'+label))
                if moved:
                    break  # move on to next slot
​
    return graph
​
def move_discs(start, end):
    '''
    Returns a tuple (n, moves) where n is the minimum number of moves to get from
    config start to config end and moves is the list of those moves, as per the
    instructions. start determines the largest numbered disc (3, 4 or 5)
    '''
    g = make_graph(start)
    q = []
    visited = set()
    path = {config: ('','') for config in g}  # use to trace path
    q.append(start)
​
    while q:
        conf = q.pop(0)
        if conf == end:
            count = 0
            next_conf, next_move = path[end]
            moves = []
​
            while next_conf != '':
                count += 1
                moves.append(next_move)
                next_conf, next_move = path[next_conf]
​
            return (count, moves[::-1])
​
        visited.add(conf)
        for conf2, move in g[conf]:
            if conf2 not in visited and conf2 not in q:
                path[conf2] = (conf, move)  # update path entry
                q.append(conf2)
​
    return 'Error!!!'    # should not arise.

