check = 1
step = 0
letter = 0
start = input(" Хотите измерить длину слова? \n").lower()

if start == "да":
    while start == "да":
        word = input("\n Введите слово: ")
        print("В", check, "слове", len(word), "букв.")
        check += 1
        start = input("Хотите измерить длину слова? \n").lower()
        step += 1
        letter += len(word)

    print("\n Вы посчитали количество букв в", step, "словах. \n" + "И написали в общей сумме", letter, "букв.")

else:
    print("\n Очень жаль! \n" + "До свидания!")


