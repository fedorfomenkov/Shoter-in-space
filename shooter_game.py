from pygame import *
from random import *
windov = display.set_mode((700, 500))
display.set_caption('Игра про тарелки и ракету')
backgroud = transform.scale(image.load('galaxy.jpg'), (700, 500))
game = True
clock = time.Clock()
font.init()
font2 = font.SysFont('Arial', 36)
font3 = font.SysFont('Arial', 36)
font4 = font.SysFont('Arial', 100)
font5= font.SysFont('Arial', 100)
score = 0
lost = 0







class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, player_speed, player_h, player_w):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(player_h, player_w))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def reset(self):
        windov.blit(self.image, (self.rect.x, self.rect.y))
   
   

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_d] and self.rect.x<600:
            self.rect.x += self.speed
        if key_pressed[K_a]:
            self.rect.x -= self.speed 
    
    def fier(self):
        
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

class Anemy(GameSprite):
    def update(self):
        global lost
        
         
        
        self.rect.y+= self.speed
        if self.rect.y >=500:            #################################
            self.rect.y = 0
            lost += 1
            self.rect.x = randint(50, 600)

        


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <0:
            self.kill()

bullets = sprite.Group()


raceta = Player('rocket.png', 300, 400, 7, 100, 100)

#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()
#shot = mixer.Sound('fire.ogg')
#lose = mixer.Sound('start-igryi.ogg')


monster = sprite.Group()
for i in range(1, 11):
    enemy = Anemy('ufo.png', randint(50, 650), 0, randint(1, 2), 80, 80)
    monster.add(enemy)

cf = ' '
coe = 1
finish = False
while game:
    if not finish :
        text = font2.render('пропущено: ' +str(lost), 1, (225, 225, 225))
        text2 = font3.render('убито: ' +str(score), 1, (225, 225, 225))
        text3 = font4.render(('ТЫ ВЫИГРАЛ'), 1, (234, 255, 0))
        text4 = font5.render('ТЫ ПРОИГРАЛ :(', 1, (234, 255, 0))
        windov.blit(backgroud, (0, 0))
        windov.blit(text, (0, 0))
        windov.blit(text2, (0, 50))
        raceta.reset()
        raceta.update()
        monster.draw(windov)
        monster.update()
        bullets.update()
        bullets.draw(windov)
        sprite_list = sprite.groupcollide(monster, bullets, True, True)
        if len(sprite_list) == coe:
            score = score + 1
                                                            ####################################################################
            
        sprites_list = sprite.spritecollide(raceta, monster, False)

        if len(sprites_list) != 0:
            windov.blit(backgroud, (0, 0))
            
            windov.blit(text4, (100, 200))
            
        

            

        if score >= 10:
            windov.blit(backgroud, (0, 0))
            windov.blit(text3,(100, 200))
            finish = True
    
            
        
        if lost >= 3:                                 #########################15 ,skj
            windov.blit(backgroud, (0, 0))
            windov.blit(text4, (100, 200))
            finish = True


        
    for e in event.get():  
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                raceta.fier()


    display.update()
    clock.tick(60)





