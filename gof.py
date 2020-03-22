import sys, pygame
import copy, time
import numpy as np

pygame.init()

size = width, height = 1000, 1000

screen = pygame.display.set_mode(size)

White = (255, 255, 255)
Black = (0, 0, 0)

done = False

clock = pygame.time.Clock()

cell_dim = cell_dim_x, cell_dim_y = 100, 100
cell_size = cell_size_x, cell_size_y = width / cell_dim_x, height / cell_dim_y
grid = np.zeros(cell_dim)

is_paused = True

def check_cell(prev_grid, x, y):
    if x < 0 or x >= cell_dim_x or y < 0 or y >= cell_dim_y:
        return 0
    return prev_grid[x][y]

def count_neighbours(prev_grid, x, y):
    neighbours = 0
    neighbours += check_cell(prev_grid, x - 1, y - 1)
    neighbours += check_cell(prev_grid, x, y - 1)
    neighbours += check_cell(prev_grid, x + 1, y - 1)
    neighbours += check_cell(prev_grid, x - 1, y)
    neighbours += check_cell(prev_grid, x + 1, y)
    neighbours += check_cell(prev_grid, x - 1, y + 1)
    neighbours += check_cell(prev_grid, x, y + 1)
    neighbours += check_cell(prev_grid, x + 1, y + 1)

    return neighbours

def update_cell(prev_grid, x, y):
    neighbours = count_neighbours(prev_grid, x, y)
    if prev_grid[x][y] == 1 and neighbours == 2 or neighbours == 3:
        grid[x][y] = 1
    else:
        grid[x][y] = 0

def evolve():
    prev_grid = np.copy(grid)
    for (x, y), value in np.ndenumerate(prev_grid):
        update_cell(prev_grid, x, y)

def clear_screen():
    screen.fill(Black)

def draw_cells():
    color_step_x, color_step_y = 255 / cell_dim_x, 255 / cell_dim_y
    for i in range(cell_dim_x):
        for j in range(cell_dim_y):
            if grid[i][j] == 1:
                pygame.draw.rect(screen, White, [i * cell_size_x, j * cell_size_y, cell_size_x, cell_size_y])
            else:
                pygame.draw.rect(screen, Black, [i * cell_size_x, j * cell_size_y, cell_size_x, cell_size_y])


def on_key_event(event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_q:
            print("Exiting")
            global done
            done = True
        elif event.key == pygame.K_SPACE:
            print("pause/unpause")
            global is_paused
            is_paused = not is_paused
        elif event.key == pygame.K_c:
            print("clearing")
            grid.fill(0)


def on_mouse_click(event):
    cell_coord = int(event.pos[0] / width * cell_dim_x), int(event.pos[1] / height * cell_dim_y)
    print("Cell coord=" + str(cell_coord))
    global grid
    print(grid[cell_coord[0]][cell_coord[1]])
    grid[cell_coord[0]][cell_coord[1]] = not grid[cell_coord[0]][cell_coord[1]]
    print(grid[cell_coord[0]][cell_coord[1]])


def on_mouse_event(event):
    if event.type == pygame.MOUSEBUTTONUP:
        print("Mouse pos=" + str(event.pos))
        on_mouse_click(event)


start = time.time()
end = time.time()
fps = 15
period =  int(1 / fps * 1000)

while not done:
    wait_time = max(int(period - (end - start) * 1000), 0)
    pygame.time.wait(wait_time)

    start = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting")
            done = True
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            on_key_event(event)
        if event.type == pygame.MOUSEBUTTONUP:
            on_mouse_event(event)

    clear_screen()

    if (not is_paused):
        evolve()

    draw_cells()

    pygame.display.flip()

    end = time.time()

pygame.quit()
