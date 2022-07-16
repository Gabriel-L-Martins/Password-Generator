#Importando bibliotecas e inicializando variáveis globais  |  Importing libraries and initializing global variables
import string
import random
min_lenght = int()
max_lenght = int()

def main():
  #Obtendo e armazenando o menor cumprimento da senha possível  |  Getting and storing the shortest possible password length
  def min_lenght():
    try:
      ###Usando variáveis globais  |  Using global variables
      global min_length

      min_length = int(input('Menor quantidade de caracteres (recomendado: 8): '))  ###Alterando a variável "min_length" para um valor recebido por um input  |  Changing the "min_length" variable to a value received by an input
    ##Lidando com erros de digitação  |  Dealing with typos
    except:
      print('   DIGITE UM VALOR VÁLIDO!')
      min_lenght()
  #Obtendo e armazenando o maior cumprimento da senha possível  |  Getting and storing the longest possible password length
  def max_lenght():
    try:
      ###Usando variáveis globais  |  Using global variables
      global max_length

      max_length = int(input('Maior quantidade de caracteres (recomendado: 14): '))  ###Alterando a variável "max_length" para um valor recebido por um input  |  Changing the "max_length" variable to a value received by an input
    ##Lidando com erros de digitação  |  Dealing with typos
    except:
      print('   DIGITE UM VALOR VÁLIDO!')
      max_lenght()

  #Inicializando funções do cumprimento da senha  |  Initializing password length functions
  min_lenght()
  max_lenght()

  #Tenta gerar a senha  |  Try to generate the password
  try:
    #Obtendo a senha
    for x in range(1):
      ##Usando variáveis globais  |  Using global variables
      global min_length
      global max_length

      length_of_string = random.randint(min_length,max_length)  ##Obtendo o cumprimento da senha  |  Getting password length
      print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))  ##Resultado após todos os processos  |  Result after all processes
  #Executa o programa novamente se o valor de "max_length" for menor que "min_length"  |  Run the program again if the value of "max_length" is less than "min_length"
  except:
    print("O segundo valor deve ser maior que o primeiro!")
    main()

main()