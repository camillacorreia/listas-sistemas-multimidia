symbols = {
  '%': 'carro',
  '$': 'acidente',
  '&': 'senhor',
  '#': 'do'
}

# Entrada do texto
input_text = input()

# Realiza a compressão do texto
compressed_text = ''
for word in input_text.split():
  if word in symbols.values():
    for symbol, meaning in symbols.items():
      if word == meaning:
        compressed_text += symbol + ' '
  else:
    compressed_text += word + ' '

compressed_text = compressed_text.rstrip()
compression_ratio = (1 - len(compressed_text) / len(input_text)) * 100

# Imprime o resultado da compressão e da taxa de compressão
print(compressed_text)
print(f"Taxa de compressão: {compression_ratio:.2f}%")