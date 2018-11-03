def key(msg, chave):
	'''Gera a keystream do tamanho da mensagem.'''

	k = 0
	keystream = chave
	
	# Se a chave for maior que a mensagem, reduz a chave
	if len(chave) > len(msg):
		keystream = chave[:len(msg)]

	# Se a mensagem for maior que a chave, repete a chave do inicio até a equivalencia
	while len(keystream) < len(msg):
		if k >= len(chave):
			k = 0
		keystream = keystream + chave[k:k+1]
		k +=1

	return keystream

def cifra(msg, chave):
	'''Cifra mensagem com base e uma chave no padrão de cifra de vigenere.'''

	keystream = key(msg, chave)

	# Converter mensagem para lista de suas letras minusculas
	msg = list(msg.lower())
	keystream = list(keystream.lower())

	# Cifrar
	cifra = ''
	for x in range(len(keystream)):
		# Transforma o keystream em uma lista com o valor que deverá ser deslocado cada caractere
		keystream[x] = ord(keystream[x]) - 97

		if ord(msg[x]) < 97 or ord(msg[x]) > 122:
			cifra = cifra + msg[x]
		elif ord(msg[x]) + keystream[x] > 122:
			cifra = cifra + chr(ord(msg[x]) + keystream[x] - 26)
		else:
			cifra = cifra + chr(ord(msg[x]) + keystream[x])

	return cifra

def descifra(msg, chave):
	'''Descifra mensagem com base e uma chave no padrão de cifra de vigenere.'''

	keystream = key(msg, chave)

	# Converter mensagem para lista de suas letras minusculas
	msg = list(msg.lower())
	keystream = list(keystream.lower())

	# Descifrar
	cifra = ''
	for x in range(len(keystream)):
		# Transforma o keystream em uma lista com o valor que deverá ser deslocado cada caractere
		keystream[x] = ord(keystream[x]) - 97

		if ord(msg[x]) < 97 or ord(msg[x]) > 122:
			cifra = cifra + msg[x]
		elif ord(msg[x]) - keystream[x] < 97:
			cifra = cifra + chr(ord(msg[x]) - keystream[x] + 26)
		else:
			cifra = cifra + chr(ord(msg[x]) - keystream[x])

	return cifra

if __name__ == "__main__":
	import sys

	ajuda = '''Passe todos os parâmetros necessários (ou nenhum, para input durante a execução)

	parâmetros: [c|d] <mensagem> <chave>

	Retorno: :string: cifrada/descifrada'''

	if len(sys.argv) > 1:
		if sys.argv[1] in 'help, -h, --help':
			print(ajuda)
		else:
			try:
				if sys.argv[1] == 'c':
					print(cifra(sys.argv[2], sys.argv[3]))
				elif sys.argv[1] == 'd':
					print(descifra(sys.argv[2], sys.argv[3]))
				else:
					print(ajuda)
			except:
			 	print(ajuda)
	else:
		opc = input('cifrar (c) ou descifrar (d):')
		msg = input('mensagem:')
		chave = input('chave:')

		if opc == 'c':
			print(cifra(msg, chave))
		elif opc == 'd':
			print(descifra(msg, chave))
		else:
			print(ajuda)
