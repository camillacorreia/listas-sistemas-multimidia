tabela_quantizacao = [
  [16, 11, 10, 16, 24, 40, 51, 61],
  [12, 12, 14, 19, 26, 58, 60, 55],
  [14, 13, 16, 24, 40, 57, 69, 56],
  [14, 17, 22, 29, 51, 87, 80, 62],
  [18, 22, 37, 56, 68, 109, 103, 77],
  [24, 35, 55, 64, 81, 104, 113, 92],
  [49, 64, 78, 87, 103, 121, 120, 101],
  [72, 92, 95, 98, 112, 100, 103, 99]
]

def quantizar_matriz(matriz):
  matriz_quantizada = []
  for i in range(8):
    linha_quantizada = []
    for j in range(8):
      valor_quantizado = round(matriz[i][j] / tabela_quantizacao[i][j])
      linha_quantizada.append(valor_quantizado)
    matriz_quantizada.append(linha_quantizada)
  return matriz_quantizada

# Leitura da matriz de entrada
matriz_entrada = []
for _ in range(8):
  linha = input().split()
  linha = [float(valor) for valor in linha]
  matriz_entrada.append(linha)

# Quantização da matriz de entrada
matriz_quantizada = quantizar_matriz(matriz_entrada)

# Impressão da matriz resultante quantizada
for linha in matriz_quantizada:
  print(' '.join(str(valor) for valor in linha))