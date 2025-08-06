
def extract_route(pred, start, target):
    route = []
    # start at the target
    cur = target
    while cur != start:
        if cur in route:
            # we have a cycle, no route
            return None
        route.append(cur)
        # and go backwards
        cur = pred[cur[0]][cur[1]]
        # remove last component
        cur = (cur[0], cur[1])

    route.append(start)
    # reverse for correct order
    # 1)
    # route.reverse()
    # 2)
    # route = route[::-1]
    # 3)
    route = [route[-i] for i in range(1, len(route) + 1)]
    return route
    


def is_valid(matrix, i,j):
    #                                                           Überprüft auf unmögliche und bereits besuchte Orte
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[i]) and matrix[i][j] == 1


def get_valid_cells(matrix, i,j):
    l = []
    for direction in [(0,-1), (-1,0), (1,0), (0,1)]:
        if is_valid(matrix, i+direction[0], j+direction[1]):
            l.append((i+direction[0], j+direction[1]))
    return l



def longest_route(matrix, start, target):
    # a) Hier speichern wir die Länge des längsten Pfades
    longest = -1
    # b) Hier speichern wir die Vorgängerzellen um später den Pfad rekonstruieren zu können
    # we keep track of the longest path that leads there
    # (i, j, max_length)
    pred = [ [(-1,-1,-1)] * len(matrix[i]) for i in range(len(matrix))]

    def dfs(matrix, steps, i,j):
        nonlocal longest, pred
        # check if valid (start could be invalid already)
        if not is_valid(matrix, i,j):
            return -1
        
        # we reached the end
        if (i,j) == target:
            return steps
        
        # get all possible (unmarked) cells
        next = get_valid_cells(matrix, i,j)

        # mark the cell
        matrix[i][j] = 8

        # currently no possible way to target
        long = -1

        # go from here to all of the next cells
        for p in next:
            long = max(long, dfs(matrix, steps+1, p[0], p[1]))
            # if the current path is longer than the longest yet
            # save as predecessor 
            # b) mit predecessors
            if long > pred[p[0]][p[1]][2]:
                pred[p[0]][p[1]]= (i,j,long)
            # a) ohne predecessors
            if long > longest:
               longest = long
        
        # undo mark
        matrix[i][j] = 1
        return long

    return dfs(matrix, 0, start[0], start[1]), pred


### from here it's just testing
matrix = [
[
    [1,0,0],
    [1,1,1],
    [1,1,1]
],
[
	[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
	[1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
	[1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
	[0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
	[1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
	[1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
	[1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
	[1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
	[1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
],
    [
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1], 
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1], 
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1], 
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1], 
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
],
[
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1], 
    [0, 0, 1, 0, 1, 1, 1, 0, 0, 1], 
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1], 
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1], 
    [1, 0, 1, 1, 1, 0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 1], 
    [0, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
    [1, 1, 1, 1, 1, 0, 0, 1, 1, 1], 
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
]
]

start_target = [[(0,0),(2,2)],[(0,0),(5,7)],[(9,8),(0,0)], [(0,0), (8,3)]]
expected = [6, 22, -1, 29]

for ex, st, m in zip(expected, start_target, matrix):
    length, pred = longest_route(m, *st)
    print(f'expected length: {ex}, computed length: {length}, match: {length == ex}')

    if length != -1:
        route = extract_route(pred, *st)
        if route is not None:
            print(' -> '.join(map(str, route)))
