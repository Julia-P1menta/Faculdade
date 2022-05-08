"# Julia-P1menta" 

num=(int(input("Digite um valor em Decimal: ")))

#Conversor decimal para binario
def decimalToBinary(num):
    if (num > 0):
        decimalToBinary(num // 2)
    print(num % 2, end=' ')
if __name__ == '__main__':
    decimalToBinary(num)
    print(":Binario")


#Conversor decimal para Hexadecimal
def decimalToBinary(num):
    if (num > 0):
        decimalToBinary(num // 16)
    print(num % 16, end=' ')
if __name__ == '__main__':
    decimalToBinary(num)
    print(":Hexadecimal")


#Conversor decimal para Octadecimal
def decimalToBinary(num):
    if (num > 0):
        decimalToBinary(num // 8)
    print(num % 8, end=' ')
if __name__ == '__main__':
    decimalToBinary(num)
    print(":Ocatadecimal")
