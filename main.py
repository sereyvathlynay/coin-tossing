import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()


icon = pygame.image.load('img/random.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Toss Coin')


frame_pos = 1
trigger = 0
round = 1
frame1 = pygame.image.load('img/1.png')
frame2 = pygame.image.load('img/2.png')
frame3 = pygame.image.load('img/3.png')
frame4 = pygame.image.load('img/4.png')
frame5 = pygame.image.load('img/5.png')
frame6 = pygame.image.load('img/6.png')
frame7 = pygame.image.load('img/7.png')
frame8 = pygame.image.load('img/8.png')
frame9 = pygame.image.load('img/9.png')
frame10 = pygame.image.load('img/10.png')
frame11 = pygame.image.load('img/11.png')

def tossing(x, y, frame_pos):
    if frame_pos == 1 or frame_pos == 12:
        screen.blit(frame1, (x, y))
    elif frame_pos == 2 or frame_pos == 13:
        screen.blit(frame2, (x, y))
    elif frame_pos == 3 or frame_pos == 14:
        screen.blit(frame3, (x, y))
    elif frame_pos == 4 or frame_pos == 15:
        screen.blit(frame4, (x, y))
    elif frame_pos == 5 or frame_pos == 16:
        screen.blit(frame5, (x, y))
    elif frame_pos == 6 or frame_pos == 17:
        screen.blit(frame6, (x, y))
    elif frame_pos == 7 or frame_pos == 18:
        screen.blit(frame7, (x, y))
    elif frame_pos == 8 or frame_pos == 19:
        screen.blit(frame8, (x, y))
    elif frame_pos == 9 or frame_pos == 20:
        screen.blit(frame9, (x, y))
    elif frame_pos == 10 or frame_pos == 21:
        screen.blit(frame10, (x, y))
    elif frame_pos == 11 or frame_pos == 22:
        screen.blit(frame11, (x, y))


result = frame1
head = pygame.image.load('img/head.png')
tail = pygame.image.load('img/tail.png')
def coin_tossed():
    return random.randint(1, 2)

    

running = True
while running:
    
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                trigger = 1
                if coin_tossed() == 1:
                    result = head
                else:
                    result = tail


    if trigger == 1:
        if round == 1:
            tossing(336, 236, frame_pos)
            if frame_pos == 11:
                round = 2
        elif round == 2:
            tossing(336, 236, frame_pos)
        frame_pos += 1
        if frame_pos > 22:
            frame_pos = 1
            trigger = 0
            round = 1

    if trigger == 0:
        screen.blit(result, (336, 236))
        

    pygame.display.update()
    clock.tick(15)



pygame.quit()
quit()
