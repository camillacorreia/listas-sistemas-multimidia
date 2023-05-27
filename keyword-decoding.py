symbols = {
  '%': 'carro',
  '$': 'acidente',
  '&': 'senhor',
  '#': 'do'
}

# Entrada do texto comprimido
compressed_text = input()

# Realiza a descompressão do texto
decoded_text = ''
for word in compressed_text.split():
  if word in symbols.keys():
    decoded_text += symbols[word] + ' '
  else:
    decoded_text += word + ' '

decoded_text = decoded_text.rstrip()

# Imprime o resultado da descompressão
print(decoded_text)