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
def decimalToHexadecimal(num):
    hexalist = ['A', 'B', 'C', 'D', 'E', 'F']
    if num == 10:
        print(hexalist[0], end='')
    if num == 11:
        print(hexalist[1], end='')
    if num == 12:
        print(hexalist[2], end='')
    if num == 13:
        print(hexalist[3], end='')
    if num == 14:
        print(hexalist[4], end='')
    if num == 15:
        print(hexalist[5], end='')
    
if (num > 0):
    decimalToHexadecimal(num // 16)
    print(num % 16, end=' ')

if __name__ == '__main__':
    decimalToHexadecimal(num)
    print(":Hexadecimal")


#Conversor decimal para Octadecimal
def decimalToOctadecimal(num):
    if (num > 0):
        decimalToOctadecimal(num // 8)
    print(num % 8, end=' ')
if __name__ == '__main__':
    decimalToOctadecimal(num)
    print(":Octadecimal")
