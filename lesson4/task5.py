from functools import reduce
def my_func (a, b):
    return a * b

new_list = [_ for _ in range(100, 1001) if _ % 2 == 0]
print(reduce(my_func, new_list))
