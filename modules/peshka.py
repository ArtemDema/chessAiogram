from .map_and_inline_b import map

#y_f - y фигуры
#x_f - x фигуры
#y_p - y точки(куда хочет походить)
#x_p - x точки(куда хочет походить)
#bw - хранит какого цвета фигура(или какой цвет надо искать и взаимодействовать с ним)

#диагонально влево:
def top_left(y_f, x_f, y_p, x_p, bw):
    if x_f != 0:
        if bw == "white":
            if map[y_f - 1][x_f - 1] != " " and map[y_f - 1][x_f - 1] != "♙" and map[y_f - 1][x_f - 1] != "♖" and map[y_f - 1][x_f - 1] != "♘" and map[y_f - 1][x_f - 1] != "♗" and map[y_f - 1][x_f - 1] != "♔" and map[y_f - 1][x_f - 1] != "♕": #Проверка на то, пытается ли игрок съесть фигуру(вражескую)
                if y_p == y_f - 1 and x_p == x_f - 1:
                    if y_p == 0:
                        map[y_f][x_f] = "♕"
                        print(map[y_f][x_f])
                    return True
                else:
                    return False
            else:
                return False
        if bw == "black":
            if map[y_f + 1][x_f - 1] != " " and map[y_f + 1][x_f - 1] != "♟" and map[y_f + 1][x_f - 1] != "♜" and map[y_f + 1][x_f - 1] != "♞" and map[y_f + 1][x_f - 1] != "♝" and map[y_f + 1][x_f - 1] != "♚" and map[y_f + 1][x_f - 1] != "♛": #Проверка на то, пытается ли игрок съесть фигуру(вражескую)
                if y_p == y_f + 1 and x_p == x_f - 1:
                    if y_p == 0:
                        map[y_f][x_f] = "♛"
                    return True
                else:
                    return False
            else:
                return False

#диагонально вправо:

def top_right(y_f, x_f, y_p, x_p, bw):
    if x_f != 7:
        if bw == "white":
            if map[y_f - 1][x_f + 1] != " " and map[y_f - 1][x_f + 1] != "♙" and map[y_f - 1][x_f + 1] != "♖" and map[y_f - 1][x_f + 1] != "♘" and map[y_f - 1][x_f + 1] != "♗" and map[y_f - 1][x_f + 1] != "♔" and map[y_f - 1][x_f + 1] != "♕": #Проверка на то, пытается ли игрок съесть фигуру(вражескую)
                if y_p == y_f - 1 and x_p == x_f + 1: #Если выбор нашего игрока совпадает с этой клеткой
                    if y_p == 0:
                        map[y_f][x_f] = "♕"
                    return True #Даётся разрешение за ход
                else:
                    return False #Не даётся разрешение на ход
        if bw == "black":
            if map[y_f + 1][x_f + 1] != " " and map[y_f + 1][x_f + 1] != "♟" and map[y_f + 1][x_f + 1] != "♜" and map[y_f + 1][x_f + 1] != "♞" and map[y_f + 1][x_f + 1] != "♝" and map[y_f + 1][x_f + 1] != "♚" and map[y_f + 1][x_f + 1] != "♛": #Проверка на то, пытается ли игрок съесть фигуру(вражескую)
                if y_p == y_f + 1 and x_p == x_f + 1:
                    if y_p == 0:
                        map[y_f][x_f] = "♛"
                    return True
                else:
                    return False
            else:
                return False
        
#вперёд(1):

def top(y_f, x_f, y_p, x_p, bw):
    if y_f != 0:
        if bw == "white":
            if map[y_f - 1][x_f] == " ": #Проверка на то, пустая ли клетка впереди
                if y_p == y_f - 1 and x_p == x_f: #Если выбор нашего игрока совпадает с этой клеткой
                    if y_p == 0:
                        map[y_f][x_f] = "♕"
                    return True #Даётся разрешение за ход
                else:
                    return False #Не даётся разрешение на ход
            else:
                return False #Не даётся разрешение на ход
        if bw == "black":
            if map[y_f + 1][x_f] == " ": 
                if y_p == y_f + 1 and x_p == x_f:
                    if y_p == 0:
                        map[y_f][x_f] = "♛"
                    return True 
                else:
                    return False 
            else:
                return False
            
##Тоже самое только сохраняет куда может пойти фигура(для короля)
def list_top_left_peshka(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♟":
                    if idy - 1 >= 0 and idx - 1 >= 0:
                        list_moves.append(f"{idy - 1} {idx - 1}")
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♟":
                    if idy + 1 <= 7 and idx - 1 >= 0:
                        list_moves.append(f"{idy + 1} {idx - 1}")
    return list_moves


def list_top_right_peshka(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♟":
                    if idy + 1 <= 7 and idx - 1 >= 0:
                        list_moves.append(f"{idy - 1} {idx - 1}")
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♟":
                    if idy + 1 <= 7 and idx + 1 <= 7:
                        list_moves.append(f"{idy + 1} {idx - 1}")
    return list_moves

def check_move_peshka(y_f, x_f, y_p, x_p, bw):
    answer = top_left(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = top(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = top_right(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    else:
        return False