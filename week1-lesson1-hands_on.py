import math

# 1. Basic arithmetic operations
a = 10
b = 5

print("Basic Arithmetic")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# 2. Math module operations
print("\nMath Module")
print("sqrt(16) =", math.sqrt(16))
print("pow(2, 10) =", math.pow(2, 10))
print("pi =", math.pi)
print("sin(math.pi/6) =", math.sin(math.pi/6))

# 3. Newton law 
print("\nNewton Law")
G = 6.674e-11 

# a) Earth and Sun
m1_a = 1.989e30          
m2_a = 5.972e24          
r_a = 149597870000 

F_a = G * m1_a * m2_a / r_a**2
print(f"F = {F_a} N")

# b) Small masses
m1_b = 70    
m2_b = 0.5   
r_b = 0.75  

F_b = G * m1_b * m2_b / r_b**2
print(f"F = {F_b} N")