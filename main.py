import sys
from random import randint
import pygame


class StarField:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Star Field')
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.window_width = 800
        self.window_height = 500
        self.display_surface = pygame.display.set_mode((self.window_width, self.window_height))
        
        self.speed = 5
        self.number_of_stars = 200
        self.stars = []
        for star in range(0,self.number_of_stars):
            self.stars.append(Star(self.window_width, self.window_height, self.speed))

    def update(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.display_surface.fill(0)

            for star in self.stars:
                star.update()
                star.draw()

            pygame.draw.ellipse(self.display_surface, 0, ((self.window_width/2)-5,(self.window_height/2)-5, 10,10), width=0)

            pygame.display.update()
            self.clock.tick(self.fps)


class Star:
    def __init__(self, window_width, window_height, speed):
        self.display_surface = pygame.display.get_surface()
        self.window_width = window_width
        self.window_height = window_height
        self.speed = speed

        self.x_offset = self.window_width/2
        self.y_offset = self.window_height/2
        
        self.x = randint(-self.window_width/2, self.window_width/2)
        self.y = randint(-self.window_height/2, self.window_height/2)
        
        self.start_x = self.x
        self.start_y = self.y

        self.z = randint(1500, 2000)

    def reset_position(self):
        self.x = randint(-self.window_width/2, self.window_width/2)
        self.y = randint(-self.window_height/2, self.window_height/2)
        self.z = randint(1500, 2000)
        self.start_x = self.x
        self.start_y = self.y

    def update(self):
        self.hyperspeed = True if self.speed > 50 else False
        self.z -= 10
        if abs(self.x) > self.window_width/2 or abs(self.y) > self.window_height/2 or self.z <= 0:
            self.reset_position()
        self.x += self.speed*(self.x/self.z)
        self.y += self.speed*(self.y/self.z)

        star_size = 0.002*(2000.0 - self.z)

        self.star_rect = pygame.Rect(self.x+self.x_offset, self.y+self.y_offset, star_size +1, star_size +1)

    def draw(self):
        if self.hyperspeed:
            pygame.draw.line(
                self.display_surface, 
                (20, 20, 20), 
                (self.start_x+self.x_offset, self.start_y+self.y_offset), (self.x+self.x_offset, self.y+self.y_offset), 
                width=1
            )
        pygame.draw.ellipse(self.display_surface, (200, 200, 200), self.star_rect, width=0)

     
if __name__ == '__main__':
    starfield = StarField()
    starfield.update()
