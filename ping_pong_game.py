from pygame import*
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, height, width):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (height, width))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 405:
            self.rect.y += self.speed

    def update2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y < 405:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
display.set_caption('ping_pong')

speedy = 3
speedx = 3

background = transform.scale(image.load('galaxy.jpg'), (700, 500))

player1 = player('sprite.png', 670, 400, 10, 25, 95)
player2 = player('sprite.png', 5, 400, 10, 25, 95)
ball = GameSprite('asteroid.png',350, 250, 10, 50, 50)

font.init()
font1 = font.SysFont('Arial', 36)
WIN = font1.render('WIN>>>', True, (0, 200, 0))
LOSE = font1.render('<<<WIN', True, (0, 200, 0))

clock = time.Clock()
FPS = 90
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_s.play()
                rocket.fire()
                
    if not finish:
        window.blit(background, (0, 0))
        ball.rect.x += speedx
        ball.rect.y += speedy

        if ball.rect.x < -50:
            finish = True
            restart_time = time.get_ticks()
            window.blit(WIN, (300, 250))

        if ball.rect.x > 700:
            finish = True
            restart_time = time.get_ticks()
            window.blit(LOSE, (300, 250))
        
        if ball.rect.y > 450 or ball.rect.y < 0:
            speedy *= -1

        if sprite.collide_rect(player1, ball):
            speedx *= -1
            ball.rect.right = player1.rect.left

        if sprite.collide_rect(player2, ball):
            speedx *= -1
            ball.rect.left = player2.rect.right
            
        ball.reset()
        player1.update()
        player1.reset()
        player2.update2()
        player2.reset()
    else:
        if time.get_ticks() - restart_time >= 2000:
            finish = False
            ball.rect.x = 700 // 2 - 25
            ball.rect.y = 500 // 2 - 25
            speedx *= -1
            speedy = 3
        
    clock.tick(FPS)
    display.update()
