dados = input() # lê os dados a serem comprimidos

compressao = "" # string que irá armazenar a compressão
contador = 0 # contador de zeros consecutivos

for d in dados:
  if d == '0':
    contador += 1 # incrementa o contador de zeros consecutivos
  else:
    if contador > 0:
      compressao += '@' + str(contador) # adiciona o símbolo '@' seguido do contador à string de compressão
      contador = 0 # reinicia o contador
    compressao += d # adiciona o dígito não nulo à string de compressão

# adiciona o símbolo '@' e o contador final, se houver zeros consecutivos no final da string
if contador > 0:
  compressao += '@' + str(contador)

print(compressao) # imprime o resultado da compressão