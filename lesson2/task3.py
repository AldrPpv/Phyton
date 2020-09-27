season_list = ['зима','зима','весна','весна','весна','лето','лето','лето','осень','осень','осень','зима']
season_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
               10: 'осень', 11: 'осень', 12: 'зима'}
while True:
    mouth = input('Введите месяц в виде целого числа от 1 до 12: ')
    if mouth.isdigit():
        mouth = int(mouth)
    else:
        continue
    # mouth = int(mouth) if mouth.isdigit() else continue - вот так почему-то не работает
    if mouth >=1 and mouth<=12:
        break
print(f'Месяц № {mouth} это - {season_list[mouth-1]} (получено с использованием списка)')
print(f'Месяц № {mouth} это - {season_dict[mouth]} (получено с использованием  словаря)')