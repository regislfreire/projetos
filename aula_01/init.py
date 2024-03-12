import time

print("Olá", end="aaaaa ")
print("mundo!")

# Revisão da aula 01 do Curso de Formação em Análise de Dados em Python.
time.sleep(2)
print('\n' * 100)
print('Hello, World!')
time.sleep(2)
print('\n' * 100)
print('Vamos fazer uma revisão de Python?')
time.sleep(2)
print('\n' * 100)
print("Estamos usando a função 'print()' para exibir conteúdo na tela.")
time.sleep(2)
print('\n' * 100)
print('Agora vamos armazenar o seu nome na variável nome.')
time.sleep(2)
print('\n' * 100)
nome=input('Qual o seu nome? ')
print('\n' * 100)
print(f'Pronto, {nome}. Agora já temos seu nome armazenado')
nomenew=type(nome)
time.sleep(2)
print('\n' * 100)
print('o tipo de dado da variável nome é: ', nomenew)
time.sleep(2)
print('\n' * 100)
type(nome)
# O método input() recebe uma entrada do usuário e armazena na variável nome. O valor armazenado é do tipo texto (string).
# Caso seja seja inserido um valor numérico, o mesmo será convertido para texto.
# Como solução é possível converter o tipo de dado antes de ser armazenado na variável.
#valor1=int(input('Qual o primeiro valor? '))
#valor2=int(input('Qual o segundo valor? '))
#print('A soma dos valores e: ', valor1+valor2)


# ou converter depois de ser armazenado na variável
#valor1=(input('Qual o primeiro valor? '))
#valor2=(input('Qual o segundo valor? '))
#print('A soma dos valores e: ', int(valor1)+int(valor2))
#nome="maria"
#idade="10"
#print("Olá, meu nome é", nome, "e eu tenho", idade, "anos")
#print(nome+idade)
