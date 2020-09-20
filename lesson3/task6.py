def int_func(word):
    return word.title()

user_string = input('Введите строку из латинских слов в нижнем регистре, разделенных пробелом: ')
_list = user_string.split()
new_string = ""
for word in range (len(_list)):
    new_string += int_func(_list[word]) + " "
print (new_string)
