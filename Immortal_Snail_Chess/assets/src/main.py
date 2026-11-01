import pygame,os,random
pygame.init()
WIDTH,HEIGHT=800,800
TILE_WIDTH,TILE_HEIGHT=WIDTH//8,HEIGHT//8
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Immortal Snail Chess")
clock=pygame.time.Clock()
running=True
if not os.path.exists(os.path.join(BASE_DIR,"../textures/chessboard.png")):raise FileNotFoundError("Missing texture: chessboard.png")
background=pygame.image.load(os.path.join(BASE_DIR,"../textures/chessboard.png")).convert()
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
selected_piece,PIECES=None,{}
for color in ["white","black"]:
    for piece in ["king","queen","rook","bishop","knight","pawn"]:
        name=f"{color}_{piece}"
        path=os.path.join(BASE_DIR,"../textures",f"{name}.png")
        if not os.path.exists(path):raise FileNotFoundError(f"Missing texture: {path}")
        PIECES[name]=pygame.image.load(path).convert_alpha()
        PIECES[name]=pygame.transform.scale(PIECES[name],(TILE_WIDTH,TILE_HEIGHT))
class Snail:
    def __init__(self,x,y):
        self.name="THE IMMORTAL SNAIL"
        self.x=x
        self.y=y
        if not os.path.exists(os.path.join(BASE_DIR,"../textures/snail.png")):raise FileNotFoundError("Missing texture: snail.png")
        self.image=pygame.image.load(os.path.join(BASE_DIR,"../textures/snail.png")).convert_alpha()
        self.image=pygame.transform.scale(self.image,(TILE_WIDTH,TILE_HEIGHT))
class Piece:
    def __init__(self,name,x,y):
        self.name=name
        self.x=x
        self.y=y
        self.moved=False
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
piece_directions={
    "pawn_move":[(0,1)],
    "pawn_capture":[(-1,1),(1,1)],
    "knight":[(1,2),(2,1),(-1,2),(-2,1),(1,-2),(2,-1),(-1,-2),(-2,-1)],
    "king":[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)],
    "rook":[(0,1),(0,-1),(1,0),(-1,0)],
    "bishop":[(1,1),(1,-1),(-1,1),(-1,-1)],
}
sliders=("rook","bishop","queen")
piece_directions["queen"]=piece_directions["rook"]+piece_directions["bishop"]
def get_piece_moves(piece:Piece,board_state):
    moves=[]
    if piece.name.endswith("pawn"):
        direction=1 if piece.name.startswith("black") else -1
        for dx,dy in piece_directions["pawn_move"]:
            nx,ny=piece.x+dx,piece.y+dy*direction
            if 0<=nx<8 and 0<=ny<8 and board_state[ny][nx] is None:
                moves.append((nx,ny))
            if not piece.moved:
                nx,ny=piece.x+dx,piece.y+(dy*2)*direction
                if 0<=nx<8 and 0<=ny<8 and board_state[ny][nx] is None and board_state[piece.y+dy*direction][piece.x] is None:
                    moves.append((nx,ny))
        for dx,dy in piece_directions["pawn_capture"]:
            nx,ny=piece.x+dx,piece.y+dy*direction
            if 0<=nx<8 and 0<=ny<8:
                target=board_state[ny][nx]
                if target is not None and target.name.split("_")[0]!=piece.name.split("_")[0]:
                    moves.append((nx,ny))
    elif piece.name=="snail":
        for dx in range (-1,2):
            for dy in range(-1,2):
                if dx==0 and dy==0:continue
                nx,ny=piece.x+dx,piece.y+dy
                if 0<=nx<8 and 0<=ny<8:
                    moves.append((nx,ny))
    else:
        directions=piece_directions[piece.name.split("_")[1]]
        for dx,dy in directions:
            nx,ny=piece.x,piece.y
            while True:
                nx+=dx
                ny+=dy
                if not (0<=nx<8 and 0<=ny<8):break
                target=board_state[ny][nx]
                if target is None:
                    moves.append((nx,ny))
                else:
                    if target.name.split("_")[0]!=piece.name.split("_")[0]:
                        moves.append((nx,ny))
                    break
                if piece.name.split("_")[1] not in sliders:
                    break
    return moves
snail=Snail(random.randint(0,7),random.randint(0,7))
for i in range(8):
    pieces.append(Piece("black_pawn",i,1))
    pieces.append(Piece("white_pawn",i,6))
def sync_board():
    board_state=[[None for _ in range(8)] for _ in range(8)]
    for piece in pieces[:]:
        if (piece.x,piece.y)==(snail.x,snail.y):
            pieces.remove(piece)
            continue
        existing=board_state[piece.y][piece.x]
        if existing is not None:
            pieces.remove(existing)
        board_state[piece.y][piece.x]=piece
    board_state[snail.y][snail.x]=snail
    return board_state
def draw_board():
    screen.blit(background,(WIDTH*0,HEIGHT*0)) #Good software design. I see absolutely no flaws here
    for piece in pieces:
        screen.blit(piece.image,(piece.x*TILE_WIDTH,piece.y*TILE_HEIGHT))
    screen.blit(snail.image,(snail.x*TILE_WIDTH,snail.y*TILE_HEIGHT))
highlight_surf=pygame.Surface((TILE_WIDTH,TILE_HEIGHT),pygame.SRCALPHA)
pygame.draw.circle(highlight_surf,(255,255,255,128),(TILE_WIDTH//2,TILE_HEIGHT//2),TILE_WIDTH//4) #I HATE pygame alpha why do they make me do this
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            mouse_x,mouse_y=event.pos
            tile_x=mouse_x//TILE_WIDTH
            tile_y=mouse_y//TILE_HEIGHT
            if 0<=tile_x<8 and 0<=tile_y<8:
                clicked_piece=board_state[tile_y][tile_x]
                if clicked_piece is not None:
                    selected_piece=clicked_piece
                else:
                    selected_piece=None
    board_state=sync_board()
    draw_board()
    if selected_piece is not None:
        moves=get_piece_moves(selected_piece,board_state)
        for mx,my in moves:
            screen.blit(highlight_surf,(mx*TILE_WIDTH,my*TILE_HEIGHT))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()