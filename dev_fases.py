""" 
variável que recebe entrada via input e imprime o nome da tela
"""
nome =input("Digite seu nome: ")
print("Olá,", nome)

# Fase 2 - Lista e laço while
# Agora guardamos vários nomes
nomes = []

# While cria um laço infinito de repetição - só para com "break"

while True:
    nome = input("Dígite um nome (ou 'sair' para terminar): ")
    if nome == 'sair':
        break
    
    nomes.append(nome)

for n in nomes:
    print(n)

# Fase 3 - Busca de nomes
busca = input("Buscar nome: ")

# 'in' verifica se o valor existe dentro da lista
if busca in nomes: 
    print(f"Nome '{busca}' encontrado!")
else:
    print(f"Nome '{busca}' não encontrado!")

# 'for' é usado para percorrer toda lista (Banco de Dados)

for  i, n in enumerate(nomes, 1):
    print(f"{i}. {n}")

# Fase 4 - Salvar e carregar do arquivo de texto
with open("nomes.txt", "w", encoding="utf-8") as arquivo:
    for nome in nomes:
        arquivo.write(nome + "\n")
print("Nomes salvos com sucesso!")

# Exibir os nomes do arquivo nomes.txt
with open ("nomes.txt", "r", encoding="utf-8") as arquivo:
    nomes_carregados = arquivo.read().splitlines

print("Nomes carregados: ", nomes_carregados)

# Fase 5: Tratamento de erros
try:
    with open("nomes.txt", "r", encoding="utf-8") as f:
        nomes =f.read().splitlines  
except FileNotFoundError:
    # arquivo não existe ainda - começa a lista vazia
    print("Arquivo não encontrado. Iniciando vazio.")
    nomes = []

# Validação: nome não poder ser vazio ou só com espaços
def validar_nome(nome):
    if not nome.strip():
        raise ValueError("Nome não pode ser vázio!")
    return nome.strip

try:
    nome = validar_nome(input("Nome: "))
    nomes.append(nome)
except ValueError as e:
    print(f"Erro: {e}")

# Fase 6 - Organização com funções
# Cada função faz UMA coisa - princípio básico

# Cada função tem o nome que descreve o que ela faz

ARQUIVO = "nomes.txt"

def carregar_nomes():
    try:
        with open(ARQUIVO, "f", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return[]

def salvar_nomes(nomes):
    with open(ARQUIVO, "r", encording="utf-8") as f:
        for name in nomes:
            f.write(nome + "\n")

def adicionar_nome(nomes, nome):
    if not nome.strip():
        raise ValueError ("Nome vazio")
    nomes.append(nome.strip())

def buscar_nomes(nomes, busca):
    return busca in nomes

def listar_nomes(nomes):
    for i, n in enumerate(nomes, 1):
        print(f"{i}. {n}")

nomes = carregar_nomes()

# Fase 7 - Criação de menu com todas as funções

def menu ():
    print("\n --- Cadastro de Nomes --- ")
    print("1. Adicionar nome")
    print("2. Listar nomes")
    print("3. Buscar nome")
    print("4. Salvar e sair")
    return input("Opção: ")

if __name__ == "__main__":
    nomes = carregar_nomes()

    while True: 
        opcao = menu()
        if opcao == "1":
            try:
                adicionar_nome(nomes, input("Nome: "))
                print("Adicionado!")
            except ValueError as e:
                print(f"Error: {e}")
        elif opcao == "2":
            listar_nomes(nomes)

        elif opcao == "3":
            busca = input("Buscar: ")
            achou = buscar_nomes(nomes, busca)
            print("Encontrada!" if achou else "Não encontrado")
        
        elif opcao == "4":
            salvar_nomes(nomes)
            print("Salvo, até logo!")
            break