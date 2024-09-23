import random

width = 11
height = 7

maze = [['#' for _ in range(width)] for _ in range(height)]


def get_valid_neighbors(x, y):
    neighbors = []
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)] # Вверх, вниз, влево, вправо

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == '#':
            neighbors.append((nx, ny))
    
    return neighbors


def generate_maze(x, y):
    maze[y][x] = ' '
    neighbors = get_valid_neighbors(x, y)

    while neighbors:
        nx, ny = random.choice(neighbors)
        if maze[ny][nx] == '#':
            maze[(y + ny) // 2][(x + nx) // 2] = ' ' # Пробиваем стену
            generate_maze(nx, ny)

        neighbors = get_valid_neighbors(x, y)

start_x = 1
start_y = 1

generate_maze(start_x, start_y)
maze[1][1] = 'E'
maze[6][9] = '0'


def print_maze(maze):
    print("\033[H\033[J", end="") # Очистка терминала
    for row in maze:
        print(' '.join(row))


def find_player(maze):
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 'E':
                return x, y


def find_exit(maze, x, y, steps):
    print_maze(maze)
    
    player_position = find_player(maze)
    x, y = player_position

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

    if 0 <= new_x < width and 0 <= new_y < height:
        if maze[new_y][new_x] != '#':
            if maze[new_y][new_x] == '0':
                maze[y][x] = '-'
                maze[new_y][new_x] = 'E'
                print_maze(maze)
                print(f"You won in {steps + 1} steps!")
                return

            maze[y][x] = '-'
            maze[new_y][new_x] = 'E'
            steps += 1
        
    return find_exit(maze, new_x, new_y, steps)

x, y = find_player(maze)
steps = 0
find_exit(maze, x, y, steps)