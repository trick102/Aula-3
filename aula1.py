# Operadores Aritmeticos
# Entrada de dados
# Estrutura de decisao e logica condicional

# Entrada e Escrita

# nome = input ("Digite seu nome: ")
# profissao = input ("Digite sua profissao ")
# salario = input ("Digite seu Salario ")

# print("0 nome é: ", nome, "\nA A sua profissao é: ", profissao, "\n O seu salario é: ", salario)

#  Fazer um progama que ira perguntar o nome do usuario
# a profissao e quanto ele recebe e mostrar para ele os dados digitados
# Operadores aritmeticos
soma = 1 + 2
multiplicacao = 2 * 2
subtracao = 2 - 2
divisao = 2 / 2

# int é para numeros inteiros
# = numeros que nao possuem casas decimais
# float é para numeros decimais
# float aceita numeros quebrados

# cast
# valor1 = int(input("Digite o valor 1: "))
# valor2 = int(input("Digite o valor 2: "))

# soma = valor1 + valor2
# multiplicacao = valor1 * valor2 
# subtracao = valor1 - valor2
# divisao = valor1 / valor2

# print("A soma dos valores é de: ", soma)

# #cast para float
# valor1 = float (input("Digite o valor 1: "))

# soma = 1.5 + valor1

# print ("soma é de: ", soma)

# Faça uma calculadora que peça para o usuario o peso e kg
# e a altura em metros e calcule o imc
# a formula do IMC é peso dividido pela altura ao quadrado

# peso = float(input("Digite seu peso"))
# altura = float (input("Digite sua altura em metros"))

# imc = peso / (altura * altura) 

# print ("o IMC é de: ", imc)

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - (4 * a * c) 

x1 = (-b + (delta**0.5)) / 2 * a

x2 = (-b - (delta**0.5)) /2 * a

print ("x1 =", x1, "x2 = ", x2)