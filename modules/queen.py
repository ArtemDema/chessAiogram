from .map_and_inline_b import map
from .elephant import bottom_right, bottom_left, top_right, top_left
from .tower import right, left, top, bottom

#y_f - y фигуры
#x_f - x фигуры
#y_p - y точки(куда хочет походить)
#x_p - x точки(куда хочет походить)
#bw - хранит какого цвета фигура(или какой цвет надо искать и взаимодействовать с ним)

def check_can_move_queen_w(y_f, x_f, y_p, x_p, bw):
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
    answer = top(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = right(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = left(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    answer = bottom(y_f, x_f, y_p, x_p, bw)
    if answer:
        return True
    else:
        return False
    
def list_right_queen(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♕":
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
                if column == "♛":
                    for i in range(8 - idx):
                        if i > 0:
                            if map[idy][idx + i] == " " or map[idy][idx + i] == "♔":
                                list_moves.append(f"{idy} {idx + i}")
                            else:
                                break
        return list_moves


def list_left_queen(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♕":
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
                if column == "♛":
                    for i in range(idx + 1):
                        if i > 0:
                            if map[idy][idx - i] == " " or map[idy][idx - i] == "♔":
                                list_moves.append(f"{idy} {idx - i}")
                            else:
                                break
        return list_moves


def list_top_queen(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♕":
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
                if column == "♛":
                    for i in range(idy + 1):
                        if i > 0:
                            if map[idy - i][idx] == " " or map[idy - i][idx] == "♔":
                                list_moves.append(f"{idy - i} {idx}")
                            else:
                                break
        return list_moves


def list_bottom_queen(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♕":
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
                if column == "♛":
                    for i in range(8 - idy):
                        if i > 0:
                            if map[idy + i][idx] == " " or map[idy + i][idx] == "♔":
                                list_moves.append(f"{idy + i} {idx}")
                            else:
                                break
        return list_moves
    


def list_bottom_right_queen(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♕":
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
                if column == "♛":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy + index < len(map) and idx + index < len(map):
                                    if map[idy + index][idx + index] == " " or map[idy + index][idx + index] == "♔":
                                        list_moves.append(f"{idy + index} {idx + index}")
                                    else:
                                        break
        return list_moves
    

def list_bottom_left_queen(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♕":
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
                if column == "♛":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy + index < len(map) and idx - index >= 0:
                                    if map[idy + index][idx - index] == " " or map[idy + index][idx - index] == "♔":
                                        list_moves.append(f"{idy + index} {idx - index}")
                                    else:
                                        break
        return list_moves
    

def list_top_left_queen(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♕":
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
                if column == "♛":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy - index < len(map) and idx - index < len(map):
                                    if map[idy - index][idx - index] == " " or map[idy - index][idx - index] == "♔":
                                        list_moves.append(f"{idy - index} {idx - index}")
                                    else:
                                        break
        return list_moves
    

def list_top_right_queen(bw):
    list_moves = []
    if bw == "white":
        for idy, row in enumerate(map):
            for idx, column in enumerate(row):
                if column == "♕":
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
                if column == "♛":
                    if idy != 7 and idx != 7:
                        for index in range(len(map) - idy):
                            if index > 0:
                                if idy - index < len(map) and idx + index < len(map):
                                    if map[idy - index][idx + index] == " " or map[idy - index][idx + index] == "♔":
                                        list_moves.append(f"{idy - index} {idx + index}")
                                    else:
                                        break
        return list_moves