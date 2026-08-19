temp_F = [24.3, 69.2, 26.8, 71.2, 29.3, 72.8, 27.0, 71.7, 30.3, 73.4]

temp_C = list(map(lambda t: (t - 32) * 5 / 9, temp_F))
print(temp_C)

base = lambda number: (bin(number), oct(number), hex(number))
print(base(10))