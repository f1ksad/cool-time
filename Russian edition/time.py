import time
import os

# Функция для очистки экрана (работает и на Windows, и на Mac/Linux)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("=== ⏱️ Твой Помощник-Таймер ===")

while True:
    print("\nЧто будем засекать?")
    print("1. Чистка зубов (2 минуты / 120 сек)")
    print("2. Варка яйца всмятку (3 минуты / 180 сек)")
    print("3. Обучение по схеме Помидора (25 мин работа / 5 мин отдых)")
    print("4. Своё время")
    print("5. Выйти")

    choice = input("\nВыбери пункт (1-5): ")

    if choice == "1":
        seconds = 120
        print("\n Время чистить зубы!")
    elif choice == "2":
        seconds = 180
        print("\n Готовим идеальное яйцо!")
    elif choice == "3":
        # --- БЛОК ПОМИДОРА ---
        print("\n Время учиться! Сосредоточься.")
        work_time = 1500 # 25 минут
        for i in range(work_time, 0, -1):
            mins, secs = divmod(i, 60)
            timer_format = "{:02d}:{:02d}".format(mins, secs)
            clear_screen()
            print(f" Идет работа: {timer_format}")
            time.sleep(1)
        
        print("\a") # Сигнал об окончании работы
        print("\n🎉 Молодец! Ты заслужил отдых!")
        
        rest_time = 300 # 5 минут
        for i in range(rest_time, 0, -1):
            mins, secs = divmod(i, 60)
            timer_format = "{:02d}:{:02d}".format(mins, secs)
            clear_screen()
            print(f" Время отдыха: {timer_format}")
            time.sleep(1)
            
        print("\a") # Сигнал об окончании отдыха
        print("\n Отдых окончен! Пора возвращаться к делам.")
        continue # Возвращаемся в главное меню

    elif choice == "4":
        try:
            seconds = int(input("\nНа сколько секунд запустить таймер? "))
        except ValueError:
            print("❌ Ошибка! Нужно ввести целое число секунд.")
            continue
    elif choice == "5":
        print("\n Пока! Хорошего дня!")
        break
    else:
        print(" Неверный выбор. Попробуй еще раз.")
        continue

    # --- ОБЩИЙ ТАЙМЕР (для пунктов 1, 2 и 4) ---
    print("\nВремя пошло...")
    for i in range(seconds, 0, -1):
        mins, secs = divmod(i, 60)
        timer_format = "{:02d}:{:02d}".format(mins, secs)
        clear_screen()
        print(f"⏱️ Осталось: {timer_format}")
        time.sleep(1)

    print("\a") # Финальный писк
    print("\n\n🎉 БИП-БИП! Время вышло! Готово!")