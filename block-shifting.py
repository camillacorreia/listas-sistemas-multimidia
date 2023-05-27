def block_shifting(matrix):
  result = [[0 for _ in range(8)] for _ in range(8)]
  for i in range(8):
    for j in range(8):
      result[i][j] = matrix[7 - i][7 - j] - 128  # Subtrair 128 para obter os valores negativos
  return result

# Entrada da matriz
matrix = []
for _ in range(8):
  row = list(map(int, input().split()))
  matrix.append(row)

# Aplicar o algoritmo de block shifting
result = block_shifting(matrix)
inverted_matrix = [row[::-1] for row in result[::-1]]

# Imprimir a matriz resultante
for row in inverted_matrix:
  print(' '.join(map(str, row)))
