Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... import time
... 
... # Define the grid size
... GRID_WIDTH = 10
... GRID_HEIGHT = 10
... 
... # Define symbols
... EMPTY = '.'
... OBSTACLE = '#'
... CAR = 'C'
... GOAL = 'G'
... 
... # Initialize grid
... grid = [[EMPTY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
... 
... # Random obstacles
... for _ in range(15):
...     x, y = random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1)
...     grid[y][x] = OBSTACLE
... 
... # Starting and goal positions
... car_pos = [0, 0]
... goal_pos = [GRID_WIDTH-1, GRID_HEIGHT-1]
... grid[car_pos[1]][car_pos[0]] = CAR
... grid[goal_pos[1]][goal_pos[0]] = GOAL
... 
... def print_grid():
...     for row in grid:
...         print(' '.join(row))
...     print()
... 
... def move_car():
...     x, y = car_pos
...     gx, gy = goal_pos
...     grid[y][x] = EMPTY
... 
    # Move towards goal while avoiding obstacles
    if gx > x and grid[y][x+1] != OBSTACLE:
        x += 1
    elif gy > y and grid[y+1][x] != OBSTACLE:
        y += 1
    elif gx < x and grid[y][x-1] != OBSTACLE:
        x -= 1
    elif gy < y and grid[y-1][x] != OBSTACLE:
        y -= 1

    car_pos[0], car_pos[1] = x, y
    grid[y][x] = CAR

# Run simulation
print("Initial Map:")
print_grid()

while car_pos != goal_pos:
    time.sleep(0.3)
    move_car()
    print_grid()

print("🚗 Reached the destination!")
