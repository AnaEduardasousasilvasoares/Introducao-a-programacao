atletas=0 
altura=0
peso=0
nome=input("digite os nomes dos jogadores (ou @ para sair):")
while(nome!="@"):
    atletas+=1
    altura+=1
    peso+=1
    sexo=input("digite o sexo dos atletas (M/F):")
    idade=int(input("digite a idade dos atletas:"))
    peso=float(input("digite o peso dos atletas:"))
    altura=float(input("digite a altura dos atletas:"))
    masc_maior_peso=0
    fem_maior_altura=0
    soma_idade=0
    media_idade=idade/atletas
    if  sexo=="M/m":
        if peso>masc_maior_peso:
            masc_maior_peso=peso
    if  sexo=="F/f":
        fem_maior_altura=altura>fem_maior_altura
        soma_idade+=idade
        media_idade=soma_idade/atletas
    nome=input("digite os nomes dos jogadores (ou @ para sair):")
print("o atleta do sexo masculino com maior peso é:", masc_maior_peso)
print("a atleta do sexo feminino com maior altura é:",fem_maior_altura)
print("a média de idade dos atletas é:",media_idade)
    