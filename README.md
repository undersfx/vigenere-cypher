# Vigenere Cypher

Exercício: Cifra e descifra utilizando o método de Vigenere.

A cifra de Vigenère é um método de criptografia simples que usa uma série de diferentes cifras de César baseadas em letras de uma senha.

Exemplo:

	>>> import vigenere
	>>> msg = 'foo'
	>>> key = 'bar'
	>>> vigenere.cifra(msg, key)
	'gof'
	>>> vigenere.descifra('gof', key)
	'foo'

Command Line:

	$ python3 vigenere.py [c|d] <mensagem> <chave>