from pygame import *
from random import*

clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption("Догонялки")
background = transform.scale(image.load("gg.png"),(700,500))
class GameSPrite(sprite.Sprite):
        def __init__(self, player_image,player_x,player_y,player_speed):
            super().__init__()
            self.image = transform.scale(image.load(player_image),(15,70))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def reset(self):
            window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSPrite):
        def update(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_w]:
                self.rect.y -= self.speed
            if keys_pressed[K_s]:
                self.rect.y += self.speed
            if keys_pressed[K_a]:
                self.rect.x -= self.speed
            if keys_pressed[K_d]:
                self.rect.x += self.speed


class Enemy(GameSPrite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]:
         self.rect.y += self.speed
        if keys_pressed[K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT]:
            self.rect.x += self.speed

sprite1 = Player("ll.jpg",300,50,5)
sprite2 = Enemy("rr.webp",300,50,5)

finish = False
game = True
while game:
    if finish!= True:
        window.blit(background,(0,0))
    
   


    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
    
    
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        sprite1.reset()
        sprite1.update()
        sprite2.reset()
        sprite2.update()
        display.update()
        clock.tick(300)
