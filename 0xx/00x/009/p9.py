# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
# a^2 + b^2 = c^2
# Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.

for c in range(1, 1000):
  for b in range(1, 1000 - c):
    a = 1000 - c - b
    if a**2 + b**2 == c**2:
      print(a, b, c)
      print(a*b*c)
      break