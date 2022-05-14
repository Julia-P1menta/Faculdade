#Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o 
#mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que 
#pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final 
#da digitação de dados deve ocorrer quando o usuário digitar 0 (zero) no campo código. 
#Ao encerrar o programa deve ser informados os códigos e os valores do cliente mais 
#alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos 
#pesos dos clientes.

cod_gordo = 0
cod_magro = 0
cod_alto = 0
cod_baixo = 0
peso_gordo = 0
peso_magro = 1000
altura_alto = 0
altura_baixo = 500
soma_peso = 0
soma_altura = 0
qtd_cliente = 0

while True:
    codigo = input("Digite o codigo do cliente: ")
    if codigo == "0":
        break

    qtd_cliente += 1
    altura = int(input("Digite a altura do cliente (em centímetros): "))
    peso = float(input("Digite o peso do cliente (em kg): "))

    soma_peso += peso
    soma_altura += altura

    if altura > altura_alto:
        altura_alto = altura
        cod_alto = codigo

    if altura < altura_baixo:
        altura_baixo = altura
        cod_baixo = codigo

    if peso > peso_gordo:
        peso_gordo = peso
        cod_gordo = codigo

    if peso < peso_magro:
        peso_magro = peso
        cod_magro = codigo

media_altura = soma_altura / qtd_cliente
media_peso = soma_peso / qtd_cliente

print(
    "O cliente mais alto é o que tem o código",cod_alto,
    " e ele possui",altura_alto,"cm de altura\n",
    "O cliente mais baixo é o que tem o código\n",cod_baixo,
    " e ele possui",altura_baixo,"cm de altura\n"
    "O cliente mais gordo é o que tem o código",cod_gordo,
    " e ele pesa",peso_gordo,"kg\n"
    "O cliente mais magro é o que tem o código",cod_magro,
    " e ele pesa",peso_magro,"kg\n"
    "A média de altura dos clientes é de",media_altura,"cm\n"
    "A média de peso dos clientes é de",media_peso,"kg")
