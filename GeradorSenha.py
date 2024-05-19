import random
#misturar letras(minusculas e maiúsculas)
minusculo = list('abcdefghijklmnopqrstuvwxyz')
maiusculo = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('1234567890')
simbols = list('!@#$%&*+=?')
lista = [1, 2, 3, 4]
senha = []
sim = []
condicao = True
def letras_minusculas():
    senha.append(random.choice(minusculo))
def letras_maiusculas():
    senha.append(random.choice(maiusculo))
def simbolos():
    senha.append(random.choice(simbols))
def numeros():
    senha.append(random.choice(numbers))
def verificador():
    for i, id in enumerate(senha):
        if id in maiusculo:
            sim.append(1)
        if id in minusculo:
            sim.append(2)
        if id in numbers:
            sim.append(3)
        if id in simbols:
            sim.append(4)
    if (1 and 2 and 3 and 4) in lista:
        pass
    else:
        condicao = False

#gerar senha
def gerar_senha():
    for i in range (opcao):
        a = random.choice(lista)
        if a == 1:
            letras_minusculas()
        elif a == 2:
            letras_maiusculas()
        elif a == 3 :
            numeros()
        elif a == 4:
            simbolos()
        #verificar se há pelo menos um digito de cada possibilidade
    verificador()
#quantos dígitos forem pedidos

while True:
    opcao = int(input('QUANTOS DIGITOS TERÁ A SUA SENHA SEGURA (MIN 6): '))
    if opcao < 6:
        opcao = 6
    gerar_senha()
    if condicao == True:
        normal = (''.join(senha))
        print(f'Sua senha foi gerada!!\nSua senha é: {normal}')
        passador = input('Deseja gerar mais uma senha? (y/n)\n')
        if passador == 'y':
            senha.clear()  
            sim.clear()
        elif passador == 'n':
            break
    elif condicao == False:
        senha.clear()
        sim.clear()

    

