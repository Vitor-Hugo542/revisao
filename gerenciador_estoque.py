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

fruta = input("Dígite o nome da fruta desejada: ")

total = 0
if fruta in estoque:
        total += estoque[fruta]
        if total > 5:
            print("Estoque ok")
        elif total >= 1 and total <=5:
            print("Estoque abaixo, por favor REPOR!")
        else:
            print("Prduto ESGOTADO!!!")