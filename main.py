import pygame
import random
from gameconstants import GAMECONSTANTS as GC
import game_utils

pygame.init()


screen = pygame.display.set_mode((GC.WIDTH,GC.HEIGHT))

clock = pygame.time.Clock()

def main():
    running = True
    playing = False
    positions = set()

    while running: 
        clock.tick(GC.FPS)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running =  False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    colum = x // GC.TILE_SIZE
                    row = y // GC.TILE_SIZE
                    pos = (colum, row)
                    
                    if pos in positions:
                        positions.remove(pos)
                    else:
                        positions.add(pos)
            
            if event.type == pygame.KEYDOWN:
                match event.key :
                    case pygame.K_SPACE:
                        playing = not playing
                    case pygame.K_c:
                        positions = set()
                        playing = False
                    case pygame.K_r:
                        positions = game_utils.genPos(random.randrange(4, 10) * GC.GRID_WIDTH)
                    
        
        screen.fill(GC.Colours["GREY"])
        game_utils.draw_grid(positions, screen)     
        pygame.display.update()      
    pygame.quit()
    
if __name__ == "__main__":
    main() 