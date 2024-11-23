from .map_and_inline_b import map

#Нужные для роботы фунции

#y_f - y фигуры
#x_f - x фигуры
#y_p - y точки(куда хочет походить)
#x_p - x точки(куда хочет походить)
#bw - хранит какого цвета фигура(или какой цвет надо искать и взаимодействовать с ним)

#
def top_left(y_f, x_f, y_p, x_p, bw):
    if y_f - 2 >= 0 and x_f - 1 >= 0:
        if x_p == x_f - 1 and y_p == y_f - 2:
            if map[y_p][x_p] == " ":
                return True
            if bw == "white":
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True
            else:
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True

#
def top_right(y_f, x_f, y_p, x_p, bw):
    if y_f - 2 >= 0 and x_f + 1 <= 7:
        if x_p == x_f + 1 and y_p == y_f - 2:
            if map[y_p][x_p] == " ":
                return True
            if bw == "white":
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True
                else:
                    if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                        return True

#
def right_top(y_f, x_f, y_p, x_p, bw):
    if y_f - 1 >= 0 and x_f + 2 <= 7:
        if x_p == x_f + 2 and y_p == y_f - 1:
            if map[y_p][x_p] == " ":
                return True
            if bw == "white":
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True
            else:
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                        return True

#
def right_bottom(y_f, x_f, y_p, x_p, bw):
    if y_f + 1 <= 7 and x_f + 2 <= 7:
        if x_p == x_f + 2 and y_p == y_f + 1:
            if map[y_p][x_p] == " ":
                return True
            if bw == "white":
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True
                else:
                    if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                        return True
            
#
def bottom_left(y_f, x_f, y_p, x_p, bw):
    if y_f + 2 <= 7 and x_f - 1 >= 0:
        if x_p == x_f - 1 and y_p == y_f + 2:
            if map[y_p][x_p] == " ":
                return True
            if bw == "white":
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True
            else:
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True

#
def bottom_right(y_f, x_f, y_p, x_p, bw):
    if y_f + 2 <= 7 and x_f + 1 <= 7:
        if x_p == x_f + 1 and y_p == y_f + 2:
            if map[y_p][x_p] == " ":
                return True
            if bw == "white":
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True
            else:
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True

#
def left_top(y_f, x_f, y_p, x_p, bw):
    if y_f - 1 >= 0 and x_f - 2 >= 0:
        if x_p == x_f - 2 and y_p == y_f - 1:
            if map[y_p][x_p] == " ":
                return True
            if bw == "white":
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True
            else:
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True

#
def left_bottom(y_f, x_f, y_p, x_p, bw):
    if y_f + 1 <= 7 and x_f - 2 >= 0:
        if x_p == x_f - 2 and y_p == y_f + 1:
            if map[y_p][x_p] == " ":
                return True
            if bw == "white":
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♙" and map[y_p][x_p] != "♖" and map[y_p][x_p] != "♘" and map[y_p][x_p] != "♗" and map[y_p][x_p] != "♔" and map[y_p][x_p] != "♕":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True
            else:
                if map[y_p][x_p] != " " and map[y_p][x_p] != "♟" and map[y_p][x_p] != "♜" and map[y_p][x_p] != "♞" and map[y_p][x_p] != "♝" and map[y_p][x_p] != "♚" and map[y_p][x_p] != "♛":#Проверка на то, пытается ли съесть игрок вражескую фигуру
                    return True
                

