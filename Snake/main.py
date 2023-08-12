import sys

import pygame

import random

from utils.snake import Snake
from utils.lines import Lines
from utils.apple import Apple

class Game():
    def __init__( self ):
        pygame.init()

        self.screen_size = 601
        self.row = 20
        self.screen = pygame.display.set_mode( ( self.screen_size, self.screen_size ) ) 

        self.font = pygame.font.SysFont('Segoe', 26)
        self.lost_font = pygame.font.SysFont('Segoe', 50)

        self.clock = pygame.time.Clock()

        self.score = 0

        self.lines = Lines( self.screen_size, self.row )
        self.snake = Snake( self.screen_size, self.row )
        self.apple = Apple( self.screen_size, self.row )

        self.move = [0, 0]

    def draw_score(self):
        self.score_text = self.font.render('Score: ' + str(self.score), True, (255, 255, 255))
        self.screen.blit(self.score_text, (10, 10))

    def draw_apple(self):
        pygame.draw.rect(self.screen, self.apple.color, (self.apple.place[0], self.apple.place[1], self.apple.size, self.apple.size))    

    def draw(self, draw_spacing = 0):
        #lines
        for i in range(self.row): 
            if draw_spacing == 0:
                pygame.draw.lines(self.screen, (255, 255, 255), False, [(0,draw_spacing), (self.screen_size - 1,draw_spacing)], 1)
                pygame.draw.lines(self.screen, (255, 255, 255), False, [(draw_spacing,0), (draw_spacing, self.screen_size - 1)], 1)
                draw_spacing = self.lines.row_spacing - 1
            
            pygame.draw.lines(self.screen, (255, 255, 255), False, [(0,draw_spacing), (self.screen_size - 1,draw_spacing)],1)
            pygame.draw.lines(self.screen, (255, 255, 255), False, [(draw_spacing,0), (draw_spacing,self.screen_size - 1)],1)
        
            draw_spacing += self.lines.row_spacing

        #snake
        for i in range(len(self.snake.body_x)):
            pygame.draw.rect(self.screen, self.snake.color, (self.snake.body_x[i], self.snake.body_y[i], self.snake.size, self.snake.size))

    def events( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.move = [0,-1]

                elif event.key == pygame.K_a:
                    self.move = [-1,0]

                elif event.key == pygame.K_d:
                    self.move = [1,0]

                elif event.key == pygame.K_s:
                    self.move = [0,1]

    def apple_place(self, tests =True):

        while tests:
            x = random.randrange(self.row)
            y = random.randrange(self.row)
            self.apple.place = [ self.apple.map_up_left_corner[0] + x * ( ( self.apple.size ) + 1 ),self.apple.map_up_left_corner[1] + y * ( ( self.apple.size ) + 1 ) ]

            for i in range(len(self.snake.body_x)):
                if self.apple.place[0] == self.snake.body_x[i] and self.snake.body_y[i] == self.apple.place[1]:
                    break
            else:
                tests = False

        if self.apple.place[0] == 0:
            self.apple.place[0] = 1

        if self.apple.place[1] == 0:
            self.apple.place[1] = 1



    def eat_apple(self):
        if self.apple.place == []:
            self.apple_place()

        elif self.snake.body_x[0] == self.apple.place[0] and self.snake.body_y[0] == self.apple.place[1]:
            self.apple_place()
            self.snake.move(self.move [0], self.move [1],False)
            self.score += 1

        self.draw_apple()                
        self.snake.move(self.move [0], self.move [1], True)
    

    def draw_lost(self):
            self.lose_text = self.lost_font.render( self.lose, True, (255, 0, 0))
            self.screen.blit(self.lose_text, (50, 235))
            pygame.display.update()

    def lost_check(self):
        self.lost = False

        for i in range(len(self.snake.body_x)):
            if self.snake.body_x[i] < 0 or self.snake.body_y[i] < 0 or self.snake.body_x[i] >= 600 or self.snake.body_y[i] >= 600:
                self.lost = True
                self.lose = "You crushed against the wall"
                break
            for j in range(len(self.snake.body_x)):
                if self.snake.body_x[i] == self.snake.body_x[j] and self.snake.body_y[i] == self.snake.body_y[j] and i != j:
                    self.lost = True
                    self.lose = "You eated Your self"

                    break
        if self.lost == False:
            self.eat_apple()
        else:
            self.draw_lost()

    def run( self ):
        while True:
            pygame.display.set_caption('Snake by Adrian Jarząb')

            pygame.time.delay(160)
            self.clock.tick(10)
            self.events()
            
            self.lost_check()
            self.draw()
            self.draw_score()

            if self.lost == False:
                pygame.display.update()
                self.screen.fill((0,0,0))

Game().run()

