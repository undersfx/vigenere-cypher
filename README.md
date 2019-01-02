# Vigenere Cypher

Exercício: 
Cifra e descifra utilizando o método de Vigenere.

Como funciona:
A cifra de Vigenère é um método de criptografia simples que usa uma série de diferentes cifras de César baseadas em letras de uma senha.

Exemplo de uso:

	>>> import vigenere
	>>> msg = 'foo'
	>>> key = 'bar'
	>>> vigenere.cifra(msg, key)
	'gof'
	>>> vigenere.descifra('gof', key)
	'foo'

Ou:

	$ python3 vigenere.py [c|d] <mensagem> <chave>
