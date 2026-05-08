import time

print("=== Твой Помощник-Таймер ===")

while True:
    print("\nЧто будем засекать?")
    print("1. Чистка зубов (2 минуты / 120 сек)")
    print("2. Варка яйца всмятку (3 минуты / 180 сек)")
    print("3. Своё время")
    print("4. Выйти")

    choice = input("\nВыбери пункт (1-4): ")

    if choice == "1":
        seconds = 120
        print("\nВремя чистить зубы!")
    elif choice == "2":
        seconds = 180
        print("\n Готовим яйцо!")
    elif choice == "3":
        try:
            seconds = int(input("\nНа сколько секунд запустить таймер? "))
        except ValueError:
            print("Ошибка! Нужно ввести целое число секунд.")
            continue
    elif choice == "4":
        print("\nПока! Пока!")
        break
    else:
        print("Неверный выбор.")
        continue

    print("Время пошло...\n")
    
    for i in range(seconds, 0, -1):
        mins, secs = divmod(i, 60)
        
        timer_format = "{:02d}:{:02d}".format(mins, secs)
        
        print(f"⏱️ {timer_format}", end="\r")
        
        time.sleep(1) 

    print("\n\n🎉 БИП-БИП! Время вышло! Готово! ")
    print("\a")