from msilib.schema import Font
import pygame 
import random                       

pygame.init()

# Game Constants 
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
violet = (238,130,238)
ListColor = [white,black,red,green,blue,violet]
WIDTH = 1000
HEIGHT = 800

# Game Variables 
score = 0
player_x = 50 
player_y = 580
y_change = 0
gravity = 0.3
x_change = 0
obs = [800,1000,1200]
obs_speed = 1
active = False

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Endless Runner')
background = black 
fps = 300
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

running = True

while running: 
    timer.tick(fps)
    screen.fill(background)
    if not active: 
        instruction_text = font.render(f'PRESS SPACEBAR TO START', True, white, black)
        screen.blit(instruction_text, (40,60))
        instruction1_text = font.render(f'PRESS SPACEBAR TO JUMP , LEFT/RIGHT TO MOVE', True, white, black)
        screen.blit(instruction1_text, (40,90))

    score_text = font.render(f'Score : {score}', True, white, black)
    screen.blit(score_text, (40,30))

    floor = pygame.draw.rect(screen,white,[0,600,WIDTH,20],border_radius=1500)
    player = pygame.draw.circle(screen,violet,[player_x,player_y],20)
    obs0 = pygame.draw.rect(screen,red,[obs[0],575,25,25])
    obs1 = pygame.draw.rect(screen,green,[obs[1],565,35,35])
    obs2 = pygame.draw.rect(screen,blue,[obs[2],570,30,30])

    for i in range(len(obs)): 
        if active: 
            obs[i] -= obs_speed 
            if obs[i] < -20: 
                if score != 0 and score % 2 == 0 :
                    obs_speed += 0.2
                obs[i] = random.randint(1000,1600) 
                score += 1 
            if player.colliderect(obs0) or player.colliderect(obs1) or player.colliderect(obs2): 
                active = False 

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:  
            running = False
        if event.type == pygame.KEYDOWN and not active: 
            if event.key == pygame.K_SPACE:
                y_change = 20 
                obs = [800,1000,1200]
                player_x = 20
                score = 0
                obs_speed = 1
                active = True 

        if event.type == pygame.KEYDOWN and active: 
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 20 
            if event.key == pygame.K_RIGHT: 
                x_change = 2
            if event.key == pygame.K_LEFT: 
                x_change = -2 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT: 
                x_change = 0 
            if event.key == pygame.K_LEFT: 
                x_change = 0 


    if 20 <= player_x <= WIDTH-20: 
        player_x += x_change 
    if player_x < 20: 
        player_x = 20
    if player_x > WIDTH-20:
        player_x = WIDTH-20

    if y_change > 0 or player_y < 580:
        player_y -= y_change
        y_change -= gravity

    if player_y > 580: 
        player_y = 580

    if player_y == 580 and y_change < 0: 
        y_change = 0
    
    pygame.display.flip() 
pygame.quit()


