import pygame
from map import Map
from person import Character
from bullet import Bullet
import random
import time
from playsound import playsound
from portal import Portal

text_team = input("enter the green's name ")
text_team2 = input("enter the red's name ")

pygame.init()
jumpcount = -10
BROWN = (150, 75, 0)
BLACK = (0, 0, 0)
GREEN = (51, 204, 51)
GOLD = (255, 255, 0)
PURPLE = (204, 0, 204)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
isJump = False
carryOn = True
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('shooting game(child friendly)')
Clock = pygame.time.Clock()
brick_on = Map((150, 75, 0), 50, 50)
brick_on.rect.x = 350
brick_on.rect.y = 450
brick_on2 = Map(BROWN, 150, 25)
brick_on2.rect.x = 175
brick_on2.rect.y = 390
brick_on3 = Map(BROWN, 150, 15)
brick_on3.rect.x = 115
brick_on3.rect.y = 260
person1 = Character(GREEN, 10, 20)
person1.rect.x = 50
person1.rect.y = 480
health = 100
person2 = Character(RED, 10, 20)
person2.rect.x = 400
person2.rect.y = 480
health2 = 100
bullet = Bullet(GOLD, 15, 10)
bullet.rect.x = 7000
bullet.rect.y = 8000
shoot_times = 0
fired = False
bullet2 = Bullet(RED, 15, 10)
bullet2.rect.x = 7000
bullet2.rect.x = 8000
shoot_times1 = 0
fired1 = False
friend = Portal(PURPLE, 75, 30)
friend.rect.x = 500
friend.rect.y = 300
portal = Portal(PURPLE, 75, 30)
portal.rect.x = 15
portal.rect.y = 300
heal = Portal(GREEN, 10, 10)
can_heal = 0
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(brick_on)
all_sprites_list.add(brick_on2)
all_sprites_list.add(person1)
all_sprites_list.add(bullet)
all_sprites_list.add(portal)
all_sprites_list.add(friend)
all_sprites_list.add(person2)
all_sprites_list.add(brick_on3)


