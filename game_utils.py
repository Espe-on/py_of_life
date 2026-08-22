import random
from gameconstants import GAMECONSTANTS as GC
import pygame


GAMECONSTANTS = {
    "BLACK" : (0, 0, 0),
    "GREY" : (123, 123, 123),
    "YELLOW" : (255, 255, 0),
    "WIDTH" : 800, 
    "HEIGHT" :800,
    "TILE_SIZE" : 20,
    "FPS": 60
}

def genPos(number):
    return set([(random.randrange(0, GC.GRID_HEIGHT), random.randrange(0, GC.GRID_WIDTH)) for _ in range(number)])

def draw_grid(positions, screen):
    for position in positions:
        column, row = position
        top_left = (column * GC.TILE_SIZE, row * GC.TILE_SIZE)
        pygame.draw.rect(screen, GC.Colours["YELLOW"], (*top_left, GC.TILE_SIZE, GC.TILE_SIZE))
    
    for row in range(GC.GRID_HEIGHT):
        pygame.draw.line(screen, GC.Colours["BLACK"], (0, row * GC.TILE_SIZE), (GC.WIDTH, row * GC.TILE_SIZE))
    for column in range(GC.GRID_WIDTH):
        pygame.draw.line(screen, GC.Colours["BLACK"], (column * GC.TILE_SIZE, 0), (column * GC.TILE_SIZE, GC.HEIGHT))
