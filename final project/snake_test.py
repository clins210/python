"""
2020.01.09
Snake Game
Made with PyGame
"""
import pygame, sys, time, random, os
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
Hellloooooo
