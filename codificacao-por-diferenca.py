n = int(input()) # lê a quantidade de amostras
amostras = list(map(int, input().split())) # lê os valores das amostras

codificacao = [amostras[0]] # lista que irá armazenar os valores da codificação

for i in range(1, n):
  diferenca = amostras[i] - amostras[i-1] # calcula a diferença entre a amostra atual e a anterior
  codificacao.append(diferenca) # adiciona a diferença à lista de codificação

print(' '.join(map(str, codificacao))) # imprime o resultado da codificação separado por espaços