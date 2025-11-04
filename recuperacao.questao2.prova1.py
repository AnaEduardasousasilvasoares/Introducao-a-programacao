print("Ana Eduarda, Byank, emanuele, Guilherme.")
n=int(input("digite um numero decimal:"))
binario=""
n=n
if n==0:
    binario="0"
else:
    while n>0:
        resto=n%2
        binario=str(resto)+binario
        n=n//2
print("o numero em binario é:",binario)