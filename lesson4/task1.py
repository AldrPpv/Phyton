from sys import argv

script_name, output_hour, rate_hour, prize = argv
wages = (float (output_hour) * float (rate_hour)) + float(prize)
print('Выработка в часах: ', output_hour)
print('Ставка в час: ', rate_hour)
print('Премия: ', prize)
print("Заработная плата составит", wages)
