def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.remove(my_list[my_list.index(min(my_list))])
    return sum(my_list)


print(my_func(1, -2, -3))
