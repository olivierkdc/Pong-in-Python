### Import libraries
import pygame

### Import players class
from Player import Player
from Ball import Ball


pygame.init()
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
def player_movement(keys_pressed, player1, player2):
    #Player1 
    if keys_pressed[pygame.K_w] and player1.y - player1.VELOCITY >= 0:
        player1.move(up=True)
    if keys_pressed[pygame.K_s] and player1.y + player1.height + player1.VELOCITY <= HEIGHT:
        player1.move(up=False)
    
    #Player2
    if keys_pressed[pygame.K_UP] and player2.y - player2.VELOCITY >= 0:
        player2.move(up=True)
    if keys_pressed[pygame.K_DOWN] and player2.y + player2.height + player2.VELOCITY <= HEIGHT:
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

                #determine ball.dy based on collision position on player1:  
                player_middle = player1.y + player1.height//2
                height_differential = player_middle - ball.y
                reduct = (player1.height //2 ) / ball.VELOCITY
                ball.dy = -height_differential / reduct
                
    else: #ball is going right (towards player2)
        if ball.y >= player2.y and ball.y <= player2.y + player2.height:
            if ball.x + ball.r >= player2.x:
                ball.dx *= -1

                #determine ball.dy based on collision position on player2:
                player_middle = player2.y + player2.height//2
                height_differential = player_middle - ball.y
                reduct = (player2.height //2 ) / ball.VELOCITY
                ball.dy = -height_differential / reduct



'''
POINTS
'''
point_font = pygame.font.SysFont("Segoe UI", 26)
round_start_font = pygame.font.SysFont("Segoe UI", 50)

def draw_window(win, players, ball, player1_points, player2_points, round_start):
    #fill background and middle divider
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, (WIDTH//2 - 2, 0, 4, HEIGHT))

    #Round Start Text
    round_start_text = round_start_font.render('Press Spacebar to launch the ball', 1, WHITE)
    if round_start == 0:
        win.blit(round_start_text, (WIDTH//2 - round_start_text.get_width()//2, HEIGHT//2 - round_start_text.get_height()//2))

    #generate and draw score
    points1_text =  point_font.render(f"{player1_points}", 1, WHITE)
    points2_text =  point_font.render(f"{player2_points}", 1, WHITE)
    win.blit(points1_text, (WIDTH//10 - points1_text.get_width()//2, 20))
    win.blit(points2_text, (WIDTH - WIDTH//10 - points2_text.get_width()//2, 20))

    #draw players
    for player in players:
        player.draw(win)
    
    #draw ball
    ball.draw(win)
    #update window
    pygame.display.update() 


POINTS_TO_WIN = 5
FPS = 60
def main():
    #Game setup
    run = True
    clock = pygame.time.Clock()

    #initialize players
    player1 = Player(10, HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2 = Player(WIDTH - PLAYER_WIDTH - 10, HEIGHT//2 - PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)
    players = [player1, player2]
    #initialize ball
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)
    round_start = 0
    #initialize points
    player1_points, player2_points = 0, 0
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        #Player input and movements
        keys_pressed = pygame.key.get_pressed()
        player_movement(keys_pressed, player1, player2)

        #Ball movement and round start
        if keys_pressed[pygame.K_SPACE]:
            round_start = 1
        if round_start > 0:
            ball.move()
        ball_collision(ball,player1,player2)

        #Add points and reset rounds
        if ball.x > WIDTH:
            player1_points += 1
            ball.initialize()
            for player in players:
                player.initialize()
            round_start = 0
        if ball.x < 0:
            player2_points += 1
            ball.initialize()
            for player in players:
                player.initialize()
            round_start = 0
        
        player_won = False
        if player1_points == POINTS_TO_WIN:
            player_won = True
            victory_text = 'Player 1 is victorious!'
        
        elif player2_points == POINTS_TO_WIN:
            player_won = True
            victory_text = 'Player 2 is victorious!'

        if player_won == True:
            end_text = round_start_font.render(victory_text, 1, WHITE)
            WIN.blit(end_text, (WIDTH//2 - end_text.get_width()//2, HEIGHT//2 - end_text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(3000)

        #Update window
        draw_window(WIN, [player1, player2], ball, player1_points, player2_points, round_start)

    pygame.quit()
    print('yup')

if __name__ == '__main__':
    main()
