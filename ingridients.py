# import random
# import collections

# proteins_with_weights = {
#     'Консервированный тунец': 90,
#     'Лосось': 30,
#     'Мидии': 30, 
#     'Морской коктейль': 30,
#     'Куриные грудки': 30,
#     'Буженина': 30
# }

# # print([key for key in proteins_with_weights.keys()])
# # print(proteins_with_weights.values())

# print(collections.Counter( random.choices([key for key in proteins_with_weights.keys()], [key for key in proteins_with_weights.values()])[0]         for _ in range(100000)))




proteins = [
    'Консервированный тунец',
    'Лосось',
    'Мидии', 
    'Морской коктейль',
    'Куриные грудки',
    'Буженина',
    'Гуляш',
    'Селедка',
    'Пармезан',
    'Моцарелла',
    'Чечевица',
    'Детские сосиски',
    'Сибас',
    'Крабовые палочки',
    'Яйца',
    'Треска',
    'Соленая рыба',
    'Креветки',
    'Нут',
    'Фарш из грудки',
    'Твердый сыр',
    'Фета',
    'Адыгейский сыр'
]

carbs = [
    'Макароны',
    'Рисовая лапша',
    'Гречневая лапша',
    'Фунчоза',
    'Картошка',
    'Батат',
    'Рис',
    'Булгур',
    'Кус-кус',
    'Нут',
    'Кукурузная крупа',
    'Ячневая крупа',
    'Цельнозерновой хлеб',
    'Пита/лаваш',
    'Картофельное пюре',
]

fats = [
    'Авокадо',
    'Оливковое масло',
    'Оливки',
    'Маслины',
    'Печень трески',
    'Орехи',
    'Кунжут',
    'Паштет',
    'Сливочное масло',
]

fiber = [
    'Салат',
    'Замороженная овощная смесь',
    'Огурцы',
    'Помидоры',
    'Сладкий перец',
    'Морковь',
    'Айсберг',
    'Руккола',
    'Брокколи',
    'Зеленая фасоль',
    'Цветная капуста',
    'Кабачки',
    'Шампиньоны',
    'Шпинат',
    'Морская капуста',
    'Воздушные хлебцы',
    'Зеленый горошек',
]
