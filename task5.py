my_list = [7, 5, 3, 3, 2]
my_list.sort(reverse=True)
print('Исходный список ', my_list)
user_number = int(input('Введите число: '))

if my_list.count(user_number) > 0:
    my_list.insert(my_list.index(user_number) + my_list.count(user_number), user_number)
else:
    my_list.append(user_number)
    my_list.sort(reverse = True)

print('Новый список ',  my_list)