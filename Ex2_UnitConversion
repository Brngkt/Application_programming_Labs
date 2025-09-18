Ed = {
    'км': 1000,
    'м': 1,
    'см': 0.01,
    'мм': 0.001,
    'mi': 1609.34,
    'yd': 0.9144
}

print('Единицы: км, м, см, мм, mi, yd')

old = input('Из: ').lower()
new = input('В: ').lower()

if old in Ed and new in Ed:

    try:
        num = float(input('Значение: '))
        result = num * Ed[old] / Ed[new]
        print(f'{num} {old} = {result:.4f} {new}')
    except:
        print('Введите число')
else:
    print('Введена неизвестная единица')
