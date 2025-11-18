bateria=int(input("nível de bateria:"))
temperatura=int(input("digite a temperatura:"))
umidade=int(input("digite a umidade:"))
modo=input("digite o modo da operação (plantio,colheita,irrigacão):").upper()

if bateria <20:
    print("bateria muito baixa!, retorne para a base.")
if bateria>=20:
     if bateria<50:
        print("bateria em nível médio, fique atento!")
if bateria>=50:
           print("bateria o sufiente para a operação.")


if temperatura>40:
      print("temperatura critica, retorne para a base.")
if temperatura <5:
      print("frio extremo, modo economia ativado.")
if umidade<30: 
      print("solo muito seco. recomendo iniciar a irrigação.")
if umidade>80:
      print("solo encharcado, Suspenda a irrigação.")


if modo=="plantio":
      print("modo plantio iniciado.")
if modo=="colheita":
        print("modo colheita iniciado.")
if modo=="irrigacão":
          print("modo irrigação iniciado.") 


ok1=0
ok2=0
ok3=0

if bateria >=50:
    ok1=1
if temperatura>=10:
      if temperatura<=35:
            ok2=1
if umidade>=30:
      if umidade<=80:
            ok3=1
if ok1==1:
      if ok2==1:
            if ok3==1:
                  print("robô atorizado para operação.")
                  
if ok1!=1:
      print("operação negada, bateria insuficiente.")
if ok2!=1:
      print("operação negada, temperatura fora do limite.")
if ok3!=1:
      print("operação negada, umidade fora do limite.")            