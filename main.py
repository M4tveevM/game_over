import pygame, os, sys


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Game_screen():
    def __init__(self):
        self.quit = False
        self.screen_init()
        self.start_ticks = pygame.time.get_ticks()
        self.runing()

    def screen_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode([800, 600])
        self.screen.fill('blue', ((0, 0), (800, 600)))
        self.all_sprites = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = load_image("gameover.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.all_sprites.add(self.sprite)
        self.sprite.rect.y = 0
        self.sprite.rect.x = -800

        pygame.display.flip()

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.quit = True

    def runing(self):
        while True:
            self.bg_new_locaton()
            pygame.display.flip()
            if self.quit:
                break
            for event in pygame.event.get():
                if self.quit:
                    break
                self.get_event(event)

    def bg_new_locaton(self):
        if self.sprite.rect.x <= 0:
            self.sprite.rect.x += 10
            self.all_sprites.draw(self.screen)



Game_screen()
