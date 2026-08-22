import random
from gameconstants import GAMECONSTANTS as GC
import pygame

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
        
def adjust_grid(positions):
    all_neighbours = set() #all of the neighbours of all current live cells
    new_positions = set() #all of the live cells for the next go around of the game

    #Go Through All Existing positions and see if they live (have 2 or 3 neighbours)
    for position in positions:
        neighbours = get_neighbours(position)
        all_neighbours.update(neighbours)
        
        neighbours= list(filter(lambda c: c in positions, neighbours))
        
        if len(neighbours) in [2,3]:
            new_positions.add(position)

    #Go Through all of the neighbours of the existing positions and see if they generate new tiles (have 3 neighbours)
    for position in all_neighbours:
        neighbours = get_neighbours(position)
        neighbours= list(filter(lambda c: c in positions, neighbours))
        
        if len(neighbours) == 3:
            new_positions.add(position)
    return new_positions


def get_neighbours(position):
    pass
