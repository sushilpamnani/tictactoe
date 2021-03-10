import pygame, sys
import numpy as np


pygame.init()

WIDTH = 1000
HEIGHT = WIDTH
LINE_WIDTH = WIDTH//60

BOARD_ROWS = 3
BOARD_COLUMNS = 3

SQUARE_SIZE = WIDTH/3
CIRCLE_RADIUS = WIDTH/10

BG_COLOR = (59, 59, 59)
LINE_COLOR = (138, 138, 138)

CROSS_COLOR = (2, 94, 242)
CIRCLE_COLOR = (18, 255, 109)

SPACE = WIDTH/12
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

#board
board = np.zeros((BOARD_ROWS, BOARD_COLUMNS))

def draw_lines():
    # 1st horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, WIDTH/3), (WIDTH, WIDTH/3), LINE_WIDTH)
    # 2nd horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 2*WIDTH/3), (WIDTH, 2*WIDTH/3), LINE_WIDTH)
    # 1st vertical
    pygame.draw.line(screen, LINE_COLOR, (WIDTH/3, 0), (WIDTH/3, WIDTH), LINE_WIDTH)
    # 2nd vertical
    pygame.draw.line(screen, LINE_COLOR, (2*WIDTH/3, 0), (2*WIDTH/3, WIDTH), LINE_WIDTH)


def mark_squares(row, column, player):
    board[row][column] = player

def available_square(row, column):
    return board[row][column] == 0

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 0:
                return False
    return True

def draw_shapes():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLUMNS):
            if board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOR, (col*WIDTH/3+SPACE, row*WIDTH/3+WIDTH/3-SPACE), (col*WIDTH/3+WIDTH/3-SPACE, row*WIDTH/3+SPACE), 30)
                pygame.draw.line(screen, CROSS_COLOR, (col*WIDTH/3+SPACE, row*WIDTH/3+SPACE), (col*WIDTH/3+WIDTH/3-SPACE, row*WIDTH/3+WIDTH/3-SPACE), 30)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col*WIDTH/3+WIDTH/6, row*WIDTH/3 + WIDTH/6), WIDTH/10, 15)


def check_win(player):
    for col in range(BOARD_COLUMNS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            draw_vertical_line(col, player)
            return True
    
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            draw_horizontal_line(row, player)
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == player:
        draw_cross_right(player)
        return True
    
    if board[0][2] == board[1][1] == board[2][0] == player:
        draw_cross_left(player)
        return True
        

def draw_vertical_line(col, player):
    color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
    pygame.draw.line(screen, color, (col*WIDTH/3+WIDTH/6, 0), (col*WIDTH/3+WIDTH/6, WIDTH), 20)

def draw_horizontal_line(col, player):
    color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
    pygame.draw.line(screen, color, (0, col*WIDTH/3+WIDTH/6), (WIDTH, col*WIDTH/3+WIDTH/6), 20)

def draw_cross_right(player):
    color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
    pygame.draw.line(screen, color, (0,0), (WIDTH,WIDTH), 20)

def draw_cross_left(player):
    color = CROSS_COLOR if player == 1 else CIRCLE_COLOR
    pygame.draw.line(screen, color, (WIDTH, 0), (0,WIDTH), 20)

def restart():
    
    screen.fill(BG_COLOR)
    draw_lines()
    for col in range(BOARD_COLUMNS):
        for row in range(BOARD_ROWS):
            board[row][col] = 0
    

player = 1

game_over = False

draw_lines()

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(3*mouseY//WIDTH)
            clicked_col = int(3*mouseX//WIDTH)

            if available_square(clicked_row, clicked_col):
                mark_squares(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

            draw_shapes()
            # print(board)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
                player = 1
    pygame.display.update()