# This code was created by Matthew Garza

# # this is where we import libraries and modules
# import pygame as pg
# from settings import *
# # from sprites import *
# from sprites_side_scroller import *
# from tilemap import *
# from os import path
# import sys 
# # we are editing this file after installing git

# '''
# GOALS: avoid the rising lava while collecting as many coins as possible
# RULES: jump, get powerups, and avoid mobs that will slow you down
# FEEDBACK: add timer, health system, make mobs do damage, (add a map with two players)
# FREEDOM:

# What's the sentence: Player 1 collides with enemy and enemy bounces off...

# '''


# '''
# put all sources here:
# Mr. Cozort

# '''



# # create a game class that carries all the properties of the game and methods
# class Game:
#   # initializes all the things we need to run the game...includes the game clock which can set the FPS
#   def __init__(self):
#     pg.init()
#     # sound mixer...
#     pg.mixer.init()
#     self.clock = pg.time.Clock()
#     self.screen = pg.display.set_mode((WIDTH, HEIGHT))
#     pg.display.set_caption("Garzas' Coolest Game Ever...")
#     self.playing = True
#   # this is where the game creates the stuff you see and hear
#   def load_data(self):
#     self.game_folder = path.dirname(__file__)
#     self.map = Map(path.join(self.game_folder, 'level1.txt'))
#     self.map = Map(path.join(self.game_folder, 'level2.txt'))
#     self.map = Map(path.join(self.game_folder, 'level3.txt'))
#     # self.map = Map(path.join(self.game_folder, 'level4.txt'))
#     # self.map = Map(path.join(self.game_folder, 'level5.txt'))
#   def new(self):
#     self.load_data()
#     print(self.map.data)
#     # create the all sprites group to allow for batch updates and draw methods
#     self.all_sprites = pg.sprite.Group()
#     self.all_walls = pg.sprite.Group()
#     self.all_powerups = pg.sprite.Group()
#     self.all_coins = pg.sprite.Group()
#     self.all_nerfs = pg.sprite.Group()
#     self.all_boost = pg.sprite.Group()
#     self.all_mobs = pg.sprite.Group()
#     self.all_lava = pg.sprite.Group()
#     # self.all.pew_pew = pg.sprite.Group()
#     # instantiating the class to create the player object 
#     # self.player = Player(self, 5, 5)
#     # self.mob = Mob(self, 100, 100)
#     # self.wall = Wall(self, WIDTH//2, HEIGHT//2)
#     # # instantiates wall and mob objects
#     # for i in range(12):
#     #   Wall(self, TILESIZE*i, HEIGHT/2)
#     #   Mob(self, TILESIZE*i, TILESIZE*i)
#     for row, tiles in enumerate(self.map.data):
#       print(row*TILESIZE)
#       for col, tile in enumerate(tiles):
#         print(col*TILESIZE)
#         if tile == '1':
#           Wall(self, col, row)
#         if tile == 'M':
#           Mob(self, col, row)
#         if tile == 'P':    
#           self.player = Player(self, col, row)
#         if tile == 'U':
#           Powerup(self, col, row)
#         if tile == 'C':
#           Coin(self, col, row)
#         if tile == 'N':
#           Nerf(self,col,row)
#         if tile == 'B':
#           Boost(self,col,row)
#         if tile =='L':
#           Lava(self,col,row)
#         if tile == 'O':
#           Moving_Platform(self,col,row)
          


# # this is a method
# # methods are like functions that are part of a class
# # the run method runs the game loop
#   def run(self):
#     while self.playing:
#       self.dt = self.clock.tick(FPS) / 1000
#       # input
#       self.events()
#       # process
#       self.update()
#       # output
#       self.draw()
#   def quit(self):
#     pg.quit()
#     sys.exit


#   pg.quit()
#   # input
#   def events(self):
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#           self.playing = False
#   # process
#   # this is where the game updates the game state
#   def show_death_screen(self):
#         self.screen.fill(RED)
#         self.draw_text("Game Over!", 42, WHITE, WIDTH / 2, HEIGHT / 2)
#         self.draw_text("Press any key to restart", 32, WHITE, WIDTH / 2, HEIGHT / 2 + 50)
#         pg.display.flip()
#         self.wait_for_key()
#         #the screem that shows up once player runs out of lives
        
#   def update(self):
#     # update all the sprites...and I MEAN ALL OF THEM
#     self.all_sprites.update()

#     if self.player.lives <= 0:
#         self.playing = False
#         self.show_death_screen()

#     if self.player.lives == 0:
#        self.show_death_screen()
#        self.run = False
    
#     def update(self):
#     # Update all sprites
#       self.all_sprites.update()

#     # Check for collisions with lava
#     for lava in self.all_lava:
#         lava.rect.y -= LAVA_RISE_SPEED * self.dt  # Move each lava sprite
#         if lava.rect.colliderect(self.player.rect):  # Check collision with the player
#             self.player.lives = 0

#     # End the game if player is out of lives
#     if self.player.lives <= 0:
#         self.playing = False
#         self.show_death_screen()


#   def draw_text(self, surface, text, size, color, x, y):
#     font_name = pg.font.match_font('arial')
#     font = pg.font.Font(font_name, size)
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect()
#     text_rect.midtop = (x,y)
#     surface.blit(text_surface, text_rect)

#   # output
#   def draw(self):
#     self.screen.fill(BLACK)
#     self.all_sprites.draw(self.screen)
#     self.draw_text(self.screen, str(self.dt*1000), 24, WHITE, WIDTH/30, HEIGHT/30)
#     self.draw_text(self.screen, str(self.player.coin_count), 24, WHITE, WIDTH-100, 50)
#     self.draw_text(self.screen, "lives:" + str(self.player.lives), 24, WHITE, WIDTH -45,HEIGHT -32)
#     pg.display.flip()

# def show_death_screen(self):
#     self.screen.fill(RED)
#     self.draw_text(self.screen, "Game Over!", 42, WHITE, WIDTH / 2, HEIGHT / 2)
#     self.draw_text(self.screen, "You were consumed by the lava.", 32, WHITE, WIDTH / 2, HEIGHT / 2 + 50)
#     pg.display.flip()
#     self.wait_for_key()

# def show_death_screen(self):
#     self.screen.fill(RED)
#     self.draw_text(self.screen, "You Died!!!", 42, WHITE, WIDTH / 2, HEIGHT / 2)
#     self.draw_text(self.screen, "Press any key to restart", 32, WHITE, WIDTH / 2, HEIGHT / 2 + 50)
#     pg.display.flip()
#     self.wait_for_key()
# def wait_for_key(self):
#     waiting = True
#     while waiting: 
#         self.clock.tick(FPS)
#         for event in pg.event.get():
#             if event.type == pg.QUIT:
#                 waiting = False
#                 self.quit()
#             if event.type == pg.KEYUP:  # Any key is pressed
#                 waiting = False
#                 self.new()  # Restart the game
#                 self.run()  # Begin the game loop again

# if __name__ == "__main__":
#   # instantiate
#   print("main is running...")
#   g = Game()
#   print("main is running...")
#   g.new()
#   g.run()
#   g.show_death_screen