a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a <= 0 or b <= 0 or c <= 0:
   print('Стороны должны быть положительными!')

elif a + b <= c or a + c <= b or b + c <= a:
   print('Это не треугольник')

else:
   p = (a + b + c) / 2
   s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
   print(f'S = {s:.2f}')
