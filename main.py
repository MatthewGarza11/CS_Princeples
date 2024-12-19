
# This code was created by Matthew Garza
import pygame as pg
from settings import *  # Ensure settings.py defines WIDTH, HEIGHT, FPS, TILESIZE, etc.
from sprites_side_scroller import *   # Ensure these modules are correctly implemented.
from tilemap import *
from os import path
import sys


'''
 GOALS: avoid the rising lava while collecting as many coins as possible
 RULES: jump, get powerups, and avoid mobs that will slow you down
 FEEDBACK: health system, make mobs do damage, rising lava, death screen, finish point
 FREEDOM: player can move around the map with limited time until lava reaches them

# What's the sentence: Player 1 collides with enemy and enemy bounces off...
'''

# '''
# put all sources here:
# Mr. Cozort
# Chat GPT 
# Evan Choy 
# '''

class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Don't mess up!...")
        self.playing = True
        self.score = 0

    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.map = Map(path.join(self.game_folder, 'level3.txt'))
        try:
            with open(path.join(self.game_folder, HS_FILE), 'r') as f:
                self.highscore = int(f.read())
        except:
            self.highscore = 0
            with open(path.join(self.game_folder, HS_FILE), 'w') as f:
                f.write(str(0))

    def new(self):
        self.load_data()
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_powerups = pg.sprite.Group()
        self.all_coins = pg.sprite.Group()
        self.all_nerfs = pg.sprite.Group()
        self.all_boost = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_lava = pg.sprite.Group()
        self.all_player = pg.sprite.Group()
        self.all_finish_lines = pg.sprite.Group()

        # Initialize map objects based on the tilemap
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'U':
                    Powerup(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'N':
                    Nerf(self, col, row)
                if tile == 'B':
                    Boost(self, col, row)
                if tile == 'L':
                    Lava(self, col, row)
                if tile == 'O':
                    Moving_Platform(self, col, row)
                if tile == 'F':
                    FinishLine(self, col, row)

    def run(self):
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        # Save high score when quitting
        with open(path.join(self.game_folder, HS_FILE), 'w') as f:
            f.write(str(self.highscore))
        pg.quit()
        sys.exit()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

    def update(self):
        self.all_sprites.update()

        # Check collisions and game-ending conditions
        for lava in self.all_lava:
            lava.rect.y -= LAVA_RISE_SPEED * self.dt
            if lava.rect.colliderect(self.player.rect):
                self.player.lives = 0

        # Check for coin collection
        hits = pg.sprite.spritecollide(self.player, self.all_coins, True)  # True means remove the coin
        for hit in hits:
            self.player.coin_count += 1
            self.score += 1  # Increment the score when a coin is collected

        # Update high score if necessary
        if self.score > self.highscore:
            self.highscore = self.score

            # Save the new high score to the file
            with open(path.join(self.game_folder, HS_FILE), 'w') as f:
                f.write(str(self.highscore))


        # Check if player is out of lives
        if self.player.lives <= 0:
            self.playing = False
            self.show_death_screen()

        # Check if player reaches the finish line
        hits = pg.sprite.spritecollide(self.player, self.all_finish_lines, False)
        if hits:
            self.playing = False
            self.show_completion_screen()

    def show_death_screen(self):
        self.screen.fill(RED)
        self.draw_text("Game Over!", 42, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to restart", 32, WHITE, WIDTH / 2, HEIGHT / 2 + 50)
        pg.display.flip()
        self.wait_for_key()

    def show_completion_screen(self):
        self.screen.fill(BLUE)
        self.draw_text("Well Done!", 42, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("You finished the game!", 32, WHITE, WIDTH / 2, HEIGHT / 2 + 50)
        self.draw_text("Press any key to restart", 24, WHITE, WIDTH / 2, HEIGHT / 2 + 100)
        pg.display.flip()
        self.wait_for_key()
        #Asked chat gpt how to make a completion screen (i only needed to know how to make words show up in the middle of the screen)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYUP:  # Any key is pressed
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.draw_text(f"{self.dt * 1000:.1f} ms", 24, WHITE, WIDTH / 30, HEIGHT / 30)
        self.draw_text(f"Coins: {self.player.coin_count}", 24, WHITE, WIDTH - 100, 50)
        self.draw_text(f"Lives: {self.player.lives}", 24, WHITE, WIDTH - 100, HEIGHT - 30)
        self.draw_text(f"High Score: {self.highscore}", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        pg.display.flip()

if __name__ == "__main__":
    print("main is running...")
    while True:  # Loop to restart the game after death or completion
        g = Game()
        g.new()
        g.run()

        # Determine the ending condition
        if g.player.lives <= 0:
            g.show_death_screen()
        else:
            g.show_completion_screen()
#asked chatgpt how to make it so the completion screen only showed when you win