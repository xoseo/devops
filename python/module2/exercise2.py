import sys
import math

if not len(sys.argv) == 4:
    sys.exit('Скрипт принимает три числа')

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a + b > c and a + c > b and b + c > a:
	pass
else:
	sys.exit("С такими сторонами треугольник не существует")

p = (a + b + c) / 2


s = math.sqrt(p * (p -a) * (p - b) * (p - c))

print(round(s, 2))