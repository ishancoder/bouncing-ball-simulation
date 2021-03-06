import pygame


GameExit = False
###Colors to use in the simulation###
black = [0,0,0]
white = [255,255,255]
red = [255,0,0]
green = [0,255,255]
blue = [0,0,255]

###variable for physics of the ball###
velocity_x = 0 #initial velocity in x direction
velocity_y = 10 #initial velocity in y direction
block_size = 40
x_pos = 100 #initially
y_pos = 100 #initially
move = 10
displacement = 0
jump_power = 50
g = 10 #gravity
t = 0.17 
energy_loss = 0.8


pygame.init()
clock = pygame.time.Clock()
disp = pygame.display.set_mode((800,600))
def draw_ball(x,y,size):
    pygame.draw.circle(disp,red,(x,y),size)

    
while not GameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity_y -= jump_power
            if event.key == pygame.K_RIGHT:
                velocity_x = move
            if event.key == pygame.K_LEFT:
                velocity_x = -move
        
    if x_pos - block_size <= 0:
        x_pos = block_size
        velocity_x = -energy_loss*velocity_x
    elif x_pos + block_size >= 800:
        x_pos = 800-block_size
        velocity_x = -energy_loss*velocity_x
    if y_pos >= 600-block_size:
        y_pos = 600-block_size
        velocity_y = -energy_loss*velocity_y
    elif y_pos - block_size <=0:
        y_pos = block_size
        velocity_y = -velocity_y
    
    clock.tick(60)
    displacement = velocity_y*t + 0.5*g*t*t
    velocity_y += g*t
    y_pos += int(displacement)
    x_pos += int(velocity_x)
    disp.fill(white)
    draw_ball(x_pos,y_pos,block_size)
    pygame.display.update()

    
pygame.quit()
quit()
