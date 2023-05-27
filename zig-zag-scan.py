def zig_zag_scan(matriz):
  vetor = []
  i, j = 0, 0
  tamanho = 8
  direcao = 1

  for _ in range(64):
    vetor.append(matriz[i][j])
    if i == tamanho - 1 and j == tamanho - 1:
      break

    if direcao == 1:
      if j == tamanho - 1:
        i += 1
        direcao = -1
      elif i == 0:
        j += 1
        direcao = -1
      else:
        i -= 1
        j += 1
    else:
      if i == tamanho - 1:
        j += 1
        direcao = 1
      elif j == 0:
        i += 1
        direcao = 1
      else:
        i += 1
        j -= 1

  return vetor

# Leitura da matriz de entrada
matriz_entrada = []
for _ in range(8):
  linha = input().split()
  linha = [int(valor) for valor in linha]
  matriz_entrada.append(linha)

# Aplicação do Zig Zag Scan
vetor_resultante = zig_zag_scan(matriz_entrada)

# Impressão do vetor resultante
print(' '.join(str(valor) for valor in vetor_resultante))