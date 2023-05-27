def rgb_to_ycbcr(rgb):
  R, G, B = rgb

  EY = 0.299 * (R/255) + 0.587 * (G/255) + 0.114 * (B/255)
  ECb = -0.169 * (R/255) - 0.331 * (G/255) + 0.500 * (B/255)
  ECr = 0.500 * (R/255) - 0.419 * (G/255) - 0.081 * (B/255)

  Y = 219 * EY + 16
  Cb = 224 * ECb + 128
  Cr = 224 * ECr + 128

  return Y, Cb, Cr

# Leitura dos valores RGB
R, G, B = map(int, input().split())

# Conversão para YCbCr
Y, Cb, Cr = rgb_to_ycbcr((R, G, B))

# Impressão do resultado
print(round(Y), round(Cb), round(Cr))