from math import factorial as fact


def gen_fact(n):
    for i in range(1, n + 1):
        yield fact(i)


n = 5
for el in gen_fact(n):
    print(el)
