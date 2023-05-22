import time

binario = ""
decimal = ""
octal = ""
decimalx = 0
binario1 = ""
binario2 = ""
main_option = 0

def binario_para_decimal(binario):
    decimal = 0
    potencia = 0
    for digito in reversed(binario):
        decimal += int(digito) * (2 ** potencia)
        potencia += 1
    return decimal

def octal_para_decimal(octal):
    decimal = 0
    potencia = 0
    for digito in reversed(octal):
        decimal += int(digito) * (8 ** potencia)
        potencia += 1
    return decimal

def decimal_para_binario(decimalx):
    if decimalx == 0:
        return '0'
    binario = ''
    while decimalx > 0:
        resto = decimalx % 2
        binario = str(resto) + binario
        decimalx = decimalx // 2
    return binario

def decimal_para_octal(decimalx):
    if decimalx == 0:
        return '0'
    octal = ''
    while decimalx > 0:
        resto = decimalx % 8
        octal = str(resto) + octal
        decimalx = decimalx // 8
    return octal

def soma_binaria(binario1, binario2):
    if len(binario1) < len(binario2):
        binario1, binario2 = binario2, binario1  # Garante que binario1 seja o maior

    binario2 = binario2.zfill(len(binario1))  # Preenche binario2 com zeros à esquerda

    resultado = ''
    carry = 0

    for i in range(len(binario1) - 1, -1, -1):
        bit1 = int(binario1[i])
        bit2 = int(binario2[i])

        soma = bit1 + bit2 + carry
        bit_soma = soma % 2
        carry = soma // 2

        resultado = str(bit_soma) + resultado

    if carry:
        resultado = '1' + resultado

    return resultado

def subtracao_binaria(binario1, binario2):
    if len(binario1) < len(binario2):
        binario1, binario2 = binario2, binario1  # Garante que binario1 seja o maior

    binario2 = binario2.zfill(len(binario1))  # Preenche binario2 com zeros à esquerda

    resultado = ''
    carry = 0

    for i in range(len(binario1) - 1, -1, -1):
        bit1 = int(binario1[i])
        bit2 = int(binario2[i])

        diferenca = bit1 - bit2 - carry
        if diferenca < 0:
            diferenca += 2
            carry = 1
        else:
            carry = 0

        resultado = str(diferenca) + resultado

    resultado = resultado.lstrip('0')  # Remove zeros à esquerda desnecessários

    if resultado == '':
        resultado = '0'

    return resultado

print("-" * 20)
print("  SISTEMA NUMÉRICO")
print("-" * 20)

while main_option != 4:
    main_option = int(input("\nESCOLHA A OPÇÃO QUE DESEJA \n\n[1] CONVERSÃO DE BINÁRIO E/OU OCTAL PARA DECIMAL \n[2] CONVERSÃO DE DECIMAL PARA BINÁRIO E/OU OCTAL \n[3] SOMA E SUBTRAÇÃO DE BINÁRIOS \n[4] SAIR DO PROGRAMA\n\n"))
    if main_option == 1:
        first_option = int(input("\n[1] BINÁRIO PARA DECIMAL \n[2] OCTAL PARA DECIMAL \n[3] VOLTAR AO MENU \n\n"))
        while first_option != 3:
            if first_option == 1:
                binario_para_decimal(binario)
                print("")
                binario = input("Digite um número binário: ")
                decimal = binario_para_decimal(binario)
                print("O binário", binario,"em decimal equivale a:", decimal)
                print("")
                time.sleep(2)
                first_option = int(input("[1] BINÁRIO PARA DECIMAL \n[2] OCTAL PARA DECIMAL \n[3] VOLTAR AO MENU \n\n"))
                # x_option = int(input("[1] REALIZAR MAIS UMA CONVERSÃO [2] VOLTAR AO MENU"))
                # if x_option == 1
            elif first_option == 2:
                octal_para_decimal(octal)
                print("")
                octal = input("Digite um número octal: ")
                decimal = octal_para_decimal(octal)
                print("O octal", octal,"em decimal equivale a:", decimal)
                print("")
                time.sleep(2)
                first_option = int(input("[1] BINÁRIO PARA DECIMAL \n[2] OCTAL PARA DECIMAL \n[3] VOLTAR AO MENU \n\n"))
    if main_option == 2:
        second_option = int(input("\n[1] DECIMAL PARA BINÁRIO/OCTAL \n[2] VOLTAR AO MENU \n\n"))
        while second_option != 2:
            decimal_para_binario(decimalx)
            decimal_para_octal(decimalx)
            print("")
            decimalx = int(input("Digite um número decimal: "))
            binario = decimal_para_binario(decimalx)
            octal = decimal_para_octal(decimalx)
            print("")
            print("O decimal", decimalx,"em binário equivale a:", binario)
            print("O decimal", decimalx,"em octal equivale a:", octal)
            print("")
            time.sleep(2)
            second_option = int(input("[1] DECIMAL PARA BINÁRIO/OCTAL \n[2] VOLTAR AO MENU \n\n"))
    if main_option == 3:
        third_option = int(input("\n[1] SOMA \n[2] SUBTRAÇÃO \n[3] VOLTAR AO MENU \n\n"))
        while third_option !=3:
            if third_option == 1:
                soma_binaria(binario1, binario2)
                binario1 = input("\nDigite o primeiro número binário: ")
                binario2 = input("Digite o segundo número binário: ")
                soma = soma_binaria(binario1, binario2)
                print("\nSoma = ", soma)
                time.sleep(2)
                third_option = int(input("\n[1] SOMA \n[2] SUBTRAÇÃO \n[3] VOLTAR AO MENU \n\n"))
            elif third_option == 2:
                subtracao_binaria(binario1, binario2)
                binario1 = input("\nDigite o primeiro número binário: ")
                binario2 = input("Digite o segundo número binário: ")
                subtracao = subtracao_binaria(binario1, binario2)
                print("\nSubtração = ", subtracao)
                time.sleep(2)
                third_option = int(input("\n[1] SOMA \n[2] SUBTRAÇÃO \n[3] VOLTAR AO MENU \n\n"))
else:
    print("\nSessão finalizada")
    time.sleep(2)