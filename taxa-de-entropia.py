import math

n = int(input())

probabilidades = []
bits = []

for i in range(n):
  p, l = input().split()
  p = float(p)
  l = int(l)
  probabilidades.append(p)
  bits.append(l)

# Cálculo da entropia
H = 0
for p in probabilidades:
  H -= p * math.log2(p)

# Cálculo do número médio de bits
L = 0
for i in range(n):
  L += probabilidades[i] * bits[i]

print(f"{H:.4f}")
print(f"{L:.4f}")
