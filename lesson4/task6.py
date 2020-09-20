from itertools import count, cycle
from sys import argv

my_list = [1, 2, 3, 4, 5]
script_name, number_start, number_end = argv
for el in count(int (number_start)+1):
    if el >= int(number_end):
        break
    else:
        print(el)
iter = cycle(my_list)
for _ in range(10):
    print(next(iter))