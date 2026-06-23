dicionario_precos ={
    "maçã": 1,
    "banana": 3,
    "uva": 8,
    "maracuja": 6,
    "morango": 13,
    "melancia": 30,
    "melão": 15,
    "arroz": 18,
    "feijão": 5,
    "milho": 2,
    "carne moída 1ª": 42,
    "costela minga": 36,
    "paleta suína": 12,
    "kit feijoada": 50
}

carrinho = []
print("Produtos disponíveis:", list(dicionario_precos.keys()))

compra = input("Dígite o que deseja comprar ou dígite 'sair' para sair:").strip()

total = 0.00
while True:
    if compra.lower() == 'sair':
        break
    if compra.lower() in dicionario_precos:
        carrinho.append(compra)
    compra = input(f"{compra} foi adicionado, deseja comprar algo mais? ou dígite 'sair' para sair:").strip()


for itens in carrinho:
    total += dicionario_precos[itens]
    if total > 100:
        total = total - total*0.1    
print (f" O total da compra é: R${total}")  