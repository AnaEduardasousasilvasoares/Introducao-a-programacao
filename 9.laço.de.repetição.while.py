n=int(input("digite um numero:"))
cont=0
i=1
while i<=n:
    if n%i==0:
        cont+=1
    i+=1
if cont==2:
    print("o numero",n,"é primo")
else:
    print("o numero",n,"não é primo")
 