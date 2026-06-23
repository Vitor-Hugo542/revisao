estoque ={
    "maçã": 1,
    "banana": 3,
    "uva": 8,
    "maracuja": 6,
    "morango": 13,
    "melancia": 0,
    "melão": 15,
    "laranja": 12,
    "jabuticaba": 3
}

compra = input("Dígite o nome da fruta desejada: ")

total = 0
for compra in estoque:
    total += estoque[compra]


if total > 5:
    print("Estoque ok")
elif total >= 1 or total <5:
    print("Estoque abaixo, por favor REPOR!")
else:
    print()