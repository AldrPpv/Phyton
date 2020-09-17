text = input('Введите список (в качестве разделителя используйте пробел)')
my_list = text.split()
new_list = []

for element in range (len(my_list)//2):
    new_list.extend([my_list[1],my_list[0]])
    my_list = my_list[2:]

new_list.extend(my_list)
print(new_list)
