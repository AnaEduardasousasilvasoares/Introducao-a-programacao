total = 0
quantidade = 0
mais_caro = 0

continuar = "s"

while continuar == "s":

    preco = -1
    while preco < 0:
        preco = float(input("Preço do produto: "))
        if preco < 0:
            print("Preço inválido!")

    total = total + preco
    quantidade = quantidade + 1

    if preco > mais_caro:
        mais_caro = preco

    continuar = ""
    while continuar != "s":
        if continuar == "n":
            break
        continuar = input("Deseja adicionar outro produto? (s/n): ")


print("Total:", total)
print("Quantidade:", quantidade)
print("Média:", total / quantidade)
print("Mais caro:", mais_caro)