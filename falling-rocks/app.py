import os
import random
import time
import keyboard

ROWS = 10
COLS = 10
player_pos = COLS // 2
obstacles = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid():
    grid = [['  ' for _ in range(COLS)] for _ in range(ROWS)]
    for row, col in obstacles:
        if 0 <= row < ROWS:
            grid[row][col] = '🔘'
    grid[ROWS - 1][player_pos] = '🧍'
    return grid

def print_grid(grid):
    top_border = '╭' + ('──' * COLS) + '╮'
    bottom_border = '╰' + ('──' * COLS) + '╯'
    print(top_border)
    for row in grid:
        print('│' + ''.join(row) + '│')
    print(bottom_border)

def game_over():
    clear()
    print("\n\n💀 FUCK YOU IDIOT YOU LOSE 💀\n\n")
    exit()

while True:
    clear()

    if random.random() < 0.3:
        obstacles.append([0, random.randint(0, COLS - 1)])

    for ob in obstacles:
        ob[0] += 1

    for row, col in obstacles:
        if row == ROWS - 1 and col == player_pos:
            game_over()

    obstacles = [ob for ob in obstacles if ob[0] < ROWS]

    if keyboard.is_pressed('left') and player_pos > 0:
        player_pos -= 1
    elif keyboard.is_pressed('right') and player_pos < COLS - 1:
        player_pos += 1

    grid = create_grid()
    print_grid(grid)

    time.sleep(0.1)
