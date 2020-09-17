goods = []
count = 1 # счетчик. Он же номер товара
prod = int (input('Сколько товаров Вы хотите внести: ')) # защиту от неправильного ввода сделал в 3-ей задаче
while prod!=0:
    products = [None, {"Название": None, "Цена": None, "Количество": None, "ед": None}]
    products[1]["Название"] = input ("Название: ")
    products[1]["Цена"] = float(input("Цена: "))
    products[1]["Количество"] = int (input("Количество: "))
    products[1]["ед"] = input("ед: ")
    products[0] = count
    prod -= 1
    count += 1
    products = tuple (products)
    goods.append(products)
print("Cтруктура данных 'ТОВАРЫ'\n", goods)
count = 0
_key = list (goods[0][1].keys())
_value = []
analytics = {}
temp = []
while count < len(_key):
    for good in goods:
        _value.append(good[1][_key[count]])
    temp = _value.copy()
    analytics[_key[count]] = temp
    _value.clear()
    count += 1

print("\n\nАналитика о товарах\n", analytics)








