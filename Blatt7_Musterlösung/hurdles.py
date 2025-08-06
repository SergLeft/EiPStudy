obstacles = []
f = open('hurdles_solvable.txt')
for line in f:
    line = line.split(',')
    obstacles.append((int(line[0]), int(line[1])))
f.close()
            
# b)
x_min = x_max = obstacles[0][0]
y_min = y_max = obstacles[0][1]
for obstacle in obstacles:
    if x_min > obstacle[0]:
        x_min = obstacle[0]
    if y_min > obstacle[1]:
        y_min = obstacle[1]
    if x_max < obstacle[0]:
        x_max = obstacle[0]
    if y_max < obstacle[1]:
        y_max = obstacle[1]

# x_min = min([obstacle[0] for obstacle in obstacles])  # Alternativ...
bounding_box = [(x_min, y_min), (x_max, y_max)]
print(bounding_box)
width = x_max - x_min + 1
height = y_max - y_min + 1

# c)
# Variante 1
grid = []
for i in range(height):
    grid.append([])
    for j in range(width):
        grid[i].append('.')

# Variante 2
grid = []
for i in range(height):
    grid.append(['.' for _ in range(width)])

#Variante 3
grid = [['.' for _ in range(width)] for _ in range(height)] 
# auch OK ist durch x,y in width x height zu iterieren und schauen, ob in obstacles

for obstacle in obstacles:
    x, y = obstacle
    grid[y-y_min][x-x_min] = 'x'
            
'''
d)
Es sollen in jedem Schritt die Zellen gespeichert werden, die man als nächstes besuchen kann und sich die gemerkt
werden, die schon besucht wurden. Außerdem die Idee, dass wenn es keine besuchbaren Zellen gibt, das Ziel nicht
erreichbar ist, z.B.
1. Starten links unten.
2. Aktuelle Position als besucht markieren und prüfen, ob das Ende erreicht ist.
3. Alle möglichen nächsten Zellen, die nicht besucht sind, in eine Liste hinzufügen.
4. Eine Position aus der Liste nehmen, als aktuell setzen und zu 2. gehen. 
5. Wenn keine Positionen mehr in der Liste sind, dann ist das Ziel nicht erreichbar.
'''

def can_traverse(grid):
    w, h = len(grid[0]), len(grid)
    target = (w, h)
    # alternativ 2D Liste für besuchte Felder mit False/0 gefüllt
    visited = []
    Q = [(0, 0)]
    while len(Q) > 0:
        p = Q.pop()
        if p == target:
            return True
        visited.append(p)
        x, y = p
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            new_x, new_y = x+dx, y+dy
            if 0 <= new_x < w and 0 <= new_y < h and grid[new_y][new_x] != 'x' and (new_x, new_y) not in visited:
                Q.append((new_x, new_y))
    return False

can_traverse(grid)
