import aiogram
import asyncio

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

map = [["♜","♞","♝","♚","♛","♝","♞","♜"],
       ["♟","♟","♟","♟","♟","♟","♟","♟"],
       [" "," "," "," "," "," "," "," "],
       [" "," "," "," "," "," "," "," "],
       [" "," "," "," "," "," "," "," "],
       [" "," "," "," "," "," "," "," "],
       ["♙","♙","♙","♙","♙","♙","♙","♙"],
       ["♖","♘","♗","♔","♕","♗","♘","♖"]]

#" " - ничего
#♙ - пешка белая
#♖ - башня белая
#♘ - конь белая
#♗ - слон белая
#♔ - король белая
#♕ - ферзь белая
#♟ - пешка чёрная
#♜ - башня чёрная
#♞ - конь чёрная
#♝ - слон чёрная
#♚ - король чёрная
#♛ - ферзь чёрная

#1 число - обозначительный знак
#2 число - y по массиву
#3 число - x по массиву
def send_map():
       mapa = InlineKeyboardMarkup(inline_keyboard=[
                                                 [InlineKeyboardButton(text=f"{map[0][0]}", callback_data="y 0 0"), 
                                                 InlineKeyboardButton(text=f"{map[0][1]}", callback_data="y 0 1"),
                                                 InlineKeyboardButton(text=f"{map[0][2]}", callback_data="y 0 2"),
                                                 InlineKeyboardButton(text=f"{map[0][3]}", callback_data="y 0 3"),
                                                 InlineKeyboardButton(text=f"{map[0][4]}", callback_data="y 0 4"),
                                                 InlineKeyboardButton(text=f"{map[0][5]}", callback_data="y 0 5"),
                                                 InlineKeyboardButton(text=f"{map[0][6]}", callback_data="y 0 6"),
                                                 InlineKeyboardButton(text=f"{map[0][7]}", callback_data="y 0 7")],
                                                 [InlineKeyboardButton(text=f"{map[1][0]}", callback_data="y 1 0"), 
                                                 InlineKeyboardButton(text=f"{map[1][1]}", callback_data="y 1 1"),
                                                 InlineKeyboardButton(text=f"{map[1][2]}", callback_data="y 1 2"),
                                                 InlineKeyboardButton(text=f"{map[1][3]}", callback_data="y 1 3"),                                               
                                                 InlineKeyboardButton(text=f"{map[1][4]}", callback_data="y 1 4"),
                                                 InlineKeyboardButton(text=f"{map[1][5]}", callback_data="y 1 5"),
                                                 InlineKeyboardButton(text=f"{map[1][6]}", callback_data="y 1 6"),
                                                 InlineKeyboardButton(text=f"{map[1][7]}", callback_data="y 1 7")],
                                                 [InlineKeyboardButton(text=f"{map[2][0]}", callback_data="y 2 0"), 
                                                 InlineKeyboardButton(text=f"{map[2][1]}", callback_data="y 2 1"),
                                                 InlineKeyboardButton(text=f"{map[2][2]}", callback_data="y 2 2"),
                                                 InlineKeyboardButton(text=f"{map[2][3]}", callback_data="y 2 3"),
                                                 InlineKeyboardButton(text=f"{map[2][4]}", callback_data="y 2 4"),
                                                 InlineKeyboardButton(text=f"{map[2][5]}", callback_data="y 2 5"),
                                                 InlineKeyboardButton(text=f"{map[2][6]}", callback_data="y 2 6"),
                                                 InlineKeyboardButton(text=f"{map[2][7]}", callback_data="y 2 7")],
                                                 [InlineKeyboardButton(text=f"{map[3][0]}", callback_data="y 3 0"), 
                                                 InlineKeyboardButton(text=f"{map[3][1]}", callback_data="y 3 1"),
                                                 InlineKeyboardButton(text=f"{map[3][2]}", callback_data="y 3 2"),
                                                 InlineKeyboardButton(text=f"{map[3][3]}", callback_data="y 3 3"),
                                                 InlineKeyboardButton(text=f"{map[3][4]}", callback_data="y 3 4"),
                                                 InlineKeyboardButton(text=f"{map[3][5]}", callback_data="y 3 5"),
                                                 InlineKeyboardButton(text=f"{map[3][6]}", callback_data="y 3 6"),
                                                 InlineKeyboardButton(text=f"{map[3][7]}", callback_data="y 3 7")],
                                                 [InlineKeyboardButton(text=f"{map[4][0]}", callback_data="y 4 0"), 
                                                 InlineKeyboardButton(text=f"{map[4][1]}", callback_data="y 4 1"),
                                                 InlineKeyboardButton(text=f"{map[4][2]}", callback_data="y 4 2"),
                                                 InlineKeyboardButton(text=f"{map[4][3]}", callback_data="y 4 3"),
                                                 InlineKeyboardButton(text=f"{map[4][4]}", callback_data="y 4 4"),
                                                 InlineKeyboardButton(text=f"{map[4][5]}", callback_data="y 4 5"),
                                                 InlineKeyboardButton(text=f"{map[4][6]}", callback_data="y 4 6"),
                                                 InlineKeyboardButton(text=f"{map[4][7]}", callback_data="y 4 7")],
                                                 [InlineKeyboardButton(text=f"{map[5][0]}", callback_data="y 5 0"), 
                                                 InlineKeyboardButton(text=f"{map[5][1]}", callback_data="y 5 1"),
                                                 InlineKeyboardButton(text=f"{map[5][2]}", callback_data="y 5 2"),
                                                 InlineKeyboardButton(text=f"{map[5][3]}", callback_data="y 5 3"),
                                                 InlineKeyboardButton(text=f"{map[5][4]}", callback_data="y 5 4"),
                                                 InlineKeyboardButton(text=f"{map[5][5]}", callback_data="y 5 5"),
                                                 InlineKeyboardButton(text=f"{map[5][6]}", callback_data="y 5 6"),
                                                 InlineKeyboardButton(text=f"{map[5][7]}", callback_data="y 5 7")],
                                                 [InlineKeyboardButton(text=f"{map[6][0]}", callback_data="y 6 0"), 
                                                 InlineKeyboardButton(text=f"{map[6][1]}", callback_data="y 6 1"),
                                                 InlineKeyboardButton(text=f"{map[6][2]}", callback_data="y 6 2"),
                                                 InlineKeyboardButton(text=f"{map[6][3]}", callback_data="y 6 3"),
                                                 InlineKeyboardButton(text=f"{map[6][4]}", callback_data="y 6 4"),
                                                 InlineKeyboardButton(text=f"{map[6][5]}", callback_data="y 6 5"),
                                                 InlineKeyboardButton(text=f"{map[6][6]}", callback_data="y 6 6"),
                                                 InlineKeyboardButton(text=f"{map[6][7]}", callback_data="y 6 7")],
                                                 [InlineKeyboardButton(text=f"{map[7][0]}", callback_data="y 7 0"), 
                                                 InlineKeyboardButton(text=f"{map[7][1]}", callback_data="y 7 1"),
                                                 InlineKeyboardButton(text=f"{map[7][2]}", callback_data="y 7 2"),
                                                 InlineKeyboardButton(text=f"{map[7][3]}", callback_data="y 7 3"),
                                                 InlineKeyboardButton(text=f"{map[7][4]}", callback_data="y 7 4"),
                                                 InlineKeyboardButton(text=f"{map[7][5]}", callback_data="y 7 5"),
                                                 InlineKeyboardButton(text=f"{map[7][6]}", callback_data="y 7 6"),
                                                 InlineKeyboardButton(text=f"{map[7][7]}", callback_data="y 7 7")]])
       return mapa