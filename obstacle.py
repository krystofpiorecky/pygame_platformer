import pygame

class Obstacle:
    def __init__(self, screen, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen

    def draw(self):
        pygame.draw.rect(
            self.screen, 
            (255, 200, 255), 
            (
                self.x, 
                self.y, 
                self.width, 
                self.height
            ), 
            3
        )