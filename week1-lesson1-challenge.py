import math

# Ideal Gas Constant
R = 8.31446261815324  
n = 1  

print("Ideal Gas Law")

# 1. Pressure
V = 0.25      
T = 300       
P = (n * R * T) / V
print(f"1. Pressure = {P} Pa")

# 2. Volume
P = 500       
T = 321       
V = (n * R * T) / P
print(f"2. Volume = {V} m³")

# 3. Temperature
P = 2.5e3     
V = 1e-5      
T = (P * V) / (n * R)
print(f"3. Temperature = {T} K")


print("\nNormal Distribution")

def normal_pdf(x, mu, sigma):
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

# 1
y1 = normal_pdf(0.5, 0, 1)
print(f"1. y = {y1}")

# 2
y2 = normal_pdf(-2.8, 3, 0.1)
print(f"2. y = {y2}")

# 3
y3 = normal_pdf(-1, -1, 3)
print(f"3. y = {y3}")