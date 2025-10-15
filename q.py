import task1
import task2
import task3
import task4
import task5
import task6
import task7
import task8
import task9
import task10


def main():
    while True:
        print("\n" + "=" * 60)
        print("КАЛЬКУЛЯТОР ФИЗИЧЕСКИХ ВЕЛИЧИН")
        print("=" * 60)
        print("Какие вычисления вам нужны? Выберите число от 1 до 10:")
        print("-" * 60)
        print("Задача 1:  Определение скорости")
        print("Задача 2:  Определение массы")
        print("Задача 3:  Определение температуры по Цельсию")
        print("Задача 4:  Определение работы")
        print("Задача 5:  Определение кинетической энергии")
        print("Задача 6:  Определение потенциальной энергии")
        print("Задача 7:  Определение давления")
        print("Задача 8:  Определение теплоты")
        print("Задача 9:  Определение частоты")
        print("Задача 10: Определение объема")
        print("-" * 60)
        print("Если хотите выйти, нажмите Q")
        print("=" * 60)

        c = input("Ваш выбор: ").strip()

        if c.lower() == "q":
            print("\nВсего доброго!")
            break
        elif c == "1":
            task1.speed()
        elif c == "2":
            task2.mass()
        elif c == "3":
            task3.temp()
        elif c == "4":
            task4.work()
        elif c == "5":
            task5.energy()
        elif c == "6":
            task6.pot_energy()
        elif c == "7":
            task7.press()
        elif c == "8":
            task8.qofheat()
        elif c == "9":
            task9.frequency()
        elif c == "10":
            task10.volume()
        else:
            print("Неправильный ввод! Пожалуйста, выберите число от 1 до 10 или Q для выхода.")


if __name__ == "__main__":
    main()