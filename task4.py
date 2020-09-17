user_text = input('Введите строку из нескольких слов, разделённых пробелами: ')
word_list = user_text.split()
for num, el in enumerate (word_list):
    print(f'{num+1}) {el[:10]}')