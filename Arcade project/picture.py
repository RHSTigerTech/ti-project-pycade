import pygame
QUOTES = ['There is 10 minutes left, I am playing clash', 'Is it because I am disabled', 'Devin stinks', 'lol this quote is to long to fit in this tiny box. bug', 'Sean is such a Calvert']

class Picture(pygame.sprite.Sprite):
    def __init__(self, img, pos):
        super().__init__()

        pygame.font.init()
        FONT = pygame.font.Font('freesansbold.ttf', 50)
        
        self.name = img

        #catch all quotes:
        if img in QUOTES:
            quote = FONT.render(str(img),True, (255, 255, 255))
            self.image = quote



        #object variables
        else:
            self.image = pygame.image.load(img).convert_alpha()

        #generate hitbox/position
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        # 3 games slide in:
        if self.name in ['Crocketdile4.jpg', 'chads_quest_small.png']:
            if self.rect.y > 400:
                self.rect.y -= 1
