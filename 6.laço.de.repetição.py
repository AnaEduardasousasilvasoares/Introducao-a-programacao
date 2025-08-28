maiormedia=0
menormedia=9999
alunorep=0
alunoap=0
for i in range(10):
    n1=float(input("digite a nota 1:"))
    n2=float(input("digite a nota 2:"))
    n3=float(input("digite a nota3:"))
    medaluno=(n1+n2+n3)/3
    if medaluno>maiormedia:
        maiormedia=medaluno
    if medaluno<menormedia:
        menormedia=medaluno
    if medaluno>=6:
        alunoap+=1
    else:
        alunorep+=1
print("a maior media é", maiormedia)
print("a menor media é",menormedia)
print("a quantidade de alunos reprovados é:", alunorep)
print("a quantidade de alunos aprovados é:", alunoap)