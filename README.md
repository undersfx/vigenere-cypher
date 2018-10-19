# Vigenere Cypher

Exercício: Cifra e descifra utilizando o método de Vigenere.

A cifra de Vigenère é um método de criptografia simples que usa uma série de diferentes cifras de César baseadas em letras de uma senha.

Exemplo:

	>>> from vigenere import *
	>>> msg = 'foo'
	>>> key = 'bar'
	>>> cifra(msg, key)
	'gof'
	>>> descifra('gof', key)
	'foo'

Ou:

	$ python3 vigenere.py [c|d] <mensagem> <chave>