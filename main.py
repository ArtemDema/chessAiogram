import aiogram
import asyncio

from modules.map_and_inline_b import map, send_map
from modules.peshka import check_move_peshka
from modules.elephant import check_can_move_elephant_w
from modules.tower import check_can_move_tower_w
from modules.horse import check_can_move_horse_w
from modules.queen import check_can_move_queen_w
from modules.king import *

from aiogram import F, Bot, Dispatcher
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

TOKEN = "6819362580:AAEDPLXCEuActglTjK-esTlAfy585hgjFyE"
bot = Bot(TOKEN)
dp = Dispatcher()

yx_for_move = []
answer_for_w_m = 0 #answer for wrong move

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветствую в тестовой версии шахмат в телеграмме(сделаной как вызов от друга).\nДля того что бы начать напишите /confirm")
    

@dp.message(Command("confirm"))
async def game(message: Message):
    await message.answer(text="Ваше игровое поле:", reply_markup=send_map())

@dp.callback_query()
async def move(callback: CallbackQuery):
    global answer_for_w_m

    #Если игрок нажал на инлайн кнопку
    if callback.data.startswith('y'):
        flopa = callback.data.split(" ")

        #добавляем всю информацию с кнопок в массив
        for i in range(len(flopa)):
            yx_for_move.append(flopa[i])
        
        if len(yx_for_move) == 6: #Если было сделано 2 нажатия на инлайн кнопки
            #Переделываю числа с str в int
            yx_for_move[1] = int(yx_for_move[1])
            yx_for_move[2] = int(yx_for_move[2])
            yx_for_move[4] = int(yx_for_move[4])
            yx_for_move[5] = int(yx_for_move[5])
            if map[yx_for_move[1]][yx_for_move[2]] == "♙" or map[yx_for_move[1]][yx_for_move[2]] == "♟": #Проверка на то, что нажимал игрок в первый раз
                #Вызывается проверка на ход для пешки
                if map[yx_for_move[1]][yx_for_move[2]] == "♙":
                    can_move = check_move_peshka(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "white")
                if map[yx_for_move[1]][yx_for_move[2]] == "♟":
                    can_move = check_move_peshka(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "black")
                if can_move: #Если финция дала разрешение на ход
                    #Перемещает фигуру
                    map[yx_for_move[4]][yx_for_move[5]] = map[yx_for_move[1]][yx_for_move[2]]
                    map[yx_for_move[1]][yx_for_move[2]] = " "
                    #Очищается список нажатий
                    yx_for_move.clear()
                    await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                                        reply_markup=send_map())
                else:#Если фунция не дала разрешение на ход
                    answer_for_w_m += 1
                    if answer_for_w_m % 2 == 0:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше", reply_markup=send_map())
                    else:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше!", reply_markup=send_map())
                    yx_for_move.clear()

            elif map[yx_for_move[1]][yx_for_move[2]] == "♖" or map[yx_for_move[1]][yx_for_move[2]] == "♜":
                if map[yx_for_move[1]][yx_for_move[2]] == "♖":
                    can_move = check_can_move_tower_w(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "white")
                if map[yx_for_move[1]][yx_for_move[2]] == "♜":
                    can_move = check_can_move_tower_w(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "black")
                if can_move: 
                    map[yx_for_move[4]][yx_for_move[5]] = map[yx_for_move[1]][yx_for_move[2]]
                    map[yx_for_move[1]][yx_for_move[2]] = " "
                    yx_for_move.clear()
                    await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                                        reply_markup=send_map())
                else:
                    answer_for_w_m += 1
                    if answer_for_w_m % 2 == 0:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше", reply_markup=send_map())
                    else:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше!", reply_markup=send_map())
                    yx_for_move.clear()

            elif map[yx_for_move[1]][yx_for_move[2]] == "♗" or map[yx_for_move[1]][yx_for_move[2]] == "♝":
                if map[yx_for_move[1]][yx_for_move[2]] == "♗":
                    can_move = check_can_move_elephant_w(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "white")
                if map[yx_for_move[1]][yx_for_move[2]] == "♝":
                    can_move = check_can_move_elephant_w(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "black")
                if can_move: 
                    map[yx_for_move[4]][yx_for_move[5]] = map[yx_for_move[1]][yx_for_move[2]]
                    map[yx_for_move[1]][yx_for_move[2]] = " "
                    yx_for_move.clear()
                    await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                                        reply_markup=send_map())
                else:
                    answer_for_w_m += 1
                    if answer_for_w_m % 2 == 0:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше", reply_markup=send_map())
                    else:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше!", reply_markup=send_map())
                    yx_for_move.clear()
            
            elif map[yx_for_move[1]][yx_for_move[2]] == "♘" or map[yx_for_move[1]][yx_for_move[2]] == "♞":
                if map[yx_for_move[1]][yx_for_move[2]] == "♘":
                    can_move = check_can_move_horse_w(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "white")
                if map[yx_for_move[1]][yx_for_move[2]] == "♞":
                    can_move = check_can_move_horse_w(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "black")
                if can_move: 
                    map[yx_for_move[4]][yx_for_move[5]] = map[yx_for_move[1]][yx_for_move[2]]
                    map[yx_for_move[1]][yx_for_move[2]] = " "
                    yx_for_move.clear()
                    await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                                        reply_markup=send_map())
                else:
                    answer_for_w_m += 1
                    if answer_for_w_m % 2 == 0:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше", reply_markup=send_map())
                    else:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше!", reply_markup=send_map())
                    yx_for_move.clear()

            elif map[yx_for_move[1]][yx_for_move[2]] == "♕" or map[yx_for_move[1]][yx_for_move[2]] == "♛":
                if map[yx_for_move[1]][yx_for_move[2]] == "♕":
                    can_move = check_can_move_queen_w(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "white")
                if map[yx_for_move[1]][yx_for_move[2]] == "♛":
                    can_move = check_can_move_queen_w(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "black")
                if can_move: 
                    map[yx_for_move[4]][yx_for_move[5]] = map[yx_for_move[1]][yx_for_move[2]]
                    map[yx_for_move[1]][yx_for_move[2]] = " "
                    yx_for_move.clear()
                    await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                                        reply_markup=send_map())
                else:
                    answer_for_w_m += 1
                    if answer_for_w_m % 2 == 0:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше", reply_markup=send_map())
                    else:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше!", reply_markup=send_map())
                    yx_for_move.clear()

            elif map[yx_for_move[1]][yx_for_move[2]] == "♔" or map[yx_for_move[1]][yx_for_move[2]] == "♚":
                if map[yx_for_move[1]][yx_for_move[2]] == "♔":
                    can_move = main_king(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "white")
                if map[yx_for_move[1]][yx_for_move[2]] == "♚":
                    can_move = main_king(yx_for_move[1],yx_for_move[2],yx_for_move[4], yx_for_move[5], "black")
                if can_move: 
                    map[yx_for_move[4]][yx_for_move[5]] = map[yx_for_move[1]][yx_for_move[2]]
                    map[yx_for_move[1]][yx_for_move[2]] = " "
                    yx_for_move.clear()
                    await bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                                        reply_markup=send_map())
                else:
                    answer_for_w_m += 1
                    if answer_for_w_m % 2 == 0:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше", reply_markup=send_map())
                    else:
                        await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                            text="Нельзя туда ходить. Подумайте лучше!", reply_markup=send_map())
                    yx_for_move.clear()
            elif map[yx_for_move[1]][yx_for_move[2]] == " ":
                answer_for_w_m += 1
                if answer_for_w_m % 2 == 0:
                    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                        text="Первым нажатием надо выбрать фигуру. Подумайте лучше", reply_markup=send_map())
                else:
                    await bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, 
                                        text="Первым нажатием надо выбрать фигуру!", reply_markup=send_map())
                yx_for_move.clear()

        



async def main():
    await dp.start_polling(bot)

asyncio.run(main())