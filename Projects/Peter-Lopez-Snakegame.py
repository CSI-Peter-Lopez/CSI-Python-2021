import pygame
import time
import random
pygame.init() # inicia todos los módulos de Pygame


yellow = (255, 255, 102) #Score
black = (0, 0, 0) #pantalla
red = (213, 50, 80) #game over
green = (0, 255, 0) #food
pink = (238,18,137) #snake

dis_width = 400
dis_height = 300
dis=pygame.display.set_mode((dis_width,dis_height))

pygame.display.set_caption("Snake game by PL")
game_over=False

snake_block = 10
snake_sped = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 25)
score_font = pygame.font.SysFont(None, 25)

def My_score(score):
    value = score_font.render("Your Score:" + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, pink, [x[0], x[1], snake_block, snake_block])

        
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/7, dis_height/2.5])

def gameRestart():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2
    
    x1_change = 0
    y1_change = 0 

    snake_List=[]
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) *10
    foody = round(random.randrange(0, dis_height - snake_block) / 10) *10

    
    while not game_over:

        while game_close == True:
            dis.fill(black)
            message("YOU LOST Press Q-Quit or P-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN: 
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameRestart()

        for event in pygame.event.get():
            if event.type==pygame.QUIT: 
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >=dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #crea el food
        #pygame.draw.rect(dis, pink, [x1,y1, snake_block, snake_block]) # crea el snake y lo ubica en la pantalla
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_List.append(snake_head)
        if len(snake_List) > length_of_snake:
            del snake_List[0]

        for x in snake_List[: -1]:
            if x == snake_head:
                game_close = True 

        our_snake(snake_block, snake_List)

        My_score(length_of_snake -1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10) *10
            foody = round(random.randrange(0, dis_height - snake_block) / 10) *10
            length_of_snake += 1

        clock.tick(snake_sped)


#pygame.display.update()
#time.sleep(5)
    pygame.quit()
    quit()

gameRestart()

