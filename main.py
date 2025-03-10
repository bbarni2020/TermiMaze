import os
import keyboard
import shutil

# Labirintus definiálása
labyrinth = [
    "##########",
    "#@       #",
    "#  ####  #",
    "#  #  #  #",
    "#  #  #  #",
    "#     #  #",
    "######   #",
    "#        #",
    "#  #######",
    "#E       #",
    "##########"
]

# Játékos kezdő pozíciója
player_pos = [1, 1]

def print_labyrinth():
    os.system('cls' if os.name == 'nt' else 'clear')
    columns, rows = shutil.get_terminal_size()
    header = " Labirintus Játék ".center(columns, "=")
    footer = " Használd a nyílbillentyűket a mozgáshoz. Cél: elérni az 'E' pontot. Nyomj 'q'-t a kilépéshez. ".center(columns, "=")
    
    print(header)
    for row in labyrinth:
        print(row.center(columns))
    print(footer)

def move_player(direction):
    global player_pos
    x, y = player_pos
    if direction == 'up' and labyrinth[x-1][y] != '#':
        player_pos[0] -= 1
    elif direction == 'down' and labyrinth[x+1][y] != '#':
        player_pos[0] += 1
    elif direction == 'left' and labyrinth[x][y-1] != '#':
        player_pos[1] -= 1
    elif direction == 'right' and labyrinth[x][y+1] != '#':
        player_pos[1] += 1

def update_labyrinth():
    global labyrinth
    new_labyrinth = []
    for i, row in enumerate(labyrinth):
        new_row = ""
        for j, char in enumerate(row):
            if [i, j] == player_pos:
                new_row += '@'
            else:
                new_row += char
        new_labyrinth.append(new_row)
    labyrinth[:] = new_labyrinth

def main():
    print_labyrinth()
    while True:
        if keyboard.is_pressed('up'):
            move_player('up')
        elif keyboard.is_pressed('down'):
            move_player('down')
        elif keyboard.is_pressed('left'):
            move_player('left')
        elif keyboard.is_pressed('right'):
            move_player('right')
        elif keyboard.is_pressed('q'):
            print("Kilépés...")
            break
        update_labyrinth()
        print_labyrinth()
        if labyrinth[player_pos[0]][player_pos[1]] == 'E':
            print("Gratulálok, nyertél!")
            break

if __name__ == "__main__":
    main()
