from datetime import datetime

mannequins_data = [
    {"фамилия": "Иванова", "имя": "Мария", "отчество": "Петровна", "пол": "ж", "национальность": "русская",
     "рост": 175, "вес": 55, "дата рождения": "1995-03-15", "домашний адрес": {"почтовый индекс": "123456",
                                                                               "страна": "Россия",
                                                                               "область": "Московская",
                                                                               "город": "Москва", "улица": "Примерная",
                                                                               "дом": "10", "квартира": "5"}},

]


def find_youngest_mannequin(mannequins_data):
    youngest_mannequin = None
    current_date = datetime.now()

    for mannequin in mannequins_data:
        birth_date = datetime.strptime(mannequin["дата рождения"], "%Y-%m-%d")
        age = (current_date - birth_date).days // 365

        if youngest_mannequin is None or age < youngest_mannequin["возраст"]:
            mannequin["возраст"] = age
            youngest_mannequin = mannequin

    return youngest_mannequin


youngest_mannequin = find_youngest_mannequin(mannequins_data)

print("Самая молодая манекенщица:")
print("ФИО:", youngest_mannequin["фамилия"], youngest_mannequin["имя"], youngest_mannequin["отчество"])
print("Пол:", "Женский" if youngest_mannequin["пол"] == "ж" else "Мужской")
print("Национальность:", youngest_mannequin["национальность"])
print("Рост:", youngest_mannequin["рост"], "см")
print("Вес:", youngest_mannequin["вес"], "кг")
print("Дата рождения:", youngest_mannequin["дата рождения"])
print("Возраст:", youngest_mannequin["возраст"], "лет")
print("Домашний адрес:", youngest_mannequin["домашний адрес"])