def list_top_left_horse(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♘":
                    if idy - 2 >= 0 and idx - 1 >= 0:
                        if map[idy - 2][idx - 1] == " " or map[idy - 2][idx - 1] == "♚":
                            list_moves.append(f"{idy - 2} {idx - 1}")
                        else:
                            break
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♞":
                    if idy - 2 >= 0 and idx - 1 >= 0:
                        if map[idy - 2][idx - 1] == " " or map[idy - 2][idx - 1] == "♔":
                            list_moves.append(f"{idy - 2} {idx - 1}")
                        else:
                            break
    return list_moves
            

def list_top_right_horse(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♘":
                    if idy - 2 >= 0 and idx + 1 <= 7:
                        if map[idy - 2][idx + 1] == " " or map[idy - 2][idx + 1] == "♚":
                            list_moves.append(f"{idy - 2} {idx + 1}")
                        else:
                            break
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♞":
                    if idy - 2 >= 0 and idx + 1 <= 7:
                        if map[idy - 2][idx + 1] == " " or map[idy -  2][idx + 1] == "♔":
                            list_moves.append(f"{idy - 2} {idx + 1}")
                        else:
                            break
    return list_moves


def list_right_top_horse(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♘":
                    if idy - 1 >= 0 and idx + 2 <= 7:
                        if map[idy - 1][idx + 2] == " " or map[idy - 1][idx + 2] == "♚":
                            list_moves.append(f"{idy - 1} {idx + 2}")
                        else:
                            break
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♞":
                    if idy - 1 >= 0 and idx + 2 <= 7:
                        if map[idy - 1][idx + 2] == " " or map[idy - 1][idx + 2] == "♔":
                            list_moves.append(f"{idy - 1} {idx + 2}")
                        else:
                            break
    return list_moves


def list_right_bottom_horse(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♘":
                    if idy + 1 <= 7 and idx + 2 <= 7:
                        if map[idy + 1][idx + 2] == " " or map[idy + 1][idx + 2] == "♚":
                            list_moves.append(f"{idy + 1} {idx + 2}")
                        else:
                            break
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♞":
                    if idy + 1 <= 7 and idx + 2 <= 7:
                        if map[idy + 1][idx + 2] == " " or map[idy + 1][idx + 2] == "♔":
                            list_moves.append(f"{idy + 1} {idx + 2}")
                        else:
                            break
    return list_moves


def list_bottom_left_horse(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♘":
                    if idy + 2 <= 7 and idx - 1 >= 0:
                        if map[idy + 2][idx - 1] == " " or map[idy + 2][idx - 1] == "♚":
                            list_moves.append(f"{idy + 2} {idx - 1}")
                        else:
                            break
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♞":
                    if idy + 2 <= 7 and idx - 1 >= 0:
                        if map[idy + 2][idx - 1] == " " or map[idy + 2][idx - 1] == "♔":
                            list_moves.append(f"{idy + 2} {idx - 1}")
                        else:
                            break
    print("asd")
    print(list_moves)
    return list_moves


def list_bottom_right_horse(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♘":
                    if idy + 2 <= 7 and idx + 1 <= 7:
                        if map[idy + 2][idx + 1] == " " or map[idy + 2][idx + 1] == "♚":
                            list_moves.append(f"{idy + 2} {idx + 1}")
                        else:
                            break
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♞":
                    if idy + 2 <= 7 and idx + 1 <= 7:
                        if map[idy + 2][idx + 1] == " " or map[idy + 2][idx + 1] == "♔":
                            list_moves.append(f"{idy + 2} {idx + 1}")
                        else:
                            break
    return list_moves


def list_left_top_horse(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♘":
                    if idy - 1 >= 0 and idx - 2 >= 0:
                        if map[idy - 1][idx - 2] == " " or map[idy - 1][idx - 2] == "♚":
                            list_moves.append(f"{idy - 1} {idx - 2}")
                        else:
                            break
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♞":
                    if idy - 1 >= 0 and idx - 2 >= 0:
                        if map[idy - 1][idx - 2] == " " or map[idy - 1][idx - 2] == "♔":
                            list_moves.append(f"{idy - 1} {idx - 2}")
                        else:
                            break
    return list_moves


def list_left_bottom_horse(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♘":
                    if idy + 1 <= 7 and idx - 2 >= 0:
                        if map[idy + 1][idx - 2] == " " or map[idy + 1][idx - 2] == "♚":
                            list_moves.append(f"{idy + 1} {idx - 2}")
                        else:
                            break
    if bw == "black":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♞":
                    if idy + 1 <= 7 and idx - 2 >= 0:
                        if map[idy + 1][idx - 2] == " " or map[idy + 1][idx - 2] == "♔":
                            list_moves.append(f"{idy + 1} {idx - 2}")
                        else:
                            break
    return list_moves



def check_can_move_horse_w(y_f, x_f, y_p, x_p, bw):
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
    answer = right_top(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = right_bottom(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = left_top(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = left_bottom(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    else:
        return False