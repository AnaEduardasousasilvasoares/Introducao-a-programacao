import os
opcao=""
print("*****MENU*****")
print("1 soma")
print("2 subtracao")
print("3 multiplicacao")
print("4 divisao")
print("5 par ou impar")
print("6 primo")
print("7 fatorial")
print("digite para encerrar")
opcao=input("digite a opção desejado ou SAIR oara encerrar:")
opcaoMaiusc=opcao.upper()
while opcaoMaiusc!="SAIR":
    if opcao=="1":
        n1=int(input("digite o primeiro valor:"))
        n2=int(input("digite o segundo valor:"))
        print("o resultado da soma entre", n1,"e",n2,"é",n1+n2,".")
    if opcao=="2":
        n1=int(input("digite o primeiro valor:"))
        n2=int(input("digite o segundo valor:"))
        print("o resultado da subtração entre", n1,"e",n2,"é",n1-n2,".")
    if opcao=="3":
        n1=int(input("digite o primeiro valor:"))
        n2=int(input("digite o segundo valor:"))
        print("o resultado da multiplicação entre", n1,"e",n2,"é",n1*n2,".")   
    if opcao=="4":
        n1=int(input("digite o primeiro valor:"))
        n2=int(input("digite o segundo valor:"))
        print("o resultado da divisão entre", n1,"e",n2,"é",n1/n2,".")
        input("pressione ENTER para voltar ao MENU")
    if opcao=="5":
        n1=int(input("digite um numero para saber se ele é par ou impar"))
        if n1%2==0:
           print("o numero",n1,"é par!!")
        else:
           print("o numero",n1, "é impar!!")
    input("Pressione ENTER para continuar!")
    print("*****MENU*****")
    print("1 soma")
    print("2 subtracao")
    print("3 multiplicacao")
    print("4 divisao")
    print("5 par ou impar")
    print("6 primo")
    print("7 fatorial")
    print("digite para encerrar")
    opcao=input("digite a opção desejado ou SAIR oara encerrar:")
    opcaoMaiusc=opcao.upper()

