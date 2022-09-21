#1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#'абвгдейка - это передача' = >" - это передача"

def del_abv():
    get_text=input('Введите любой текст  ')
    print (f'Изначальный текст был {get_text}')
    get_text=get_text.split()
    get_text=" ".join(map(str,[t for t in get_text if 'абв' not in t]))
    print(f'\n Получившийся текст будет {get_text}')
del_abv()    