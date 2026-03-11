import os
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause(t=1.5):
    time.sleep(t)


def main_menu():
    while True:
        clear()
        print("--- МЕНЮ ---")
        print("1. Белочки и орешки")
        print("2. Последний символ")
        print("3. Выход")

        choice = input("Выберите: ")

        if choice == "1":
            clear()
            print("--- БЕЛОЧКИ ---")
            try:
                n = int(input("Сколько белочек? "))
                k = int(input("Сколько орешков? "))

                if n > 10000 or k > 10000:
                    print("Числа должны быть до 10000!")
                else:
                    res = k // n
                    print("Каждая белочка получит:", res)
            except:
                print("Ошибка! Нужно вводить числа")

            input("\nНажми Enter...")

        elif choice == "2":
            clear()
            print("--- ПОСЛЕДНИЙ СИМВОЛ ---")
            s = input("Введите строку: ")
            if s:
                print("Последний символ:", s[-1])
            else:
                print("Строка пустая!")

            input("\nНажми Enter...")

        elif choice == "3":
            clear()
            print("Пока!")
            pause(1)
            break
        else:
            print("Нет такого пункта")
            pause(1)


main_menu()