#Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
#Предусмотрите последний ход, ибо там конфет остается меньше.
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""
import random

def get_number(message):
     while True:
      input_nomber = input(message)
      if not input_nomber.isnumeric():
        print("Вы ввели не число. Попробуйте снова: ")
      elif not 0 < int(input_nomber):
        print("Ваше число не диапазоне. Попробуйте снова ")
      else:
         break
     return int (input_nomber)

def user_interfece():
    print(5*'\n') 
    print('Добро пожаловать в игру, сделайте так , чтобы противник взял последнюю конфету')
    total_count=get_number('Введите количество конфет в куче: ')
    while True:
        turn=get_number('Введите количество конфет, которое можно забрать за ход.\n Оно должно быть меньше общего количества конфет  ')
        if turn>=total_count:
            print('Превышен лимит общего количества конфет в куче. Повторите ввод  ')
        elif turn<total_count:
            break
    while True :
        user_choise=get_number('Если вы хотите играть против человека введите 1\n Если вы хотите играть против компьютера, введите 2 ')   
        print('Кто будет первым ходить? Будет брошен случайный жребий \n') 
        if user_choise==1:
            game_logic_pvp(total_count,turn)
            break
        elif user_choise==2:
           game_logic_pve(total_count,turn)
           break
        else:
            print('Введите 1 или 2 ')



def play_game (total_count,trun):
    while True:
        play_input=get_number(f'Введите число в диапозоне от 1 до {trun}  ')
        print ('\n')
        if play_input<=trun and play_input>0:
            break
    print (f'Берём {play_input} конфет')    
    total_count-=play_input
    return int (total_count)

def computer_game(total_count,trun) :
         if total_count<trun:
           trun = trun-(trun-total_count)
         print(f'Компьютер берёт {trun} конфет')   
         total_count-=trun
         return int (total_count)  

def game_logic_pvp(total_count,trun):
    is_turn=random.randint(1,2)
    while total_count>1:
        if is_turn%2==0:
            print(f'Ход первого игрока.\n В куче {total_count} конфет')  
            total_count = play_game(total_count,trun)
            is_turn+=1
        if total_count>0 and is_turn%2!=0:
              print(f'Ход второго игрока.\n В куче {total_count} конфет')  
              total_count = play_game(total_count,trun)
              is_turn+=1
        if total_count<trun:
            trun=trun-(trun-total_count)  
            print(f'В куче осталось {total_count} конфет') 
    if is_turn%2==0:
        print('Игрок 1 вы проиграли, последний ход остался за вами') 
    if is_turn%2!=0:
        print('Игрок 2 вы проиграли, последний ход остался за вами')    
def game_logic_pve(total_count,trun):
    is_turn=random.randint(1,2)
    while total_count>1:
        if is_turn%2==0:
            print(f'Ход игрока.\n В куче {total_count} конфет\n')
            total_count=play_game(total_count,trun)
            is_turn+=1
        if is_turn%2!=0 and total_count>0:
            print(f'Ход компьютера.\n В куче {total_count} конфет\n') 
            total_count=computer_game(total_count,trun)
            is_turn+=1  
        if total_count<trun:
            trun=trun-(trun - total_count)  
    print(f'В куче осталось {total_count} конфет')   

    if is_turn%2==0:
        print('Игрок вы проиграли , первый ход осталсяза вами') 
    elif is_turn%2!=0:
        print('Компьютер вы проиграли,последний ход остался за вами') 

user_interfece()


                           


