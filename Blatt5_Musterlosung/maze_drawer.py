import random

def create_maze(n2):
    n = n2 // 2
    maze = [['#'] * (n * 2 + 1) for _ in range(n * 2 + 1)]

    last = (-1,-1)
    def carve(x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < n * 2 and 1 <= ny < n * 2 and maze[ny][nx] == '#':
                maze[ny][nx] = ' '
                maze[ny - dy//2][nx - dx//2] = ' '
                last = (nx-1, ny - 1)
                carve(nx, ny)
                

    maze[1][0] = 'S'
    carve(1, 1)
    maze[-2][-1] = 'E'
    return maze


def draw_maze(maze):
    for row in maze:
        for cell in row:
            if cell.lower() == 'e':
                print('\x1b[5;30;42m  \x1b[0m', end='')
            if cell.lower() == 's':
                print('\x1b[5;30;41m  \x1b[0m', end='')
            if cell.lower() == 'x':
                print('\x1b[5;30;44m  \x1b[0m', end='')
            if cell == '#':
                print('\x1b[5;30;40m  \x1b[0m', end='')
            if cell == ' ':
                print('\x1b[5;30;47m  \x1b[0m', end='')
        print()
    print()