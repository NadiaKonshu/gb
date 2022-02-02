el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0

while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1
el = 0
for elem in range(int(len(my_list)/2)):
        left_elem = my_list[el]
        right_elem = my_list[el + 1]
        my_list[el] = right_elem
        my_list[el + 1] = left_elem
        el += 2
print(my_list)











