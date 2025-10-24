import pygame  
from pygame import mixer
import math
import random
#initialize pygame
pygame.init()
screen=pygame.display.set_mode((1612,720))
#title and logo
pygame.display.set_caption("Catch The Ball")
icon=pygame.image.load('shoot.png')
pygame.display.set_icon(icon)
#background image
bg_img = pygame.image.load('bg.png').convert()
bg_img = pygame.transform.smoothscale(bg_img,(1612,720))
#background sound
mixer.music.load('bgmusic.mp3')
mixer.music.play(-1)

#player
playerimg=pygame.image.load('basket.png')
playerx = 620
playery = 500
px_change=0

#target
ballimg = []
ballx = []
bally = []
by_change = 2
num_of_balls = 3
for i in range(num_of_balls):
   ballimg.append(pygame.image.load('ball.png'))
   ballx.append(random.randint(0,620))
   bally.append(random.randint(0,60))

def player(x,y):
  screen.blit(playerimg,(playerx,playery))

def target(x,y):
  screen.blit(ballimg[i],(ballx[i],bally[i]))
  
#collision
def collision(x1,x2,y1,y2):
  distance = math.sqrt((math.pow(x2-x1,2)) + (math.pow(y2-y1,2)))
  if distance < 40:
    return True
  else:
    return False

#score
score_val = 0
font = pygame.font.Font('freesansbold.ttf',32)
tx=10
ty=10
def show_score(x,y):
  score = font.render("Score:" + str(score_val),True,(255,255,255))
  screen.blit(score,(x,y))
  
#main game loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
    if event.type == pygame.KEYDOWN:
      if  event.key == pygame.K_LEFT:
        px_change = -10
      if  event.key == pygame.K_RIGHT:
        px_change = 10
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        px_change = 0

  screen.blit(bg_img,(0,0))
  
  playerx += px_change
  if playerx <= 0:
    playerx = 0
  elif playerx >= 1330:
    playerx = 1330
  
  for i in range(num_of_balls):
    bally[i] += by_change
    col = collision(playerx,ballx[i],playery,bally[i])
    if col:
     col_sound=mixer.Sound('collect.mp3')
     col_sound.play()
     ballx[i] = random.randint(0,620)
     bally[i] = random.randint(0,60)
     score_val += 1
    if bally[i] > 560:
     ballx[i] = random.randint(0,620)
     bally[i] = random.randint(0,60)
    target(ballx[i],bally[i])

  player(playerx,playery)   
  show_score(tx,ty)
  pygame.display.update()
  
pygame.quit()
