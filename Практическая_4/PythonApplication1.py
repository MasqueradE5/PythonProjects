import requests
import random

def main():
    print("Меню: \n",
    "1  Найти персонажа \n",
    "2  Найти эпизод\n",
    "3 Найти локацию\n",
    "4 Случайный персонаж\n",
    "5 Список всех эпизодов\n",
    "6  Выход\n")

    with open("history.txt", "a", encoding="utf-8") as f:
            f.write("Меню: \n" +
                "1  Найти персонажа \n" +
                "2  Найти эпизод\n" +
                "3 Найти локацию\n" +
                "4 Случайный персонаж\n" +
                "5 Список всех эпизодов\n" +
                "6  Выход\n")
            f.write("\n")


    User_input=(int(input("Ваш выбор: ")))
    if User_input == 1:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВВОД ПОЛЬЗОВАТЕЛЯ: \n")
            f.write("\n")
            f.write("1. Найти персонажа" + "\n")
            f.write("\n")
        charfound()
    elif User_input == 2:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВВОД ПОЛЬЗОВАТЕЛЯ: \n")
            f.write("\n")
            f.write("2. Найти эпизод" + "\n")
            f.write("\n")
        episode()
    elif User_input == 3:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВВОД ПОЛЬЗОВАТЕЛЯ: \n")
            f.write("\n")
            f.write("3. Найти локацию" + "\n")
            f.write("\n")
        location()
    elif User_input == 4:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВВОД ПОЛЬЗОВАТЕЛЯ: \n")
            f.write("\n")
            f.write("4. Случайный персонаж" + "\n")
            f.write("\n")
        charrand()
    elif User_input == 5:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВВОД ПОЛЬЗОВАТЕЛЯ: \n")
            f.write("\n")
            f.write("5. Список всех серий" + "\n")
            f.write("\n")
        all_episodes()
    elif User_input == 6:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВВОД ПОЛЬЗОВАТЕЛЯ: \n")
            f.write("\n")
            f.write("6. Выход" + "\n")
            f.write("\n")
        print("Производится выход")
    else:
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВВОД ПОЛЬЗОВАТЕЛЯ: \n")
            f.write("\n")
            f.write(str(User_input) + "\n")
            f.write("\n")
        print("Неверный ввод")
        main()

def all_episodes():
    for i in range(1,52):
        response = requests.get("https://rickandmortyapi.com/api/episode/" + str(i))
        data = response.json()
        print(str(i)+".",data["name"])
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВЫВОД: \n")
            f.write("\n")
            f.write(str(i) + ". "+ data["name"] + "\n")
            f.write("\n")
    main()


def charrand():
    r= random.randint(1, 826)
    response = requests.get("https://rickandmortyapi.com/api/character/" + str(r))
    data = response.json()
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write("ВЫВОД: \n")
        f.write("\n")
        f.write("Имя: " + data["name"] + "\n")
        f.write("Статус: " + data["status"]+"\n")
        f.write("Вид " + data["species"]+"\n")
        f.write("Местонахождение: " + data["location"]["name"]+"\n")
        f.write("Кол-во эпизодов: " + str(len(data["episode"]))+"\n")
        f.write("\n")
    print("Имя: ",data["name"])
    print("Статус: ",data["status"])
    print("Вид: ",data["species"])
    print("Местонахождение: ",data["location"]["name"])
    print("Количество эпизодов: ", len(data['episode']))
    main()


def charfound():
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write("ВЫВОД: \n")
        f.write("\n")
        f.write("Введите имя персонажа: \n")
        f.write("\n")
    User_input= input("Введите имя персонажа: ")
    params = {"name": User_input}
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write("ВВОД ПОЛЬЗОВАТЕЛЯ: \n")
        f.write("\n")
        f.write(User_input +"\n")
        f.write("\n")
    response = requests.get("https://rickandmortyapi.com/api/character", params=params)
    if response.status_code == 200:
        data = response.json()
        print("Имя: ",data["results"][0]["name"])
        print("Статус: ",data["results"][0]["status"])
        print("Вид: ",data["results"][0]["species"])
        print("Местонахождение: ",data["results"][0]["location"]["name"])
        print("Количество эпизодов: ", len(data["results"][0]['episode']))
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВЫВОД: \n")
            f.write("\n")
            f.write("Имя: " + data["results"][0]["name"] + "\n")
            f.write("Статус: " + data["results"][0]["status"]+"\n")
            f.write("Вид " + data["results"][0]["species"]+"\n")
            f.write("Местонахождение: " + data["results"][0]["location"]["name"]+"\n")
            f.write("Кол-во эпизодов: " + str(len(data["results"][0]["episode"]))+"\n")
            f.write("\n")
        main()
    else:
        print("Ошибка ", response.status_code)
        main()

def episode():
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write("ВЫВОД: \n")
        f.write("\n")
        f.write("Введите номер эпизода: \n")
        f.write("\n")
    User_input= input("Введите номер эпизода: ")
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write("ВВОД ПОЛЬЗОВАТЕЛЯ: \n")
        f.write("\n")
        f.write(User_input +"\n")
        f.write("\n")
    response = requests.get("https://rickandmortyapi.com/api/episode/"+ str(User_input))
    if response.status_code == 200:
        data = response.json()
        char_list = []
        print("Название:",data["name"])
        print("Дата выхода",data["air_date"])
        print("Код эпизода:",data["episode"])
        if len(data["characters"]) < 6:
            print("Персонажи:", data["characters"])
        else:
            for i in range(5):
                char_list.append(data["characters"][i])
            print(char_list)
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВЫВОД: \n")
            f.write("\n")
            f.write("Название " + data["name"] + "\n")
            f.write("Дата выхода: " + data["air_date"]+"\n")
            f.write("Код эпизода " + data["episode"]+"\n")
            if len(data["characters"]) < 6:
                f.write("Персонажи: " + data["characters"]["name"]+"\n")
            else:
                f.write("Персонажи: " + str(char_list) + "\n")
            f.write("\n")
        main()
    else:
        print("Ошибка ", response.status_code)
        main()

def location():
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write("ВЫВОД: \n")
        f.write("\n")
        f.write("Введите название локации: \n")
        f.write("\n")
    User_input= input("Введите название локации: ")
    params = {"name": User_input}
    with open("history.txt", "a", encoding="utf-8") as f:
        f.write("ВВОД ПОЛЬЗОВАТЕЛЯ: \n")
        f.write("\n")
        f.write(User_input +"\n")
        f.write("\n")
    response = requests.get("https://rickandmortyapi.com/api/location", params=params)
    if response.status_code == 200:
        data = response.json()
        print("Название", data["results"][0]["name"])
        print("Тип:", data["results"][0]["type"])
        print("Измерение:", data["results"][0]["dimension"])
        print("Число жителей:", len(data["results"][0]["residents"]))
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write("ВЫВОД: \n")
            f.write("\n")
            f.write("Название " + data["results"][0]["name"] + "\n")
            f.write("Тип: " + data["results"][0]["type"]+"\n")
            f.write("Измерение: " + data["results"][0]["dimension"]+"\n")
            f.write("Число жителей: " + str(len(data["results"][0]["residents"]))+"\n")
            f.write("\n")
        main()
    else:
        print("Ошибка ", response.status_code)
        main()

main()
