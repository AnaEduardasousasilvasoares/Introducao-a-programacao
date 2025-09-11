jogadores=int(input("digite o numero de jogadores de volei:"))
soma_altura=0
i=0
while i< jogadores:
   if i< jogadores: 
    altura=float(input("digite a altura dos jogadadores:"))
   soma_altura=altura
   i+=1
mediaaltura= (soma_altura)/ jogadores 
print("a media de altura dos jogadores:", soma_altura/jogadores)