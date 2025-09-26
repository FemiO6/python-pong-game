import pygame
import random
import sys
from button import Button

clock = pygame.time.Clock()
# activate pygame
pygame.init()
 
# creating the pygame window
LENGTH, HEIGHT = 1250, 625
Gamewindow = pygame.display.set_mode((LENGTH, HEIGHT)) 
pygame.display.set_caption("Femi's Pong game")                

Backround = pygame.image.load("backround.png")

def get_font(size):
    return pygame.font.Font("font.ttf", size)

def pvp():


    while True:
       
        
        x=0
        #allowing for score to be dispalyed
        FONT = pygame.font.SysFont("Consolas", int(LENGTH/20))
        #Creating the dimensions for the paddles
        paddle1 = pygame.Rect(LENGTH-110, HEIGHT/2-50, 25,125)
        paddle2 = pygame.Rect(110, HEIGHT/2-50, 25,125)
        #Setting variables for score and setting it to 0
        p1_score, p2_score = 0, 0

        #Creating the dimensions for the ball
        ball = pygame.Rect(LENGTH/2-10, HEIGHT/2-10, 20, 20)
        #allows ball to move in any direction within game window
        speed_x, speed_y = 1, 1
        
    
        #to keep window open until choosing to close it
        running = True
        while running:
            key = pygame.key.get_pressed()#this will allow for keybinds to be given so that the paddles can be moved at the same time
            #moving the paddles
            if key[pygame.K_UP]:
                if paddle1.top > 0:# makes sure paddle cannot travel off the scrren
                    paddle1.top -= 2
            if key[pygame.K_DOWN]:
                if paddle1.bottom < HEIGHT:
                    paddle1.bottom += 2
            if key[pygame.K_w]:
                if paddle2.top > 0:
                    paddle2.top -= 2
            if key[pygame.K_s]:
                if paddle2.bottom < HEIGHT:
                    paddle2.bottom += 2
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    quit()
            #making the ball stay within the cinfines of the screen
            if ball.y >= HEIGHT:
                speed_y = -1
            if ball.y <= 0:
                speed_y = 1
            if ball.x <=0:
                p1_score += 1
                ball.center = (LENGTH/2, HEIGHT/2)
                speed_x, speed_y = random.choice([-1, 1]), random.choice([-1, 1])
            if ball.x >= LENGTH:
                p2_score += 1
                ball.center = (LENGTH/2, HEIGHT/2)
                speed_x, speed_y = random.choice([-1, 1]), random.choice([-1, 1])
            #making the ball bounce off the paddles
            if paddle1.x - ball.width <= ball.x <= paddle1.x and ball.y in range(paddle1.top-ball.width, paddle1.bottom+ball.width):
                speed_x = -1
            if paddle2.x - ball.width <= ball.x <= paddle2.x and ball.y in range(paddle2.top-ball.width, paddle2.bottom+ball.width):
                speed_x = 1 

           
            #allowing the ball to move
            ball.x += speed_x *2.5
            ball.y += speed_y *2.5
            #Displaying the score
            paddle1_score_text = FONT.render(str(p1_score), True, "white")
            paddle2_score_text = FONT.render(str(p2_score), True, "white")

            if p1_score>= 10:
                    x = -1
            if p2_score>= 10:
                x = 1
                
            if x > 0:
                
                main_menu()
                pygame.display.update()
            if x < 0:
                
                main_menu()
                pygame.display.update()
            
              
            
            # makes sure that when paddles are moved true position of paddle is shown 
            Gamewindow.fill("black")
            #allows for paddles and ball to appear on the game window
            pygame.draw.rect(Gamewindow, "Blue", paddle1)
            pygame.draw.rect(Gamewindow, "Red", paddle2)
            pygame.draw.circle(Gamewindow,"Magenta", ball.center, 15)

            Gamewindow.blit(paddle1_score_text, (LENGTH/2+50, 50))
            Gamewindow.blit(paddle2_score_text, (LENGTH/2-50, 50))
            if x == 0:
                        pygame.display.update()
            clock.tick(300)

