import numpy

from .map_and_inline_b import map
from .elephant import *
from .horse import *
from .peshka import *
from .queen import *
from .tower import *

list_moves_peshka = []

#y_f - y фигуры
#x_f - x фигуры
#y_p - y точки(куда хочет походить)
#x_p - x точки(куда хочет походить)
#bw - хранит какого цвета фигура(или какой цвет надо искать и взаимодействовать с ним)
#y_e - y точки(куда может походить вражеская фигура)
#x_e - x точки(куда может походить вражеская фигура)

def check_can_move_king(y_f, x_f, y_p, x_p, bw, list):
    for var in list:
        variable = var.split(" ")
        print(variable)
        variable[0] = int(variable[0])
        variable[1] = int(variable[1])
        ansewr = top_king(y_f, x_f, y_p, x_p, bw, variable[0], variable[1]) #Проверка на ход короля вверх
        if ansewr: #Если вернулось True
            return False #нельзя ходить
        ansewr = bottom_king(y_f, x_f, y_p, x_p, bw, variable[0], variable[1])
        if ansewr:
            return False
        ansewr = left_king(y_f, x_f, y_p, x_p, bw, variable[0], variable[1])
        if ansewr:
            return False
        ansewr = right_king(y_f, x_f, y_p, x_p, bw, variable[0], variable[1])
        if ansewr:
            return False

# Проверка на то, хочет ли игрок походить в возможный предел хода королём
def check_move_king(y_f, x_f, y_p, x_p):
    #top
    if y_p == y_f - 1 and x_p == x_f:
        return True
    if y_p == y_f - 1 and x_p == x_f - 1:
        return True
    if y_p == y_f - 1 and x_p == x_f + 1:
        return True
    #bottom
    if y_p == y_f + 1 and x_p == x_f:
        return True
    if y_p == y_f + 1 and x_p == x_f - 1:
        return True
    if y_p == y_f + 1 and x_p == x_f + 1:
        return True
    #left
    if y_p == y_f and x_p == x_f -  1:
        return True
    if y_p == y_f - 1 and x_p == x_f - 1:
        return True
    if y_p == y_f + 1 and x_p == x_f - 1:
        return True
    #right
    if y_p == y_f and x_p == x_f +  1:
        return True
    if y_p == y_f - 1 and x_p == x_f + 1:
        return True
    if y_p == y_f + 1 and x_p == x_f + 1:
        return True
    
    return False
def top_king(y_f, x_f, y_p, x_p, bw, y_e, x_e):
    if y_f != 0:    #Если фигура не вверху
        if y_p == y_f - 1 and x_p == x_f:   #если точка куда походить совпадает с этим вариантом
            if y_p == y_e and x_p == x_e:   #если точка куда походить, есть в вариантах куда ходить вражеской фигуре
                return True     #нельзя туда ходить

        if x_f != 0:
            if y_p == y_f - 1 and x_p == x_f - 1:
                if y_p == y_e and x_p == x_e:
                    return True

        if x_f != 7:
            if y_p == y_f - 1 and x_p == x_f + 1:
                if y_p == y_e and x_p == x_e:
                    return True


def bottom_king(y_f, x_f, y_p, bw, x_p, y_e, x_e):
    if y_f != 7:
        if y_p == y_f + 1  and x_p == x_f:
            if y_p == y_e and x_p == x_e:
                return True

        if x_f != 0:
            if y_p == y_f + 1 and x_p == x_f - 1:
                if y_p == y_e and x_p == x_e:
                    return True

        if x_f != 7:
            if y_p == y_f + 1 and x_p == x_f + 1:
                if y_p == y_e and x_p == x_e:
                    return True


def left_king(y_f, x_f, y_p, x_p, bw, y_e, x_e):
    if x_f != 0:
        if x_p == x_f - 1 and y_p == y_f:
            if y_p == y_e and x_p == x_e:
                return True

        if y_f != 7:
            if y_p == y_f + 1 and x_p == x_f - 1:
                if y_p == y_e and x_p == x_e:
                    return True

        if y_f != 0:
            if y_p == y_f - 1 and x_p == x_f - 1:
                if y_p == y_e and x_p == x_e:
                    return True

            
def right_king(y_f, x_f, y_p, x_p, bw, y_e, x_e):
    if x_f != 7:
        if x_p == x_f + 1 and y_p == y_f:
            if y_p == y_e and x_p == x_e:
                return True

        if y_f != 7:
            if y_p == y_f + 1 and x_p == x_f + 1:
                if y_p == y_e and x_p == x_e:
                    return True

        if y_f != 7:
            if y_p == y_f - 1 and x_p == x_f + 1:
                if y_p == y_e and x_p == x_e:
                    return True


def peshka(y_f, x_f, y_p, x_p, bw):
    if bw == "white":
        top_left = list_top_left_peshka("black")
        top_right = list_top_right_peshka("black")
    if bw == "black":
        top_left = list_top_left_peshka("white")
        top_right = list_top_right_peshka("white")

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, top_left)
    if result == False:
        return False
        
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, top_right)
    if result == False:
        return False
    else:
        return True
        
