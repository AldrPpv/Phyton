def sum_user_list (str):
    _list = str.split()
    return sum(list(map(float, _list))) if _list.count ("q") == 0 else sum(list (map (float, _list[0:_list.index('q')])))

sum_number = 0
while True:
    user_str = input('Введите строку чисел, разделенных пробелом (для выхода введите "q"): ')
    print('Сумма введенных Вами чисел: ', sum_user_list(user_str))
    sum_number += sum_user_list(user_str)
    print ('Общая сумма: ', sum_number)
    if user_str.find('q'.lower()) != -1:
        break






