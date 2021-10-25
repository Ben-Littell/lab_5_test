import pygame
import math
import random

# colors in RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
sand = (194, 178, 128)
sea_blue = (0, 105, 148)
brown = (165, 42, 42)
COLORS = [RED, GREEN, BLUE, BLACK]

# animation variables
clouds_corner = 50
x_center_boat = 40
boat_height = 300
boat_movement = 1

# Math Constants
PI = math.pi
HEIGHT = 500
WIDTH = 700
# Game Constants
SIZE = (WIDTH, HEIGHT)
FPS = 60

########################################################################################################################

'''
class Rocket:
    def __init__(self, height, width, center, color1, color2):
        self.height = height
        self.width = width
        self.color1 = color1
        self.color2 = color2
        self.center = center

    def draw_rocket(self):
        # cone
        pygame.draw.polygon(screen, BLACK, [(self.center-self.width//2, self.height+50),
                                            (self.center+self.width//2, self.height+50),
                                            (self.center, self.height)])
        # body
        pygame.draw.rect(screen, BLACK, (self.center-self.width//2, self.height+50, self.width, self.height-25))
        # thruster
        pygame.draw.polygon(screen, BLACK, [(self.center-self.width//2, self.height+300),
                                            (self.center+self.width//2, self.height+300),
                                            (self.center-self.width//2-15, self.height+300)])

'''


class Clouds:
    def __init__(self, color):
        self.color = color

    def draw_clouds(self, top_left_x):
        cloud_x1 = top_left_x
        cloud_x2 = top_left_x + 10
        cloud_x3 = top_left_x - 10
        cloud_x4 = top_left_x + 25
        for numb in range(3):
            change_cx = numb * 110
            change_cy = numb * 20
            pygame.draw.ellipse(screen, self.color, (cloud_x1 + change_cx, 30 + change_cy, 50, 30))
            pygame.draw.ellipse(screen, self.color, (cloud_x2 + change_cx, 45 + change_cy, 50, 30))
            pygame.draw.ellipse(screen, self.color, (cloud_x3 + change_cx, 35 + change_cy, 50, 30))
            pygame.draw.ellipse(screen, self.color, (cloud_x4 + change_cx, 33 + change_cy, 50, 30))


class Boat:
    def __init__(self, b_x_cord, b_y_cord, sail_c, mast_c, boat_c):
        self.x_cord = b_x_cord
        self.y_cord = b_y_cord
        self.sail_c = sail_c
        self.mast_c = mast_c
        self.boat_c = boat_c

    def draw_boat(self):
        # mast
        pygame.draw.rect(screen, self.mast_c, (self.x_cord - 3, self.y_cord + 10, 6, 40))
        # sail
        pygame.draw.polygon(screen, self.sail_c, [(self.x_cord, self.y_cord),
                                                  (self.x_cord - 20, self.y_cord + 30),
                                                  (self.x_cord + 20, self.y_cord + 30)])
        pygame.draw.ellipse(screen, self.boat_c, (self.x_cord - 20, self.y_cord + 40, 40, 20))


########################################################################################################################

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Animation Intro')

clock = pygame.time.Clock()
running = True
# game loop
clouds = Clouds(WHITE)
while running:
    boats = Boat(x_center_boat, boat_height, WHITE, brown, RED)
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clouds_corner += 3
    if clouds_corner > WIDTH + 1:
        clouds_corner = WIDTH - WIDTH - 285
    x_center_boat += boat_movement
    if x_center_boat >= WIDTH - 40:
        boat_movement = boat_movement * -1
    elif x_center_boat <= 20:
        boat_movement = boat_movement * -1

    screen.fill(WHITE)
    # Background
    pygame.draw.rect(screen, sand, [0, 400, 700, 100])
    pygame.draw.rect(screen, sea_blue, [0, 0, 700, 400])
    # clouds
    clouds.draw_clouds(clouds_corner)
    # boats
    boats.draw_boat()
    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()
