import sys, pygame
import copy
pygame.init()

size = width, height = 1000, 1000

screen = pygame.display.set_mode(size)

White = (255, 255, 255)
Black = (0, 0, 0)

done = False

clock = pygame.time.Clock()

cell_dim = cell_dim_x, cell_dim_y = 100, 100
cell_size = cell_size_x, cell_size_y = width / cell_dim_x, height / cell_dim_y
grid = [[False for x in range(width)] for y in range(height)]

is_paused = True

#grid[50][50] = True
#grid[51][50] = True
#grid[50][51] = True
#grid[51][51] = True

#grid[51][52] = True
#grid[52][53] = True

grid[0][0] = True
grid[1][0] = True
grid[0][1] = True
grid[1][1] = True

grid[2][2] = True
grid[3][2] = True
grid[2][3] = True
grid[3][3] = True

grid[10][10] = True
grid[10][11] = True
grid[10][12] = True

def check_cell(prev_grid, x, y):
    if x < 0 or x >= cell_dim_x or y < 0 or y >= cell_dim_y:
        return 0
    if prev_grid[x][y] == True:
        return 1
    return 0

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
    if prev_grid[x][y] == True and neighbours == 2 or neighbours == 3:
        grid[x][y] = True
    else:
        grid[x][y] = False

def update_grid():
    prev_grid = copy.deepcopy(grid)
    for x in range(cell_dim_x):
        for y in range(cell_dim_y):
            update_cell(prev_grid, x, y)

def clear_screen():
    screen.fill(Black)

def draw_cells():
    color_step_x, color_step_y = 255 / cell_dim_x, 255 / cell_dim_y
    for i in range(0, cell_dim_x):
        for j in range (0, cell_dim_y):
            if grid[i][j] == True:
                pygame.draw.rect(screen, White, [i * cell_size_x, j * cell_size_y, cell_size_x, cell_size_y])
            else:
                pygame.draw.rect(screen, Black, [i * cell_size_x, j * cell_size_y, cell_size_x, cell_size_y])


def on_key_event(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            print("pressed space")
            global is_paused
            is_paused = not is_paused

while not done:

    pygame.time.wait(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting")
            done = True
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            on_key_event(event)

    if (is_paused):
        continue

    clear_screen()
    update_grid()
    draw_cells()

    pygame.display.flip()


pygame.quit()
