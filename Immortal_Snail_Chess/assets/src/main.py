import pygame,sys,os
pygame.init()
WIDTH,HEIGHT=800,800
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Immortal Snail Chess")
clock=pygame.time.Clock()
running=True
background=pygame.image.load(os.path.join(BASE_DIR,"../textures/chessboard.png")).convert()
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
class Snail:
    def __init__(self,x,y):
        self.x=x
        self.y=y
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.blit(background,(WIDTH*0,HEIGHT*0)) #Good software design. I see absolutely no flaws here
    pygame.display.flip()
    clock.tick(60)
pygame.quit()