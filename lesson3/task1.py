def sub (num_1, num_2):
  return num_1/num_2

a = float (input ('Введите делимое а: '))
b = float (input ('Введите делитель b: '))
try:
  print ('Результат деления a/b: ', sub (a, b))
except ZeroDivisionError:
  print ('Деление на ноль запрещено!')