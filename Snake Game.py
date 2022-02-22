import pygame
import random
import time

#Window
pygame.init()

white = (255, 255, 255)
yellow = (255, 25, 102)
black = (0, 0, 0)
red = (213, 50 ,80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((600, 400))

pygame.display.set_caption('Snake Game')

#Enable Time

clock = pygame.time.Clock()

# set speed of snake and block

snake_block = 10
Snake_speed = 15

# adding font styles and size

font_style = pygame.font.SysFont('bahnschrift', 25)
score_font = pygame.font.SysFont('coufier', 20, 'bold')

# setting up score

def Your_score(score) :
    value = score.font.render('Made by...Your score) ' + str(score), True, yellow)
# message display

def our_snake(snkae_block, snake_lift) :
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0],x[1], snake_block, snake_block])
        
# game lop and main function

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width /2
    y1 = dis_height /2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block)/ 10.0)* 10.0
    foody = round(random.randrange(0, dis_height - snake_block)/ 10.0)* 10.0

    while not game_over:
        while game_close== True:
            dis.fill(blue)
            message ('You Lost!! Press c- Play Again OR Q- Quit', red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.L_a:
                        gameloop()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                            x1_change =-snake_block
                            y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                            x1_change =snake_block
                            y1_change = 0
                    elif event.key == pygame.K_UP:
                            y1_change =-snake_block
                            x1_change = 0
                    elif event.key == pygame.K_DOWN:
                            y1_change =snake_block
                            x1_change = 0

            if x1>= dis_width or x1<0 or y1>= dis_height or y1<0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head.appendix(x1)
            snake_Head.appendix(y1)
            snake_List.appendix(snake_Head)
            if len(snake_List) > Lenght_of_snake:
                del snake_List[0]

            for x in snake_List [:-1]:
                if x == snake_Head:
                    game_close = True
            our_snake(snake_block, Snake_List)
            Your_score(Length_of_snake -1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block)/ 10.0)*10.0
                foody = round(random.randrange(0, dis_height - snake_block)/ 10.0)*10.0
                Lenght_of_snake += 1

            clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()
