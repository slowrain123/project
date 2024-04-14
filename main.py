from pygame import *
from random import*

clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption("Догонялки")
background = transform.scale(image.load("gg.jpg"),(700,500))
class GameSPrite(sprite.Sprite):
        def __init__(self, player_image,player_x,player_y,player_speed,player_asd,player_hh):
            super().__init__()
            self.image = transform.scale(image.load(player_image),(player_asd,player_hh))
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


class Ball(GameSPrite):
    directionX = 'left'
    directionY = "up"
    def update(self):
        if self.rect.x <= 0:
            self.directionX = "right"
        if self.rect.x >= 700:
            self.directionX = "left"
        if self.directionX == "left":
            self.rect.x -= self.speed
        if self.directionX == "right":
            self.rect.x += self.speed


        if self.rect.y <= 0:
            self.directionY = "down"
        if self.rect.y >= 450:
            self.directionY = "up"
        if self.directionY == "up":
            self.rect.y -= self.speed
        if self.directionY == "down":
            self.rect.y += self.speed
            


sprite1 = Player("gg.png",300,50,5, 70,50)
sprite2 = Enemy("ll.webp",300,50,5, 70,50)
sprite3 = Ball("tt.png",50,50,5,70,50)
finish = False
game = True
while game:
    if finish!= True:
        window.blit(background,(0,0))
        sprite1.reset()
        sprite1.update()
        sprite2.reset()
        sprite2.update()
        sprite3.reset()
        sprite3.update()
        display.update()



    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
    
    
    
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    clock.tick(60)

