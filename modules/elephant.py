from .map_and_inline_b import map
#Нужные для работы проверки:

#y_f - y фигуры
#x_f - x фигуры
#y_p - y точки(куда хочет походить)
#x_p - x точки(куда хочет походить)
#bw - хранит какого цвета фигура(или какой цвет надо искать и взаимодействовать с ним)

#диагонально вниз вправо
def bottom_right(y_f, x_f, y_p, x_p, bw):
    if y_f != 7 and x_f != 7:
        if bw == "white":
            for index in range(len(map) - y_f):
                if index > 0:
                    if y_f + index < len(map) and x_f + index < len(map):
                        if map[y_f + index][x_f + index] != " ":#Проверка, которая вычисляет фигуры по пути к точке хода
                            if x_p != x_f + index and y_p != y_f + index:#Если выбор игрока не совпадает с этой точкой
                                return False
                        if x_p == x_f + index and y_p == y_f + index:#Если выбор нашего игрока совпадает с точкой
                            if map[y_p][x_p] == " ":#Проверка на то, пустая ли клетка
                                return True#Даётся разрешение на ход
                            if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                                return True#Даётся разрешение на ход
            return False#Если ничего из этого - то не даётся разрешение на ход
        if bw == "black":
            for index in range(len(map) - y_f):
                if index > 0:
                    if y_f + index < len(map) and x_f + index < len(map):
                        if map[y_f + index][x_f + index] != " ":
                            if x_p != x_f + index and y_p != y_f + index:
                                return False
                        if x_p == x_f + index and y_p == y_f + index:
                            if map[y_p][x_p] == " ":
                                return True
                            if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":
                                return True
            return False

def bottom_left(y_f, x_f, y_p, x_p, bw):
    if y_f != 7 or x_f != 0:
        if bw == "white":
            for index in range(len(map) - y_f):
                if index > 0:
                    if y_f + index < len(map) and x_f - index >= 0:
                        if map[y_f + index][x_f - index] != " ":
                            if x_p != x_f - index and y_p != y_f + index:
                                return False
                        if x_p == x_f - index and y_p == y_f + index:
                            if map[y_p][x_p] == " ":
                                return True
                            if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":
                                return True
            return False
        if bw == "black":
            for index in range(len(map) - y_f):
                if index > 0:
                    if y_f + index < len(map) and x_f - index >= 0:
                        if map[y_f + index][x_f - index] != " ":
                            if x_p != x_f - index and y_p != y_f + index:
                                return False
                        if x_p == x_f - index and y_p == y_f + index:
                            if map[y_p][x_p] == " ":
                                return True
                            if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":
                                return True
            return False
    
def top_right(y_f, x_f, y_p, x_p, bw):
    if y_f != 0 or x_f != 7:
        if bw == "white":
            for index in range(y_f):
                if index > 0:
                    if y_f - index >= 0 and x_f + index < len(map):
                        if map[y_f - index][x_f + index] != " ":
                            if x_p != x_f + index and y_p != y_f - index:
                                return False
                        if x_p == x_f + index and y_p == y_f - index:
                            if map[y_p][x_p] == " ":
                                return True
                            if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":
                                return True
            return False
        if bw == "black":
            for index in range(len(map) - y_f):
                if index > 0:
                    if y_f - index >= 0 and x_f + index < len(map):
                        if map[y_f - index][x_f + index] != " ":
                            if x_p != x_f + index and y_p != y_f - index:
                                return False
                        if x_p == x_f + index and y_p == y_f - index:
                            if map[y_p][x_p] == " ":
                                return True
                            if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":
                                return True
            return False
    
def top_left(y_f, x_f, y_p, x_p, bw):
    if y_f != 0 or x_f != 0:
        if bw == "white":
            for index in range(y_f):
                if index > 0:
                    if y_f - index >= 0 and x_f - index >= 0:
                        if map[y_f - index][x_f - index] != " ":
                            if x_p != x_f - index and y_p != y_f - index:
                                return False
                        if x_p == x_f - index and y_p == y_f - index:
                            if map[y_p][x_p] == " ":
                                return True
                            if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":
                                return True
            return False
        if bw == "black":
            for index in range(y_f):
                if index > 0:
                    if y_f - index >= 0 and x_f - index >= 0:
                        if map[y_f - index][x_f - index] != " ":
                            if x_p != x_f - index and y_p != y_f - index:
                                return False
                        if x_p == x_f - index and y_p == y_f - index:
                            if map[y_p][x_p] == " ":
                                return True
                            if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":
                                return True
            return False
        




def list_bottom_right_elephant(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♗":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy + index < len(map) and idx + index < len(map):
                                    if map[idy + index][idx + index] == " " or map[idy + index][idx + index] == "♔":
                                        list_moves.append(f"{idy + index} {idx + index}")
                                    else:
                                        break
        return list_moves
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♝":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy + index < len(map) and idx + index < len(map):
                                    if map[idy + index][idx + index] == " " or map[idy + index][idx + index] == "♔":
                                        list_moves.append(f"{idy + index} {idx + index}")
                                    else:
                                        break
        return list_moves
    

def list_bottom_left_elephant(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♗":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy + index < len(map) and idx - index >= 0:
                                    if map[idy + index][idx - index] == " " or map[idy + index][idx - index] == "♔":
                                        list_moves.append(f"{idy + index} {idx - index}")
                                    else:
                                        break
        return list_moves
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♝":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy + index < len(map) and idx - index >= 0:
                                    if map[idy + index][idx - index] == " " or map[idy + index][idx - index] == "♔":
                                        list_moves.append(f"{idy + index} {idx - index}")
                                    else:
                                        break
        return list_moves
    

def list_top_left_elephant(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♗":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy - index < len(map) and idx - index < len(map):
                                    if map[idy - index][idx - index] == " " or map[idy - index][idx - index] == "♔":
                                        list_moves.append(f"{idy - index} {idx - index}")
                                    else:
                                        break
        return list_moves
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♝":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy - index < len(map) and idx - index < len(map):
                                    if map[idy - index][idx - index] == " " or map[idy - index][idx - index] == "♔":
                                        list_moves.append(f"{idy - index} {idx - index}")
                                    else:
                                        break
        return list_moves
    

def list_top_right_elephant(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♗":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy - index < len(map) and idx + index < len(map):
                                    if map[idy - index][idx + index] == " " or map[idy - index][idx + index] == "♔":
                                        list_moves.append(f"{idy - index} {idx + index}")
                                    else:
                                        break
        return list_moves
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♝":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy - index < len(map) and idx + index < len(map):
                                    if map[idy - index][idx + index] == " " or map[idy - index][idx + index] == "♔":
                                        list_moves.append(f"{idy - index} {idx + index}")
                                    else:
                                        break
        return list_moves

def check_can_move_elephant_w(y_f, x_f, y_p, x_p, bw):
    answer = bottom_right(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = bottom_left(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = top_right(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = top_left(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    else:
        return False