# Nome: João Pedro Gonçalves Viana RGM 5934238212
# Nome: Pietro Danton Silveira RGM 5933512515
# Nome: Henry Dietri Yoshida RGM 5934114530
# Campus Paulista

import time

def binario_para_decimal(binario):
  if not binario.isdigit() or any(digito not in '01' for digito in binario):
    print("ERRO! DIGITE UM BINÁRIO VÁLIDO.")
    return None

  decimal = 0
  potencia = 0
  for digito in reversed(binario):
    decimal += int(digito) * (2**potencia)
    potencia += 1
  return decimal


def octal_para_decimal(octal):
  if not octal.isdigit() or any(digito not in '01234567' for digito in octal):
    print("ERRO! DIGITE UM OCTAL VÁLIDO.")
    return None

  decimal = 0
  potencia = 0
  for digito in reversed(octal):
    decimal += int(digito) * (8**potencia)
    potencia += 1
  return decimal


def decimal_para_binario(decimal):
  if not decimal.isdigit():
    print("ERRO! DIGITE UM DECIMAL VÁLIDO.")
    return None

  decimal = int(decimal)
  if decimal == 0:
    return '0'
  binario = ''
  while decimal > 0:
    resto = decimal % 2
    binario = str(resto) + binario
    decimal = decimal // 2
  return binario


def decimal_para_octal(decimal):
  if not decimal.isdigit():
    print("ERRO! DIGITE UM DECIMAL VÁLIDO.")
    return None

  decimal = int(decimal)
  if decimal == 0:
    return '0'
  octal = ''
  while decimal > 0:
    resto = decimal % 8
    octal = str(resto) + octal
    decimal = decimal // 8
  return octal


def soma_binaria(binario1, binario2):
  if not (binario1.isdigit() and binario2.isdigit()) or any(digito not in '01' for digito in binario1 + binario2):
    print("ERRO! DIGITE BINÁRIOS VÁLIDOS.")
    return None

  if len(binario1) < len(binario2):
    binario1, binario2 = binario2, binario1

  binario2 = binario2.zfill(len(binario1))
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
  if not (binario1.isdigit() and binario2.isdigit()) or any(digito not in '01' for digito in binario1 + binario2):
    print("ERRO! DIGITE BINÁRIOS VÁLIDOS.")
    return None

  if len(binario1) < len(binario2):
    binario1, binario2 = binario2, binario1

  binario2 = binario2.zfill(len(binario1))
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

  resultado = resultado.lstrip('0')

  if resultado == '':
    resultado = '0'

  return resultado


print("-" * 20)
print("  SISTEMA NUMÉRICO")
print("-" * 20)

main_option = 0

while main_option != 4:
  try:
    main_option = int(input("\nESCOLHA A OPÇÃO QUE DESEJA \n\n[1] CONVERSÃO DE BINÁRIO E/OU OCTAL PARA DECIMAL \n[2] CONVERSÃO DE DECIMAL PARA BINÁRIO E/OU OCTAL \n[3] SOMA E SUBTRAÇÃO DE BINÁRIOS \n[4] SAIR DO PROGRAMA\n\n"))
    
    if main_option not in [1,2,3,4]:
      raise ValueError

    if main_option == 1:
        while True:
            try:
                first_option = int(input("\n[1] BINÁRIO PARA DECIMAL \n[2] OCTAL PARA DECIMAL \n[3] VOLTAR AO MENU \n\n"))
                if first_option == 1:
                    binario = input("Digite um número binário: ")
                    decimal = binario_para_decimal(binario)
                    if decimal is not None: #para não aparecer resultado = none
                        print("O binário", binario, "em decimal equivale a:", decimal)
                        time.sleep(2)
                elif first_option == 2:
                    octal = input("Digite um número octal: ")
                    decimal = octal_para_decimal(octal)
                    if decimal is not None:
                        print("O octal", octal, "em decimal equivale a:", decimal)
                        time.sleep(2)
                elif first_option == 3:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("\nDIGITE UMA OPÇÃO VÁLIDA!")

    elif main_option == 2:
      while True:
        try:
          second_option = int(input("\n[1] DECIMAL PARA BINÁRIO/OCTAL \n[2] VOLTAR AO MENU \n\n"))

          if second_option == 1:
            decimalx = input("Digite um número decimal: ")
            binario = decimal_para_binario(decimalx)
            octal = decimal_para_octal(decimalx)
            if binario is not None:
              print("O decimal", decimalx, "em binário equivale a:", binario)
            if octal is not None:
              print("O decimal", decimalx, "em octal equivale a:", octal)
            time.sleep(2)
            second_option = int(input("[1] DECIMAL PARA BINÁRIO/OCTAL \n[2] VOLTAR AO MENU \n\n"))
          elif second_option == 2:
            break
          else:
            raise ValueError
        except ValueError:
          print("\nDIGITE UMA OPÇÃO VÁLIDA!")

    elif main_option == 3:
      while True:
        try:
          third_option = int(input("\n[1] SOMA \n[2] SUBTRAÇÃO \n[3] VOLTAR AO MENU \n\n"))

          if third_option == 1:
            binario1 = input("Digite o primeiro número binário: ")
            binario2 = input("Digite o segundo número binário: ")
            soma = soma_binaria(binario1, binario2)
            if soma is not None:
              print("Soma =", soma)
              time.sleep(2)
            third_option = int(input("\n[1] SOMA \n[2] SUBTRAÇÃO \n[3] VOLTAR AO MENU \n\n"))
          elif third_option == 2:
            binario1 = input("Digite o primeiro número binário: ")
            binario2 = input("Digite o segundo número binário: ")
            subtracao = subtracao_binaria(binario1, binario2)
            if subtracao is not None:
              print("Subtração =", subtracao)
              time.sleep(2)
            third_option = int(input("\n[1] SOMA \n[2] SUBTRAÇÃO \n[3] VOLTAR AO MENU \n\n"))
          elif third_option == 3:
            break
          else:
            raise ValueError
        except ValueError:
          print("\nDIGITE UMA OPÇÃO VÁLIDA!")
            

  except ValueError:
    print("\nDIGITE UMA OPÇÃO VÁLIDA!")

print("\nSessão finalizada")
time.sleep(2)
