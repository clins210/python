"""
Snake Game
Made with PyGame
"""

import pygame, sys, time, random


# Initialize pygame and check for errors encountered
check_errors = pygame.init()
if check_errors[1] > 0:
    print('Had {} errors when initialising game, exiting...'.format(check_errors[1]))
    sys.exit(-1)


# frame, window and model initialization
frame_size_x = 720
frame_size_y = 640
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
pygame.display.set_caption('Snake')


# Game variables
# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

snake_head = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_x = random.randrange(1, (frame_size_x//10)) * 10
food_y = random.randrange(1, (frame_size_y//10)) * 10
food_pos = [food_x, food_y]
food_spawn = True

change_to = direction = 'RIGHT'

score = 0
over = 0


def game_over():
    """
    the final show frame setting after game over
    """
    my_font = pygame.font.SysFont('times new roman', 90)
    my_font2 = pygame.font.SysFont('times new roman', 36)
    game_over_surface = my_font.render('GG', True, red)
    game_over_surface2 = my_font2.render('< Press ESC To Exit >', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect2 = game_over_surface2.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_over_rect2.midtop = (frame_size_x/2, frame_size_y/3+30)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_over_surface2, game_over_rect2)

    show_score(0, red, 'times', 100)
    # Refresh game screen
    pygame.display.flip()
    time.sleep(1)

    return 1 


def end():
    """
    the event of quit the game
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    

def show_score(choice, color, font, size):
    """
    the tiltle initialization, ex: "Score: 0"
    """
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)


# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:

            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'

            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))


    # change(and store) the direciton
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    
    # the movement in different direction
    if direction == 'UP':
        snake_head[1] -= 10
    if direction == 'DOWN':
        snake_head[1] += 10
    if direction == 'LEFT':
        snake_head[0] -= 10
    if direction == 'RIGHT':
        snake_head[0] += 10


    # snake body extension
    snake_body.insert(0, list(snake_head))
    if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()


    # Spawning food on the screen
    if not food_spawn:
        food_x = random.randrange(1, (frame_size_x//10)) * 10
        food_y = random.randrange(1, (frame_size_y//10)) * 10
        food_pos = [food_x, food_y]
    food_spawn = True


    # Display
    game_window.fill(black)

    # Draw Snake
    for pos in snake_body:
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))


    # gameover_condition: head out of frame
    if snake_head[0] < 0 or snake_head[0] > frame_size_x-10:
        over = game_over()
        end()
    if snake_head[1] < 0 or snake_head[1] > frame_size_y-10:
        over = game_over()
        end()
    # gameover_condition: head & body touching
    for block in snake_body[1:]:
        if snake_head[0] == block[0] and snake_head[1] == block[1]:
            over = game_over()
            end()


    if not over:
        show_score(1, white, 'consolas', 10)
        # Refresh game screen
        pygame.display.update()
        # Refresh rate
        pygame.time.Clock().tick(10)