def Ai():

    while True:
        
        
            x=0
            #allowing for score to be dispalyed
            FONT = pygame.font.SysFont("Consolas", int(LENGTH/20))
            #Creating the dimensions for the paddles
            paddle1 = pygame.Rect(LENGTH-110, HEIGHT/2-50, 25,125)
            bot_paddle = pygame.Rect(110, HEIGHT/2-50, 25,125)
            #Setting variables for score and setting it to 0
            p1_score, Ai_score = 0, 0

            #Creating the dimensions for the ball
            ball = pygame.Rect(LENGTH/2-10, HEIGHT/2-10, 20, 20)
            #allows ball to move in any direction within game window
            speed_x, speed_y = 1, 1
            #creating game ending mechanics
        
            #to keep window open until choosing to close it
            running = True
            while running:
                key = pygame.key.get_pressed()#this will allow for keybinds to be given so that the paddles can be moved at the same time
                #moving the paddles
                if key[pygame.K_UP]:
                    if paddle1.top > 0:# makes sure paddle cannot travel off the scrren
                        paddle1.top -= 2
                if key[pygame.K_DOWN]:
                    if paddle1.bottom < HEIGHT:
                        paddle1.bottom += 2
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        quit()
                #making the ball stay within the cinfines of the screen
                if ball.y >= HEIGHT:
                    speed_y = -1
                if ball.y <= 0:
                    speed_y = 1
                if ball.x <=0:
                    p1_score += 1
                    ball.center = (LENGTH/2, HEIGHT/2)
                    speed_x, speed_y = random.choice([-1, 1]), random.choice([-1, 1])
                if ball.x >= LENGTH:
                    Ai_score += 1
                    ball.center = (LENGTH/2, HEIGHT/2)
                    speed_x, speed_y = random.choice([-1, 1]), random.choice([-1, 1])
                #making the ball bounce off the paddles
                if paddle1.x - ball.width <= ball.x <= paddle1.x and ball.y in range(paddle1.top-ball.width, paddle1.bottom+ball.width):
                    speed_x = -1
                if bot_paddle.x - ball.width <= ball.x <= bot_paddle.x and ball.y in range(bot_paddle.top-ball.width, bot_paddle.bottom+ball.width):
                    speed_x = 1 
                # making Ai track the ball

                if bot_paddle.y < ball.y:
                    bot_paddle.top += 1.5
                if bot_paddle.bottom > bot_paddle.y:
                    bot_paddle.bottom -= 1.5 
                    
                #allowing the ball to move
                ball.x += speed_x *2.5
                ball.y += speed_y *2.5
                #Displaying the score
                paddle1_score_text = FONT.render(str(p1_score), True, "black")
                bot_paddle_score_text = FONT.render(str(Ai_score), True, "black")

                if p1_score>= 10:
                    x = -1
                if Ai_score>= 10:
                    x = 1
                    
                if x > 0:
                   
                    main_menu()
                    pygame.display.update()
                if x < 0:
                    
                    main_menu()
                    pygame.display.update()
                
                
                
                # makes sure that when paddles are moved true position of paddle is shown 
                Gamewindow.fill("papaya whip")
                #allows for paddles and ball to appear on the game window
                pygame.draw.rect(Gamewindow, "Blue", paddle1)
                pygame.draw.rect(Gamewindow, "Red", bot_paddle)
                pygame.draw.circle(Gamewindow,"Magenta", ball.center, 15)

                Gamewindow.blit(paddle1_score_text, (LENGTH/2+50, 50))
                Gamewindow.blit(bot_paddle_score_text, (LENGTH/2-50, 50))
                if x == 0:
                            pygame.display.update()
                clock.tick(300)

