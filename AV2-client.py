#Nome: Lucas Silva de Oliveira Ra: 0050018893
import requests
import json

api = "http://127.0.0.1:8080/lista_paises"

dados = requests.get(api).json()
ocr = []
result=[]
#print(json.dumps(dados, indent=4))
# print(dados)
venda_id=[]
painel = []
count = 0
for a in dados:
    painel.append(f"{count}.{a['Country']}")
    print(f"{count}.{a['Country']}")
    count += 1
op = input('Digite a opção desejada: ')

for a2 in painel:
    if a2.split('.')[0] == op:
        pais = a2.split('.')[1]
        break
print(f'O País selecionado foi: {pais}, Calculando...')

api2 = "http://127.0.0.1:8080/lista_vendas/"+str(pais)
dados2 = requests.get(api2).json()
for a3 in dados2:
    venda_id.append(a3['InvoiceId'])
    

for a4 in venda_id:
    api3 = "http://127.0.0.1:8080/lista_itemvenda/"+str(a4)
    dados3 = requests.get(api3).json()
    for a5 in dados3:
        api4 = "http://127.0.0.1:8080/get_genero/"+str(a5['TrackId'])
        dados4 = requests.get(api4).json()
        for a6 in dados4:
            result.append(a6['Name'])
            if a6['Name'] not in ocr:
                ocr.append(a6['Name'])
            if a6 in ocr:
                continue
maior = 0
for a7 in ocr:
    if result.count(a7) > maior:
        maior= result.count(a7)
        genero = a7
        

print(f'O genero que vendeu mais faixas no pais: {pais}, foi: {genero} com um total de {maior} vendas!!')
    
  