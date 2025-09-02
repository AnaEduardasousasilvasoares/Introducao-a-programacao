thanos=150
aranha=110
anos=0
print("antes:aranha=",aranha,"thanos=",thanos)
if aranha>thanos:
    anos=0
else:
    anos=(thanos-aranha)//(3-2)+1
    aranha+=anos*3
    thanos+=anos*2
print("depois:aranha=",aranha,"thanos=",thanos)
print(anos,"é a quantidade de anos que demorou para a aranha ultrapassar o thanos")  
print(aranha, "é a altura da aranha")
print(thanos,"é a altura do thanos")