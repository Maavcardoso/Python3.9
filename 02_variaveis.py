# str (string): Stores alphabets, words or other characters. Ou qualquer valor entre aspas Ex: hello, a, ç, ^, '1',''
# int (integer): Stores whole numbers; Ex: 1,2,3... -1 ... 0
# float: Stores fractional numbers. Ex: 7.5, -15.253, 1.0, 2.0...
# bool (boolean): Stores True (1) or False (0) values.

n1 = input ('Digite um número: ')
print (type(n1))

n2 = int(input ('Digite um número: '))
print (type(n2))

# Ao rodar esse código, podemos observar que n1, por mais que seja
# digitado um número, é considerado uma string. Para ser considerado int,
# fui obrigado a inserir a tipagem antes do método input de n2.

n3 = bool(input('Digite um número: '))
print (n3)

# Neste código, lê-se um valor booleano, portanto, ele só pode retornar true ou false.
# Sendo que: n3 == NULL retorna False e N3 != NULL retorna True. NULL: Sem valor, vazio. 

n4 = input('digite algo: ')
print(n4.isnumeric())

# Neste código, o método isnumeric() analisa a string e retorna um valor booleano.
# essa função analisa o conteúdo da string e os diferencia, mesmo sendo números ou outros caracteres.
# ele verifica se é possível transformar os valores na string em um tipo primitivo, nesse caso, Int. 


