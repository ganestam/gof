import sys, pygame
pygame.init()

size = width, height = 2000, 2000

screen = pygame.display.set_mode(size)

White = (255, 255, 255)
Black = (0, 0, 0)

done = False

clock = pygame.time.Clock()

cell_dim = cell_dim_x, cell_dim_y = 100, 100
cell_size = cell_size_x, cell_size_y = width / cell_dim_x, height / cell_dim_y

def clear_screen():
    screen.fill(Black)

def draw_cells():
    color_step_x, color_step_y = 255 / cell_dim_x, 255 / cell_dim_y
    for i in range(0, cell_dim_x):
        for j in range (0, cell_dim_y):
            if j < cell_dim_y / 2:
                pygame.draw.rect(screen, (50, 50, 200), [i * cell_size_x, j * cell_size_y, cell_size_x, cell_size_y], 1)
            else:
                pygame.draw.rect(screen, (200, 200, 0), [i * cell_size_x, j * cell_size_y, cell_size_x, cell_size_y], 1)



def on_key_event(event):
    return
#    if event.type == pygame.KEYUP:
#        if event.

while not done:

    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting")
            done = True
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            on_key_event(event)
    

    clear_screen()
    draw_cells()

    pygame.display.flip()


pygame.quit()
