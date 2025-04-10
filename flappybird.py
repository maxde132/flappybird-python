import random
import time
from pynput import keyboard


grid0 = [". "] * 10
grid1 = [". "] * 10
grid2 = [". "] * 10
grid3 = [". "] * 10
grid4 = [". "] * 10
grid5 = [". "] * 10
grid6 = [". "] * 10
grid7 = [". "] * 10
grid8 = [". "] * 10
grid9 = [". "] * 10
score = 0
flappy_x = 0
flappy_y = 4

frame_time = 0.5
running = True  

def clear():
    
    print("\033[2J\033[H", end="")

def displaygrid():
    
    clear()
    print("".join(grid0))
    print("".join(grid1))
    print("".join(grid2))
    print("".join(grid3))
    print("".join(grid4))
    print("".join(grid5))
    print("".join(grid6))
    print("".join(grid7))
    print("".join(grid8))
    print("".join(grid9))
    print("Score: "+str(score))

def updatecharacter(row, column, newchar):
    if row == 0:
        grid0[column] = newchar
    elif row == 1:
        grid1[column] = newchar
    elif row == 2:
        grid2[column] = newchar
    elif row == 3:
        grid3[column] = newchar
    elif row == 4:
        grid4[column] = newchar
    elif row == 5:
        grid5[column] = newchar
    elif row == 6:
        grid6[column] = newchar
    elif row == 7:
        grid7[column] = newchar
    elif row == 8:
        grid8[column] = newchar
    elif row == 9:
        grid9[column] = newchar
    else:
        print("Invalid row:", row)

def updatecolumn(column, newchar):
    """Update an entire column with newchar."""
    for row in range(10):
        updatecharacter(row, column, newchar)

def movecolumn(column):
    
    updatecharacter(0, column - 1, grid0[column])
    updatecharacter(1, column - 1, grid1[column])
    updatecharacter(2, column - 1, grid2[column])
    updatecharacter(3, column - 1, grid3[column])
    updatecharacter(4, column - 1, grid4[column])
    updatecharacter(5, column - 1, grid5[column])
    updatecharacter(6, column - 1, grid6[column])
    updatecharacter(7, column - 1, grid7[column])
    updatecharacter(8, column - 1, grid8[column])
    updatecharacter(9, column - 1, grid9[column])

def moveallcolumns():
    """Shift all the columns left and clear the last column."""
    for col in range(1, 10):
        movecolumn(col)
    updatecolumn(9, ". ")

def generatepipes(column):
    
    random_int = random.randint(1, 8)
    updatecolumn(column, "| ")
    
    if random_int - 1 >= 0:
        updatecharacter(random_int - 1, column, ". ")
    updatecharacter(random_int, column, ". ")
    if random_int + 1 < 10:
        updatecharacter(random_int + 1, column, ". ")


def on_press(key):
    global flappy_y, running
    try:        
        if key.char == 'q':
            running = False        
        elif key.char == 'b':
            flappy_y = min(9, flappy_y + 1)
            clear()
            displaygrid()
    except AttributeError:
        if key == keyboard.Key.space or key == keyboard.Key.up:
            flappy_y = max(0, flappy_y - 1)
            clear()
            displaygrid()
        elif key == keyboard.Key.down:
            flappy_y = min(9, flappy_y + 1)
        elif key == keyboard.Key.esc:
            running = False

listener = keyboard.Listener(on_press=on_press)
listener.start()

def check_collision():
    
    global running
    if flappy_y == 0:
        cell = grid0[0]
    elif flappy_y == 1:
        cell = grid1[0]
    elif flappy_y == 2:
        cell = grid2[0]
    elif flappy_y == 3:
        cell = grid3[0]
    elif flappy_y == 4:
        cell = grid4[0]
    elif flappy_y == 5:
        cell = grid5[0]
    elif flappy_y == 6:
        cell = grid6[0]  
    elif flappy_y == 7:
        cell = grid7[0]
    elif flappy_y == 8:
        cell = grid8[0]
    elif flappy_y == 9:
        cell = grid9[0]
    else:
        cell = ". "
    
    if cell != ". ":
        updatecharacter(flappy_y, flappy_x, "@ ")
        displaygrid()
        print("Game Over!")
        running = False
        return True
    return False


updatecharacter(flappy_y, flappy_x, "@ ")

# Main game loop.
while running:
    moveallcolumns()
    updatecolumn(9, ". ")
    if check_collision():
        break

    
    flappy_y = min(9, flappy_y + 1)
    updatecharacter(flappy_y, flappy_x, "@ ")
    displaygrid()
    time.sleep(frame_time)

    moveallcolumns()
    updatecolumn(9, ". ")
    if check_collision():
        break

    updatecharacter(flappy_y, flappy_x, "@ ")
    displaygrid()
    time.sleep(frame_time)
    
    moveallcolumns()
    updatecolumn(9, ". ")
    if check_collision():
        break

    
    flappy_y = min(9, flappy_y + 1)
    updatecharacter(flappy_y, flappy_x, "@ ")
    displaygrid()
    time.sleep(frame_time)
    
    moveallcolumns()
    generatepipes(9)
    score = score + 1
    if check_collision():
        break

    
    
