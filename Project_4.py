check = 1
step = 0
letter = 0
start = input(" Хотите измерить длину слова? \n").lower()

if start == "да" or start == "yes":
    while start == "да" or start == "yes":
        word = input("\n Введите слово: ")
        print("В", check, "слове", len(word), "символов.")
        check += 1
        start = input("Хотите измерить длину слова? \n").lower()
        step += 1
        letter += len(word)

    if letter == 0:
        print("\n Символов не было введенно.")
    else:
        print("\n Вы посчитали количество символов в", step, "словe(ах). \n" + "И написали в общей сумме", letter, "символов.")
else:
    print("\n Очень жаль! \n" + "До свидания!")


