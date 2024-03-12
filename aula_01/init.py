# Revisão da aula 01 do Curso de Formação em Análise de Dados em Python.
print('Hello, World!')

nome=input('Qual seu nome? ')
print(nome)
# O método input() recebe uma entrada do usuário e armazena na variável nome. O valor armazenado é do tipo texto (string).
# Caso seja seja inserido um valor numérico, o mesmo será convertido para texto.
# Como solução é possível converter o tipo de dado antes de ser armazenado na variável.
valor1=int(input('Qual o primeiro valor? '))
valor2=int(input('Qual o segundo valor? '))
print('A soma dos valores e: ', valor1+valor2)


# ou converter depois de ser armazenado na variável
valor1=(input('Qual o primeiro valor? '))
valor2=(input('Qual o segundo valor? '))
print('A soma dos valores e: ', int(valor1)+int(valor2))
