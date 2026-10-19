import pygame,os,random
pygame.init()
WIDTH,HEIGHT=800,800
TILE_WIDTH,TILE_HEIGHT=WIDTH//8,HEIGHT//8
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Immortal Snail Chess")
clock=pygame.time.Clock()
running=True
background=pygame.image.load(os.path.join(BASE_DIR,"../textures/chessboard.png")).convert()
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
PIECES={}
for color in ["white","black"]:
    for piece in ["king","queen","rook","bishop","knight","pawn"]:
        name=f"{color}_{piece}"
        path=os.path.join(BASE_DIR,"../textures",f"{name}.png")
        PIECES[name]=pygame.image.load(path).convert_alpha()
        PIECES[name]=pygame.transform.scale(PIECES[name],(TILE_WIDTH,TILE_HEIGHT))
class Snail:
    def __init__(self,x,y):
        self.name="THE IMMORTAL SNAIL"
        self.x=x
        self.y=y
        self.image=pygame.image.load(os.path.join(BASE_DIR,"../textures/snail.png")).convert_alpha()
        self.image=pygame.transform.scale(self.image,(TILE_WIDTH,TILE_HEIGHT))
class Piece:
    def __init__(self,name,x,y):
        self.name=name
        self.x=x
        self.y=y
        self.image=PIECES[name]
pieces=[
    Piece("black_rook",0,0),
    Piece("black_knight",1,0),
    Piece("black_bishop",2,0),
    Piece("black_queen",3,0),
    Piece("black_king",4,0),
    Piece("black_bishop",5,0),
    Piece("black_knight",6,0),
    Piece("black_rook",7,0),
    Piece("white_rook",0,7),
    Piece("white_knight",1,7),
    Piece("white_bishop",2,7),
    Piece("white_queen",3,7),
    Piece("white_king",4,7),
    Piece("white_bishop",5,7),
    Piece("white_knight",6,7),
    Piece("white_rook",7,7),
]
for i in range(8):
    pieces.append(Piece("black_pawn",i,1))
    pieces.append(Piece("white_pawn",i,6))
def draw_board():
    screen.blit(background,(WIDTH*0,HEIGHT*0)) #Good software design. I see absolutely no flaws here
    for piece in pieces:
        screen.blit(piece.image,(piece.x*TILE_WIDTH,piece.y*TILE_HEIGHT))
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    draw_board()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()