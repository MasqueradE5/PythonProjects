from datetime import datetime
import random
import sys
import msvcrt

def clear_console():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def get_key():
    return msvcrt.getch().decode("utf-8").lower()

def save_score(name, score):
    with open("results.txt", "a", encoding="utf-8") as f:
        nnow = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"[{nnow}] Игрок {name}, очки: {score}\n")

SYMBOLS = {
    "#": "\U0001F7E6",   # стена
    ".": "⚪",   # точка
    "P": "😋",   # пакман
    " ": "⬛",   # пустое
    "G": "👻"    # призрак
}


RAW_MAP = [
    "############################",
    "#............##............#",
    "#.####.#####.##.#####.####.#",
    "#.####.#####.##.#####.####.#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#......##....##....##......#",
    "######.#####.##.#####.######",
    "#..........................#",
    "#..........######..........#",
    "#.######...####....######..#",
    "#..........................#",
    "#.####.##.########.##.####.#",
    "#.####.##....##....##.####.#",
    "#......######.##.######....#",
    "#..........................#",
    "#.####.#####.##.#####.####.#",
    "#............##............#",
    "#............##............#",
    "############################",
]

score = 0
game_over = False
win= False
name= input("Введите имя")
field = [list(row) for row in RAW_MAP];
field[1][1] = 'P'
field[13][8] = 'G'
player_x, player_y = 1, 1
ghost_x, ghost_y = 13, 8
gunder = '.'
x= 0
y= 0
def move(dx, dy):
    global player_x, player_y, score, game_over
    cur_x = player_x
    cur_y = player_y
    new_x, new_y = player_x + dx, player_y + dy
    if field[new_x][new_y] != "#" and field[new_x][new_y] == " ":
        player_x, player_y = new_x, new_y
    elif field[new_x][new_y] == "G":
        game_over = True
    elif field[new_x][new_y] == ".":
        score += 1
        player_x, player_y = new_x, new_y
    if game_over != True:
        field[cur_x][cur_y]= ' '
        field[player_x][player_y]= 'P'

def iswin():
    global name, score
    for sublist in field:
        if '.' in sublist or gunder == '.':
            win = False
        else:
            win = True
            save_score(name,score)



def ghostmove():
    global ghost_x, ghost_y, gunder
    themove= []
    w, e, n, s = [ghost_x-1, ghost_y],[ghost_x+1, ghost_y], [ghost_x, ghost_y-1], [ghost_x, ghost_y+1]
    if field[w[0]][w[1]] != '#':
        themove.append('w')
    if field[e[0]][e[1]] != '#':
        themove.append('e')
    if field[n[0]][n[1]] != '#':
        themove.append('n')
    if field[s[0]][s[1]] != '#':
        themove.append('s')
    r= random.choice(themove)
    if r == 'w':
        field[ghost_x][ghost_y] = gunder
        ghost_x, ghost_y = w[0], w[1]
        gunder = field[ghost_x][ghost_y]
        field[ghost_x][ghost_y] = 'G'
        if gunder == 'P':
            game_over = True
    if r == 'e':
        field[ghost_x][ghost_y] = gunder
        ghost_x, ghost_y = e[0], e[1]
        gunder = field[ghost_x][ghost_y]
        field[ghost_x][ghost_y] = 'G'
        if gunder == 'P':
            game_over = True
    if r == 'n':
        field[ghost_x][ghost_y] = gunder
        ghost_x, ghost_y = n[0], n[1]
        gunder = field[ghost_x][ghost_y]
        field[ghost_x][ghost_y] = 'G'
        if gunder == 'P':
            game_over = True
    if r == 's':
        field[ghost_x][ghost_y] = gunder
        ghost_x, ghost_y = s[0], s[1]
        gunder = field[ghost_x][ghost_y]
        field[ghost_x][ghost_y] = 'G'
        if gunder == 'P':
            game_over = True

for row in field:
    clear_console();
    print("".join(SYMBOLS.get(cell, cell) for cell in row))

while game_over != True or win != True:
    x,y= 0, 0
    char_key = get_key();
    if char_key.lower() == 'w':
        x, y = -1,0
        print("Вперед (W)")
    elif char_key.lower() == 'a':
        print("Влево (A)")
        x,y = 0,-1
    elif char_key.lower() == 's':
        print("Назад (S)")
        x, y = 1, 0
    elif char_key.lower() == 'd':
        print("Вправо (D)")
        x, y = 0, 1
    elif char_key.lower() == 'q':
        print("Выход...")
        break;
    move(x,y);
    ghostmove();
    for row in field:
        clear_console();
        print("".join(SYMBOLS.get(cell, cell) for cell in row))
    iswin();
    if win == True or game_over == True:
        break;



