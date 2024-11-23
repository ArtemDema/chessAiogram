from .map_and_inline_b import map

#Нужные для работы проверки:

#y_f - y фигуры
#x_f - x фигуры
#y_p - y точки(куда хочет походить)
#x_p - x точки(куда хочет походить)
#bw - хранит какого цвета фигура(или какой цвет надо искать и взаимодействовать с ним)

#вправо
def right(y_f, x_f, y_p, x_p, bw):
    if x_f != 7:
        if bw == "white":
            for i in range(8 - x_f):
                if i > 0:
                    if map[y_f][x_f + i] != " ":
                        if x_p != x_f + i and y_p == y_f:
                            return False
                    if x_p == x_f + i and y_p == y_f:
                        if map[y_p][x_p] == " ":
                            return True
                        if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":
                            return True
            return False
        if bw == "black":
            for i in range(8 - x_f):
                if i > 0:
                    if map[y_f][x_f + i] != " ":
                        if x_p != x_f + i and y_p == y_f:
                            return False
                    if x_p == x_f + i and y_p == y_f:
                        if map[y_p][x_p] == " ":
                            return True
                        if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":
                            return True
            return False

#влево
def left(y_f, x_f, y_p, x_p, bw):
    if x_f != 0:
        if bw == "white":
            for i in range(x_f + 1):
                if i > 0:
                    if map[y_f][x_f - i] != " ":
                        if x_p != x_f - i and y_p == y_f:
                            return False
                    if x_p == x_f - i and y_p == y_f:
                        if map[y_p][x_p] == " ":
                            return True
                        if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":
                            return True
            return False
        if bw == "black":
            for i in range(x_f + 1):
                if i > 0:
                    if map[y_f][x_f - i] != " ":
                        if x_p != x_f - i and y_p == y_f:
                            return False
                    if x_p == x_f - i and y_p == y_f:
                        if map[y_p][x_p] == " ":
                            return True
                        if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":
                            return True
            return False

#вниз
def bottom(y_f, x_f, y_p, x_p, bw):
    if y_f != 7:
        if bw == "white":
            for i in range(8 - y_f):
                if i > 0:
                    if map[y_f + i][x_f] != " ":
                        if x_p == x_f and y_p != y_f + i:
                            return False
                    if x_p == x_f and y_p == y_f + i:
                        if map[y_p][x_p] == " ":
                            return True
                        if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":
                            return True
            return False
        if bw == "black":
            for i in range(8 - y_f):
                if i > 0:
                    if map[y_f + i][x_f] != " ":
                        if x_p == x_f and y_p != y_f + i:
                            return False
                    if x_p == x_f and y_p == y_f + i:
                        if map[y_p][x_p] == " ":
                            return True
                        if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":
                            return True
            return False
#вверх
def top(y_f, x_f, y_p, x_p, bw):
    if y_f != 0:
        if bw == "white":
            for i in range(y_f + 1):
                if i > 0:
                    if map[y_f - i][x_f] != " ":
                        if x_p == x_f and y_p != y_f - i:
                            return False
                    if x_p == x_f and y_p == y_f - i:
                        if map[y_p][x_p] == " ":
                            return True
                        if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":
                            return True
            return False
        if bw == "black":
            for i in range(y_f + 1):
                if i > 0:
                    if map[y_f - i][x_f] != " ":
                        if x_p == x_f and y_p != y_f - i:
                            return False
                    if x_p == x_f and y_p == y_f - i:
                        if map[y_p][x_p] == " ":
                            return True
                        if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":
                            return True
            return False
        

def list_right_tower(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♖":
                    for i in range(8 - idx):
                        if i > 0:
                            if map[idy][idx + i] == " " or map[idy][idx + i] == "♚":
                                list_moves.append(f"{idy} {idx + i}")
                            else:
                                break
        return list_moves
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♜":
                    for i in range(8 - idx):
                        if i > 0:
                            if map[idy][idx + i] == " " or map[idy][idx + i] == "♔":
                                list_moves.append(f"{idy} {idx + i}")
                            else:
                                break
        return list_moves


def list_left_tower(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♖":
                    for i in range(idx + 1):
                        if i > 0:
                            if map[idy][idx - i] == " " or map[idy][idx - i] == "♚":
                                list_moves.append(f"{idy} {idx - i}")
                            else:
                                break
        return list_moves
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♜":
                    for i in range(idx + 1):
                        if i > 0:
                            if map[idy][idx - i] == " " or map[idy][idx - i] == "♔":
                                list_moves.append(f"{idy} {idx - i}")
                            else:
                                break
        return list_moves


def list_top_tower(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♖":
                    for i in range(idy + 1):
                        if i > 0:
                            if map[idy - i][idx] == " " or map[idy - i][idx] == "♚":
                                list_moves.append(f"{idy - i} {idx}")
                            else:
                                break
        return list_moves
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♜":
                    for i in range(idy + 1):
                        if i > 0:
                            if map[idy - i][idx] == " " or map[idy - i][idx] == "♔":
                                list_moves.append(f"{idy - i} {idx}")
                            else:
                                break
        return list_moves


def list_bottom_tower(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♖":
                    for i in range(8 - idy):
                        if i > 0:
                            if map[idy + i][idx] == " " or map[idy + i][idx] == "♚":
                                list_moves.append(f"{idy + i} {idx}")
                            else:
                                break
        return list_moves
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♜":
                    for i in range(8 - idy):
                        if i > 0:
                            if map[idy + i][idx] == " " or map[idy + i][idx] == "♔":
                                list_moves.append(f"{idy + i} {idx}")
                            else:
                                break
        return list_moves


def check_can_move_tower_w(y_f, x_f, y_p, x_p, bw):
    answer = bottom(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = top(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = right(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = left(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    else:
        return False