def endless():
    
    while True:
            
        x = 0
            
        #allowing for score to be dispalyed
        FONT = pygame.font.SysFont("Consolas", int(LENGTH/20))
        
        #Creating the dimensions for the paddles
        paddle1 = pygame.Rect(LENGTH/2, 580, 200, 20)
        
        #Setting variables for score and setting it to 0
        p1_score = 0     
        
        #Creating the dimensions for the ball
        ball = pygame.Rect(LENGTH/2-10, HEIGHT/2-10, 20, 40)
        
        #allows ball to move in any direction within game window
        speed_x, speed_y = 1, 1
            
            #to keep window open until choosing to close it
        running = True
        while running:
            key = pygame.key.get_pressed()#this will allow for keybinds to be given so that the paddles can be moved at the same time
            #moving the paddles
            if key[pygame.K_LEFT]:
                if paddle1.x >= 0:# makes sure paddle cannot travel off the scrren
                    paddle1.x -= 2
            if key[pygame.K_RIGHT]:
                if paddle1.x <= LENGTH-200:
                    paddle1.x += 2
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    quit()  
                #making the ball stay within the cinfines of the screen
            if ball.y >= HEIGHT:
                 speed_y = -1
            if ball.y <= 0:
                 speed_y = 1
            if ball.x <=0:
                speed_x = 1
            if ball.x >= LENGTH:
                speed_x = -1
             #making the ball bounce off the paddles
            if ball.colliderect(paddle1):
                speed_y = -1
                p1_score = p1_score + 1

            #game over condition
            if ball.y >= HEIGHT:
                main_menu()
            #allowing the ball to move
            ball.x += speed_x *1.5
            ball.y += speed_y *1.5
            # makes sure that when paddles are moved true position of paddle is shown 
            Gamewindow.fill("grey")
            #allows for paddle and ball to appear on the game window
            pygame.draw.rect(Gamewindow, "black", paddle1)
            pygame.draw.circle(Gamewindow,"black", ball.center, 15)

            paddle1_score_text = FONT.render(str(p1_score), True, "black")

            Gamewindow.blit(paddle1_score_text, (LENGTH/2+50, 50))
            if x == 0:
                pygame.display.update()
            clock.tick(300)

def main_menu():
    while True:
        Gamewindow.blit(Backround, (0, 0))
        Menu_Pointer_pos = pygame.mouse.get_pos()

        Menu_txt = get_font(50).render("Paddle PoP!", True, "green")
        Menu_rect = Menu_txt.get_rect(center=(LENGTH/2, 100))

        pvp_button = Button(image=pygame.image.load("red.png"), pos=(LENGTH/2, 180), 
                            text_input="PvP", font=get_font(50), base_colour="blue", secondary_colour="white")
        Ai_button = Button(image=pygame.image.load("magenta.png"), pos=(LENGTH/2, 300), 
                           text_input="Vs Ai", font=get_font(50), base_colour="black", secondary_colour="white")
        endless_button = Button(image=pygame.image.load("blue.png"), pos=(LENGTH/2, 450), 
                            text_input="endless", font=get_font(50), base_colour="red", secondary_colour="white")
        quit_button = Button(image=pygame.image.load("black.png"), pos=(LENGTH/2, 570), 
                             text_input="QUIT", font=get_font(50), base_colour="magenta", secondary_colour="white")
        Gamewindow.blit(Menu_txt, Menu_rect)

        for button in [pvp_button, Ai_button, endless_button, quit_button]:
            button.Colourchange(Menu_Pointer_pos)
            button.update(Gamewindow)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pvp_button.Check_for_input(Menu_Pointer_pos):
                    pvp()
                if Ai_button.Check_for_input(Menu_Pointer_pos):
                   Ai()
                if endless_button.Check_for_input(Menu_Pointer_pos):
                   endless()
                if quit_button.Check_for_input(Menu_Pointer_pos):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main_menu()