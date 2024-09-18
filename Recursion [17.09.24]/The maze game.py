maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', 'E', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '0', '#', '#', '#', '#']
]


def print_maze(maze):
    for row in maze:
        print(' '.join(row))


def find_player(maze):
    for x in range(len(maze)):
        for y in range(len(maze)):
            if maze[y][x] == 'E':
                return x, y


def find_exit(maze, x, y, steps):
    print_maze(maze)
    x, y = find_player(maze)

    move = input("Your move a/w/s/d (to exit, press zero): ")
    if move == '0':
        return
    elif move == 'w':
        new_x, new_y = x, y - 1
    elif move == 's':
        new_x, new_y = x, y + 1
    elif move == 'a':
        new_x, new_y = x - 1, y
    elif move == 'd':
        new_x, new_y = x + 1, y
    else:
        return find_exit(maze, x, y, steps)

    if maze[new_y][new_x] == '0':
        maze[y][x] = '-'
        maze[new_y][new_x] = 'E'
        steps += 1
        print_maze(maze)
        print(f"You won in {steps} steps!")
        return
    elif maze[new_y][new_x] != '#':
        maze[y][x] = '-'
        maze[new_y][new_x] = 'E'
        steps += 1
        
    return find_exit(maze, x, y, steps)

x, y = find_player(maze)
steps = 0
find_exit(maze, x, y, steps)