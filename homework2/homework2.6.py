goods=[]
goods_count = int(input("введите количество товаров "))
for el in range(goods_count):
    print("Введите параметры товара:")
    name = input("введите название товара - ")
    cost = input("введите цену товара -")
    count = input("введите количество товара -")
    unit = input("введите единицу товара -")
    good = (el, {"название": name, "цена": cost, "количество": count, "единица": unit})
    goods.append(good)

print(f"Ваши товары: {goods}")

names = []
costs = []
counts = []
units = []

for el in range(len(goods)):
    good = goods[el][1]
    names.append(good.get("название"))
    costs.append(good.get("цена"))
    counts.append(good.get("количество"))
    units.append(good.get("единица"))

analitics = {
    'название': list(set(names)),
    'цена': list(set(costs)),
    'количество': list(set(counts)),
    'ед': list(set(units)),
}
print(f"Аналитика по товарам: {analitics}")











# goods = [
#     (1,{'название': "компьютер",: "20000",'количество':5,'ед': "шт"}),
#     (2,{'название': "принтер",'цена': "6000",'количество':2,'ед': "шт"}),
#     (3,{'название': "сканер",'цена': "2000",'количество':7,'ед': "шт"}),
# ]
# for el in range(len(goods)):
#     good = goods[0]
#     print(good[1].keys())

# my_dict = {
#     'название': ["компьютер","принтер",'сканер"],
#     'цена': ["20000","6000",'2000"],
#     'количество': ["5", "2", '7"],
#     'ед': ["шт"]
# }