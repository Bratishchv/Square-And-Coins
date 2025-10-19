from tkinter import *

INST = """                  Инструкция к игре «Squares And Coins»

    Управление
        WASD или стрелки — движение персонажа
        Пробел — активация турбо-режима
        I — вызов инструкции

    Цель игры
        Собрать как можно больше монет за отведенное время, 
            избегая красного квадрата (врага).

    Элементы игры
        Зеленый квадрат — ваш персонаж
        Красный квадрат — враг, которого нужно избегать
        Цветные круги — монеты разных типов
        Верхняя панель — отображает время, уровень 
            и счет

    Типы монет
        Желтые монеты (+3 очка) — крупные бонусы
        Зеленые монеты (+1 очко) — стандартные монеты
        Жёлтые, сливающиеся с фоном мины (-1 жизнь) — опасные предметы
        Синие монеты (+2 очка) — средние бонусы
                        ...мотайте ниже...
        Белые монеты (+5 очков) — редкие крупные бонусы

    Особенности игры
        Турбо-режим — увеличивает скорость персонажа при зажатом пробеле
        Автоматическое ускорение — скорость растет с набором очков
        Система уровней — переход на следующий уровень при наборе 
            определенного количества очков
        Таймер — игра заканчивается при истечении времени

    Советы по игре
        Используйте турбо-режим для быстрого сбора монет
        Избегайте столкновения с красным квадратом
        Следите за временем на верхней панели
        Собирайте белые монеты для быстрого набора очков
        При опасности используйте маневренность персонажа

    Завершение игры
        Игра заканчивается в следующих случаях:
        
        Истечение времени
        Изчезновение всех жизней
        Нажатие на крестик окна

    Для повторного запуска нажмите пробел 
        после завершения игры"""



def instruction(current_name, current_sound):
    global root, butt_sound, name

    def close():
        global butt_sound, name
        
        close.result = {
            'name': name.get(),
            'sound': "🔊" if butt_sound["text"] == "🔊" else "🔊"
        }

        root.destroy()
        root.quit()

    def set_btt_sound():
        global butt_sound
        butt_sound["text"] = "🔊" if butt_sound["text"] == "🔇" else "🔇"

    root = Tk()
    root.protocol("WM_DELETE_WINDOW", close)
    root.geometry("600x565")
    root.title("Инструкция и настройки")    

    app = Frame(root)
    app.grid()

    instruction_text = Text(app)
    instruction_text.insert(0.0, INST)
    instruction_text.grid(column=0, row=0, columnspan=2, rowspan=2)

    Label(app, text="                                                                                     Настройки").grid(column=0, sticky="w")
    Label(app, text="\nВаше имя: ").grid(sticky="w")

    name = Entry(app)
    name.grid(sticky="w")

  #  Button(app, text="Зарегестрироваться").grid(sticky="w")

    Label(app, text="\nЗвук: ").grid(sticky="w")
    butt_sound = Button(app, text="🔊", command=set_btt_sound)
    butt_sound.grid(sticky="w")

    Button(app, text="Сохранить и выйти               ", command=close).grid(sticky=E, column = 1, row = 3)

    root.mainloop()

    if hasattr(close, 'result'):
        current_name = close.result['name']
        current_sound = close.result['sound']
 
    return current_name, current_sound
