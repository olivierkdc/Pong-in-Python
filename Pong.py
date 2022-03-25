### Import libraries
import pygame

### Import players class
from Player import Player
from Ball import Ball

WIDTH, HEIGHT = 800, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Pong!')

'''
COLORS
'''
BLACK = (0,0,0)
WHITE = (255,255,255)

'''
Players
'''
PLAYER_WIDTH, PLAYER_HEIGHT = 15, 100
def player_movement(keys, player1, player2):
    #Player1 
    if keys[pygame.K_w] and player1.y - player1.VELOCITY >= 0:
        player1.move(up=True)
    if keys[pygame.K_s] and player1.y + player1.height + player1.VELOCITY <= HEIGHT:
        player1.move(up=False)
    
    #Player2
    if keys[pygame.K_UP] and player2.y - player2.VELOCITY >= 0:
        player2.move(up=True)
    if keys[pygame.K_DOWN] and player2.y + player2.height + player2.VELOCITY <= HEIGHT:
        player2.move(up=False)

'''
BALL
'''
BALL_RADIUS = 8 
def ball_collision(ball, player1, player2):
    #Vertical collisions (ceiling/floor of window)
    if ball.y + ball.r >= HEIGHT:
        ball.dy *= -1
    elif ball.y - ball.r <= 0:
        ball.dy *= -1

    ### player collisions:
    #player1
    if ball.dx < 0: #verify ball is going left (towards player1)
        if ball.y >= player1.y and ball.y <= player1.y + player1.height:
            if ball.x - ball.r <= player1.x + player1.width:
                ball.dx *= -1

                #determine ball.dy based on collision position on the player:  
                player_middle = player1.y - player1.height//2
                
    else: #ball is going right (towards player2)
        if ball.y >= player2.y and ball.y <= player2.y + player2.height:
            if ball.x + ball.r >= player2.x:
                ball.dx *= -1
FPS = 60
def draw_window(win, players, ball):
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, (WIDTH//2 - 2, 0, 4, HEIGHT))
    for player in players:
        player.draw(win)
    
    ball.draw(win)


    pygame.display.update() 


def main():
    #Game setup
    run = True
    clock = pygame.time.Clock()

    #initialize players
    player1 = Player(10, HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2 = Player(WIDTH - PLAYER_WIDTH - 10, HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)

    #initialize ball
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        #Player input and movements
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player1, player2)

        #Ball movement
        ball.move()
        ball_collision(ball,player1,player2)
        #Update window
        draw_window(WIN, [player1, player2], ball)

    pygame.quit()
    print('yup')

if __name__ == '__main__':
    main()