def elephant(y_f, x_f, y_p, x_p, bw):
    if bw == "white":
        left = list_bottom_left_elephant("black")
        right = list_bottom_right_elephant("black")
        top = list_top_left_elephant("black")
        bottom = list_top_right_elephant("black")
    if bw == "black":
        left = list_bottom_left_elephant("white")
        right = list_bottom_right_elephant("white")
        top = list_top_left_elephant("white")
        bottom = list_top_right_elephant("white")

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, left)
    if result == False:
        return False
        
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, right)
    if result == False:
        return False

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, top)
    if result == False:
        return False

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, bottom)
    if result == False:
        return False
    else:
        return True


def horse(y_f, x_f, y_p, x_p, bw):
    if bw == "white":
        top_left_h = list_top_left_horse("black")
        top_right_h = list_top_right_horse("black")
        right_top_h = list_right_top_horse("black")
        right_bottom_h = list_right_bottom_horse("black")
        bottom_left_h = list_bottom_left_horse("black")
        bottom_right_h = list_bottom_right_horse("black")
        left_top_h = list_left_top_horse("black")
        left_bottom_h = list_left_bottom_horse("black")
    if bw == "black":
        top_left_h = list_top_left_horse("white")
        top_right_h = list_top_right_horse("white")
        right_top_h = list_right_top_horse("white")
        right_bottom_h = list_right_bottom_horse("white")
        bottom_left_h = list_bottom_left_horse("white")
        bottom_right_h = list_bottom_right_horse("white")
        right_top_h = list_right_top_horse("white")
        right_bottom_h = list_right_bottom_horse("white")

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, top_left_h)
    if result == False:
        return False
        
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, top_right_h)
    if result == False:
        return False

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, right_top_h)
    if result == False:
        return False

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, right_bottom_h)
    if result == False:
        return False
    
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, bottom_left_h)
    if result == False:
        return False
    
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, bottom_right_h)
    if result == False:
        return False
    
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, left_top_h)
    if result == False:
        return False
    
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, left_bottom_h)
    if result == False:
        return False
    else:
        return True


def tower(y_f, x_f, y_p, x_p, bw):
    if bw == "white":
        left = list_left_tower("black")
        right = list_right_tower("black")
        top = list_top_tower("black")
        bottom = list_bottom_tower("black")
    if bw == "black":
        left = list_left_tower("white")
        right = list_right_tower("white")
        top = list_top_tower("white")
        bottom = list_bottom_tower("white")

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, left)
    if result == False:
        return False
        
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, right)
    if result == False:
        return False

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, top)
    if result == False:
        return False

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, bottom)
    if result == False:
        return False
    else:
        return True
    
    


def queen(y_f, x_f, y_p, x_p, bw):
    if bw == "white":
        left = list_left_queen("black")
        right = list_right_queen("black")
        top = list_top_queen("black")
        bottom = list_bottom_queen("black")
        left_bottom_q = list_bottom_left_queen("black")
        right_bottom_q = list_bottom_right_queen("black")
        left_top_q = list_top_left_queen("black")
        right_top_q = list_top_right_queen("black")
    if bw == "black":
        left = list_left_queen("white")
        right = list_right_queen("white")
        top = list_top_queen("white")
        bottom = list_bottom_queen("white")
        left_bottom_q = list_bottom_left_queen("white")
        right_bottom_q = list_bottom_right_queen("white")
        left_top_q = list_top_left_queen("white")
        right_top_q = list_top_right_queen("white")

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, left)
    if result == False:
        return False
        
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, right)
    if result == False:
        return False

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, top)
    if result == False:
        return False

    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, bottom)
    if result == False:
        return False
    
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, left_bottom_q)
    if result == False:
        return False
    
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, right_bottom_q)
    if result == False:
        return False
    
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, left_top_q)
    if result == False:
        return False
    
    result = check_can_move_king(y_f, x_f, y_p, x_p, bw, right_top_q)
    if result == False:
        return False
    else:
        return True

def main_king(y_f, x_f, y_p, x_p, bw):
    correct = 0
    result = check_move_king(y_f, x_f, y_p, x_p) #Проверка на то, куда ходит игрок(если дальше чем на 1 клетку от короля то нельзя)
    if result:  #Если точка хода не дальше чем 1 клетка
        result_peshka = peshka(y_f, x_f, y_p, x_p, bw)  #проверка пешек
        if result_peshka:   #Если они прошли проверку
            correct += 1    #Сколько фигур прошло проверку(если будет 5 - ходить можно(в конце будет сделано))
        else:   #если пешки проверку не прошли
            return False    #ходить нельзя(в точку куда выбрал игрок)
        
        result_tower = tower(y_f, x_f, y_p, x_p, bw)
        if result_tower:
            correct += 1
        else:
            return False
        
        result_tower = elephant(y_f, x_f, y_p, x_p, bw)
        if result_tower:
            correct += 1
        else:
            return False
        
        result_tower = queen(y_f, x_f, y_p, x_p, bw)
        if result_tower:
            correct += 1
        else:
            return False
        
        print("a")
        result_tower = horse(y_f, x_f, y_p, x_p, bw)
        if result_tower:
            correct += 1
        else:
            return False

        if correct == 5:
            return True