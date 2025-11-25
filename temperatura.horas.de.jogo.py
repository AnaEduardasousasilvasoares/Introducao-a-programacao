quantidade = int(input("Quantas temperaturas? "))

soma = 0
acima_30 = 0
abaixo_15 = 0

for i in range(quantidade):
    temperatura = float(input("Temperatura: "))

    if i == 0:              
        maior = temperatura
        menor = temperatura
    else:                    
        if temperatura > maior:
            maior = temperatura
        if temperatura < menor:
            menor = temperatura

    soma = soma + temperatura

    if temperatura > 30:
        acima_30 = acima_30 + 1
    if temperatura < 15:
        abaixo_15 = abaixo_15 + 1

media = soma / quantidade

print("Maior temperatura:", maior)
print("Menor temperatura:", menor)
print("Média:", media)
print("Acima de 30°C:", acima_30)
print("Abaixo de 15°C:", abaixo_15)

if maior - menor > 20:
    print("ALERTA: Variação térmica extrema!")
else:
    print("Variação dentro do esperado.")
    
    
    horas = int(input("Horas por semana: "))
gasto = int(input("Gasto mensal: "))
jogos = int(input("Jogos instalados: "))

perfil = "não classificado"


if horas >= 30:
    if gasto >= 100:
        if jogos >= 20:
            perfil = "HARDCORE"


if perfil == "não classificado":
    if horas >= 10:
        if horas <= 29:
            if gasto >= 30:
                if gasto <= 99:
                    if jogos >= 10:
                        if jogos <= 19:
                            perfil = "INTERMEDIÁRIO"

if perfil == "não classificado":
    if horas < 10:
        perfil = "CASUAL"
    else:
        if gasto < 30:
            perfil = "CASUAL"
        else:
            if jogos < 10:
                perfil = "CASUAL"

print("Classificação:", perfil)