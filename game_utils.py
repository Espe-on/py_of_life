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
        
        neighbours= list(filter(lambda c: c in positions, neighbours)) # filter the neighbours list based on if they're in the live positions passed to this functions
        
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
    # there are 8 neighbours to a given position (given here as a tuple), this will return a list of those neighbours
    x, y = position
    neighbours = []
    for dx in [-1, 0 , 1]:
        if x + dx < 0 or x + dx > GC.GRID_WIDTH: # picks up x values which are off the screen
            continue
        for dy in [-1, 0 , 1]:
            if y + dy < 0 or y + dy > GC.GRID_HEIGHT: # picks up y values which are off the screen 
                continue
            if dx == 0 and dy == 0:
                continue
            
            neighbours.append((x + dx , y + dy))
    return neighbours
