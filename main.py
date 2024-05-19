from pygame import *
from random import*
font.init()
font2 = font.Font(None, 64)
clock = time.Clock()
window = display.set_mode((700,500))
display.set_caption("Догонялки")
background = transform.scale(image.load("rr.jpg"),(700,500))
class GameSPrite(sprite.Sprite):
        def __init__(self, player_image,player_x,player_y,player_speed,player_asd,player_hh):
            super().__init__()
            self.image = transform.scale(image.load(player_image),(player_asd,player_hh))
            self.speed = player_speed
            self.speedX = player_speed
            self.speedY = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def reset(self):
            window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSPrite):
        def update(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_UP]:
                self.rect.y -= self.speed
            if keys_pressed[K_DOWN]:
                self.rect.y += self.speed
class Enemy(GameSPrite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
                self.rect.y -= self.speed
        if keys_pressed[K_s]:
                self.rect.y += self.speed
        

class Ball(GameSPrite):
    def update(self):
        global score1
        global score2
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.x <= 0:
            self.rect.x = 500
            score2  += 1
        if self.rect.x >= 650:
            score1 += 1
            
            self.rect.x = 100

        if self.rect.y <= 0:
            self.speedY *= -1
        if self.rect.y >= 450:
            self.speedY *= -1

        if sprite.collide_rect(sprite1, sprite3):
            self.speedX *= -1

        if sprite.collide_rect(sprite2, sprite3):
            self.speedX *= -1
        

sprite1 = Player("gg.png",630,200,5, 70,50)
sprite2 = Enemy("ll.webp",5,200,5, 70,50)
sprite3 = Ball("tt.png",30,80,5,50,50)
finish = False
game = True
score1 = 0
score2 = 0

test1 = True
test2 = True

while game:
    if finish!= True:
        window.blit(background,(0,0))
        sprite1.reset()
        sprite1.update()
        sprite2.reset()
        sprite2.update()
        sprite3.reset()
        sprite3.update()

    
    if score1 == 5:
        if test1 == True:
            sprite1.image = transform.scale(image.load('gg.png'),(150,100))
            sprite1.rect = sprite1.image.get_rect()
            sprite1.rect.x = 550
            test1 = False
    if score2 == 5:
         if test2 == True:
            sprite2.image = transform.scale(image.load('ll.webp'),(150,100))
            sprite2.rect = sprite2.image.get_rect()
            sprite2.rect.x = 10
            test2 = False
    if score1 >= 6:
        text3 = font2.render("Игрок справа проиграл",True,(255,0,0))
        window.blit(text3,(100,250))
        finish = True
    if score2 >= 6:
        text3 = font2.render("Игрок слева  проиграл",True,(255,0,0))
        window.blit(text3,(100,250))
        finish = True
    text1 = font2.render(str(score1) + ':' + str(score2),True,(255,0,0))
    window.blit(text1,(300,10))
    
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        
    display.update()
    clock.tick(75)

