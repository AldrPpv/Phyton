list = [100, 234.56, "string", True, [1,2,"str"],{'1':1, '2':2, 'True': 1},(1.0, 2, False)]
print(list, '\n', '-' * 100)
for element in list:
    print(element, type(element), '\n','-' * 50)