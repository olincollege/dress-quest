import pygame, sys, random

class Frog(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.frog_sit = pygame.image.load("frog_sit").convert_alpha()
    self.frog_jump = pygame.image.load('frog_jump').convert_alpha()
    self.image = self.frog_sit
    self.image = pygame.transform.rotozoom(self.image,0,.25)
    self.rect = self.image.get_rect()
    
    #player movement
    self.direction = pygame.math.Vector2(0,0)
    self.gravity = 0.7
    self.jump_speed = -17
    self.speed = 8

  def test(self):
    return self.direction.x

  def test2(self):
    return self.rect

  def player_input(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and self.rect.bottom >= 300:
      self.jump()
    if keys[pygame.K_RIGHT] and self.rect.bottomright[0] <= screen_w:
      self.direction.x = 1
    elif keys[pygame.K_LEFT] and self.rect.bottomleft[0] >= 0:
      self.direction.x = -1
    else:
      self.direction.x = 0

  def apply_gravity(self):
    self.direction.y += self.gravity
    self.rect.y += self.direction.y
    if self.rect.bottom < 300: 
      self.image = self.frog_jump
      self.image = pygame.transform.rotozoom(self.image,0,.18)
      
    else:
      self.image = self.frog_sit
      self.image = pygame.transform.rotozoom(self.image,0,.25)
      
    #delete line below for platform game
    if self.rect.bottom >= 300: self.rect.bottom = 300

  def jump(self):
    self.direction.y = self.jump_speed
    
  def update(self):
    self.player_input()
    self.apply_gravity()
    self.rect.x += self.direction.x * self.speed
    self.test() #delete later

class Clothes(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.rnbw_top = pygame.image.load("rainbow_top.png").convert_alpha()
    self.image = self.rnbw_top
    self.image = pygame.transform.rotozoom(self.image,0,.25)
    self.rect = self.image.get_rect()
    self.direction = pygame.math.Vector2(0,0)


  def update(self):
    self.rect.x += 1
    #self.direction.y = Frog.direction.y
  
#General Setup
pygame.init()
clock = pygame.time.Clock()

#Game Screen
screen_w = 500
screen_h = 1080
screen = pygame.display.set_mode((screen_w,screen_h))
background = pygame.image.load("Background_Blue.png")

#Frog Sprite Group Creation
frog_group = pygame.sprite.Group()
frog_group.add(Frog())

#Clothes Sprite Group Creation
clothes_group = pygame.sprite.Group()
clothes_group.add(Clothes())

#just put a ground in ig for the vibes
ground_surface = pygame.image.load('grnd.png.png').convert()


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()


  pygame.display.flip()
  screen.blit(background,(0,0))
  screen.blit(ground_surface,(0,300))
  frog_group.draw(screen)
  frog_group.update()
  clothes_group.draw(screen)
  clothes_group.update()
  clock.tick(60)