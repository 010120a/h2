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
display.set_caption('шутер')

speedy = 3
speedx = 3
max_y1 = 50
max_y2 = 450

background = transform.scale(image.load('galaxy.jpg'), (700, 500))

player1 = player('sprite.png', 630, 400, 10, 25, 95)
player2 = player('sprite.png', 50, 400, 10, 25, 95)
ball = GameSprite('asteroid.png',350, 250, 10, 50, 50)

font.init()
font1 = font.SysFont('Arial', 36)
WIN = font1.render('YOU WIN', True, (0, 200, 0))
LOSE = font1.render('YOU LOSE', True, (255, 0, 0))

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
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speedx *= -1

        if sprite.collide_rect(max_y1, ball) or sprite.collide_rect(max_y2, ball):
            speedy *= -1
            
        ball.reset()
        player1.update()
        player1.reset()
        player2.update2()
        player2.reset()
    clock.tick(FPS)
    display.update()