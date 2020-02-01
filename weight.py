weight = int(input('weight: '))
unit = input('pound(l)or kilogram(k): ')
if unit.upper == 'L' or 'K':
    convert = weight * 0.45
    print(fss"{convert}")
else:
    convert = weight /0.45
    print(f"{convert}")

