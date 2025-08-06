import maze_drawer as mz

datei = open('maze2.txt', 'r')
maze = [list(line) for line in datei]
datei.close()

# Find start
x, y = -1, -1
for i in range(len(maze)):
    row = maze[i]
    for j in range(len(row)):
        if row[j] == 'S':
            x, y = j, i

prev = [[[-1,-1] for _ in range(len(maze[0]))] for _ in range(len(maze))]
visit_queue = [[x, y]]

is_solvable = False
while len(visit_queue) != 0:
    el = visit_queue.pop(0)
    cx, cy = el[0], el[1]
    if maze[cy][cx] == 'E':
        is_solvable = True
        break
    for richtung in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        dx, dy = richtung[0], richtung[1]
        next_cx, next_cy = cx + dx, cy + dy
        if 0 <= next_cx < len(maze[0]) and 0 <= next_cy < len(maze):  # Nächstes Feld im Labyrinth
            if maze[next_cy][next_cx] == ' ' or maze[next_cy][next_cx] == 'E':  # Nächstes Feld im begehbar
                if prev[next_cy][next_cx] == [-1, -1]:  # Nächstes Feld noch nicht besucht
                    visit_queue.append([next_cx, next_cy])
                    prev[next_cy][next_cx] = [cx, cy]

if is_solvable:
    while prev[cy][cx] != [-1,-1]:
        cx, cy = prev[cy][cx][0], prev[cy][cx][1]
        if maze[cy][cx] == 'S':
            break
        maze[cy][cx] = 'X'
    mz.draw_maze(maze)
    print("Der Weg ist frei!")
else:
    print("Der Weg ist versperrt!")