while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        person1.moveRight(5)
    if keys[pygame.K_a]:
        person1.moveLeft(5)
    if keys[pygame.K_w]:
        # self.rect.y = -40 * math.sin(math.pi * self.rect.x / 16) + 40
        isJump = True
        person1.isJump = True
        person1.isFinished = False
        person1.Jump()
        if pygame.sprite.collide_mask(person1, brick_on):
            person1.rect.y = brick_on.rect.y - 23
            person1.isFinished = True
        if pygame.sprite.collide_mask(person1, brick_on2):
            person1.rect.y = brick_on2.rect.y - 23
        if person1.rect.y == 480 or pygame.sprite.collide_mask(person1, brick_on2):
            person1.isFinished = True
        else:
            person1.isFinished = False
    if keys[pygame.K_LEFT]:
        person2.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        person2.moveRight(5)
    if keys[pygame.K_UP]:
        person2.isJump = True
        person2.isFinished = False
        person2.Jump()
        if person2.rect.y == 480:
            person2.isFinished = True
    if keys[pygame.K_q]:
        can_load = random.randint(0, 100)
        if can_load > 25:
            if shoot_times1 == 0:
                pass
            shoot_times -= 1
            if shoot_times < 0:
                shoot_times = 0
        else:
            pass
    if keys[pygame.K_n]:
        can_load1 = random.randint(0, 100)
        if can_load1 > 25:
            if shoot_times1 == 0:
                pass
            shoot_times1 -= 1
            if shoot_times1 < 0:
                shoot_times1 = 0
        else:
            pass
    if pygame.sprite.collide_mask(person2, brick_on):
        person2.rect.y = brick_on.rect.y - 23
    if pygame.sprite.collide_mask(person2, brick_on2):
        person2.rect.y = brick_on2.rect.y - 23
    if pygame.sprite.collide_mask(person1, brick_on3):
        person1.rect.y = brick_on3.rect.y - 23
    if pygame.sprite.collide_mask(person2, brick_on3):
        person2.rect.y = brick_on3.rect.y - 23
    if keys[pygame.K_m] and shoot_times1 < 41:
        all_sprites_list.add(bullet2)
        bullet2.rect.y = person2.rect.y
        bullet2.rect.x = person2.rect.x
        fired1 = True
        bullet2.rect.x -= 1
        shoot_times1 += 1
        pygame.mixer.music.load('shooting.wav')
        pygame.mixer.music.play(0)
    if pygame.sprite.collide_rect(bullet2, brick_on):
        bullet2.rect.x -= 5
        fired1 = False
        all_sprites_list.remove(bullet2)
        bullet2.rect.x = 0
        bullet2.rect.y = 0
        person2.isFinished = True
    if pygame.sprite.collide_rect(bullet2, brick_on2):
        bullet2.rect.x -= 5
        fired1 = False
        all_sprites_list.remove(bullet2)
        bullet2.rect.x = 0
        bullet2.rect.y = 0
        person2.isFinished = True
    if pygame.sprite.collide_mask(bullet2, brick_on3):
        bullet2.rect.x -= 5
        fired1 = False
        all_sprites_list.remove(bullet2)
        bullet2.rect.x = 0
        bullet2.rect.y = 0
        person2.isFinished = True
    if not keys[pygame.K_0] and fired1 is True:
        if bullet2.rect.x > 700:
            bullet2.rect.x = 700
            all_sprites_list.remove(bullet2)
            fired1 = False
        bullet2.rect.x -= 30
    if keys[pygame.K_e] and shoot_times < 41:
        all_sprites_list.add(bullet)
        bullet.rect.y = person1.rect.y
        bullet.rect.x = person1.rect.x
        fired = True
        bullet.rect.x += 1
        shoot_times += 1
        pygame.mixer.music.load('shooting.wav')
        pygame.mixer.music.play(0)
    if not keys[pygame.K_e] and fired is True:
        if bullet.rect.x > 700:
            bullet.rect.x = 700
            all_sprites_list.remove(bullet)
            fired = False
        bullet.rect.x += 30
    if pygame.sprite.collide_mask(bullet, person2):
        critacal_shot = random.randint(0, 100)
        can_heal = random.randint(0, 100)
        if critacal_shot > 90:
            health2 -= 23
            print('critical shot!')
        else:
            health2 -= 7
        
    if pygame.sprite.collide_mask(bullet2, person1):
        critacal_shot2 = random.randint(0, 100)
        can_heal = random.randint(0, 100)
        if critacal_shot2 > 90:
            health -= 23
            print('critical shot!')
        else:
            health -= 7
    if pygame.sprite.collide_rect(bullet, brick_on):
        bullet.rect.x -= 5
        fired = False
        all_sprites_list.remove(bullet)
        bullet.rect.x = 0
        bullet.rect.y = 0
        person1.isFinished = True
    if pygame.sprite.collide_rect(bullet, brick_on2):
        bullet.rect.x -= 5
        fired = False
        all_sprites_list.remove(bullet)
        bullet.rect.x = 0
        bullet.rect.y = 0
        person1.isFinished = True
    if pygame.sprite.collide_mask(bullet, brick_on3):
        bullet.rect.x -= 5
        fired = False
        all_sprites_list.remove(bullet)
        bullet.rect.x = 0
        bullet.rect.y = 0
        person1.isFinished = True
    if not keys[pygame.K_w] and person1.isFinished is False:
        if pygame.sprite.collide_mask(person1, brick_on):
            person1.rect.y = brick_on.rect.y - 23
        if pygame.sprite.collide_mask(person1, brick_on2):
            person1.rect.y = brick_on2.rect.y - 23
        person1.rect.y += 5
        if person1.rect.y > 480:
            person1.rect.y = 480
    if not keys[pygame.K_UP] and person2.isFinished is False:
        if pygame.sprite.collide_mask(person2, brick_on):
            person2.rect.y = brick_on.rect.y - 23
        if pygame.sprite.collide_mask(person2, brick_on2):
            person2.rect.y = brick_on2.rect.y - 23
        person2.rect.y += 5
        if person2.rect.y > 480:
            person2.rect.y = 480
            person2.isFinished = True
    if pygame.sprite.collide_mask(person1, portal):
        randomcoordsx = random.randint(0, 500)
        randomcoordsy = random.randint(0, 500)
        person1.rect.y = randomcoordsy
        person1.rect.x = randomcoordsx
    if pygame.sprite.collide_mask(person1, friend):
        randomcoordsx = random.randint(0, 500)
        randomcoordsy = random.randint(0, 500)
        person1.rect.y = randomcoordsy
        person1.rect.x = randomcoordsx
    if pygame.sprite.collide_mask(person2, portal):
        randomcoordsx2 = random.randint(0, 500)
        randomcoordsy2 = random.randint(0, 500)
        person2.rect.y = randomcoordsy2
        person2.rect.x = randomcoordsx2
    if pygame.sprite.collide_mask(person2, friend):
        randomcoordsx2 = random.randint(0, 500)
        randomcoordsy2 = random.randint(0, 500)
        person2.rect.y = randomcoordsy2
        person2.rect.x = randomcoordsx2
    if can_heal > 80:
        can_heal = 0
        who = random.randint(0, 1)
        if who == 1:
            heal.rect.x = 50
            heal.rect.y = 480
            all_sprites_list.add(heal)
        if who == 0:
            heal.rect.x = 450
            heal.rect.y = 480
            all_sprites_list.add(heal)
    if pygame.sprite.collide_rect(person1, heal):
        health += 30
        if health > 100:
            health = 100
        all_sprites_list.remove(heal)
        heal.rect.x = 0
        heal.rect.y = 0
    if pygame.sprite.collide_rect(person2, heal):
        health2 += 30
        if health2 > 100:
            health2 = 100
        all_sprites_list.remove(heal)
        heal.rect.x = 0
        heal.rect.y = 0
    screen.fill(BLACK)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    font = pygame.font.Font(None, 43)
    health_text = f'red health: {health2}'
    if health <= 0:
        all_sprites_list.remove(person1)
        font_win = pygame.font.Font(None, 43)
        win_text = 'RED HAS WON THE GAME!'
        text_win = font_win.render(str(win_text), 1, WHITE)
        screen.blit(text_win, (100, 200))
        breaks
    text = font.render(str(health_text), 1, WHITE)
    screen.blit(text, (460, 10))
    if health2 <= 0:
        all_sprites_list.remove(person2)
        font_win = pygame.font.Font(None, 43)
        win_text = 'GREEN HAS WON THE GAME!'
        text_win = font_win.render(str(win_text), 1, WHITE)
        screen.blit(text_win, (100, 200))
        break
    font = pygame.font.Font(None, 43)
    health_text = f'green health: {health}'
    text = font.render(str(health_text), 1, WHITE)
    screen.blit(text, (100, 10))
    name101 = pygame.font.Font(None, 15)
    text = name101.render(str(text_team), 1, WHITE)
    screen.blit(text, (person1.rect.x - 6, person1.rect.y - 15))
    name202 = pygame.font.Font(None, 15)
    text = name202.render(str(text_team2), 1, WHITE)
    screen.blit(text, (person2.rect.x - 5, person2.rect.y - 15))
    pygame.display.flip()
    Clock.tick(30)
pygame.quit()

playsound("victory.wav")