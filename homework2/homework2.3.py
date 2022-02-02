seasons_list = [
    {12 : 'winter', 1 : 'winter', 2 : 'winter'},
    {3 : 'spring', 4 : 'spring', 5 : 'spring'},
    {6: 'summer', 7: 'summer', 8: 'summer'},
    {9: 'autumn', 10: 'autumn', 11: 'autumn'}
]
month = int(input("Введите номер месяца"))
if month >= 1 and month <= 12:
    for num in range(len(seasons_list)):
        season = seasons_list[num].get(month)
        if season != None:
            print(season)
else:
    print("Вы ввели несуществующий номер месяца")