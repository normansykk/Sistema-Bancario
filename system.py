
import json

with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

while_loop = True
while while_loop:
 print("Bem vindo ao Banco do Futuro!")
 print("1- Abrir conta")
 print("2- Acessar conta")
 print("3- Sair") 
 escolha = input("Escolha uma opção: ")
 if escolha == "1":
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    while len(cpf) != 11 or not cpf.isdigit():
        print("CPF inválido. Tente novamente.")
        cpf = input("Digite seu CPF: ")
    while cpf in dados:
            print("CPF já cadastrado. Tente novamente.")
            cpf = input("Digite seu CPF: ")        
    senha = input("Digite sua senha: ")
    dados[cpf] = {"nome": nome, "senha": senha, "saldo": 0}
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print("Conta criada com sucesso!")
 elif escolha == "2":
    cpf = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")
    if cpf in dados and dados[cpf]["senha"] == senha:
        print(f"Bem vindo, {dados[cpf]['nome']}!")
        while True:
            print("1- Consultar saldo")
            print("2- Depositar")
            print("3- Sacar")
            print("4- voltar")
            escolha_conta = input("Escolha uma opção: ")
            if escolha_conta == "1":
                print(f"Seu saldo é: R${dados[cpf]['saldo']:.2f}")
            elif escolha_conta == "2":
             while True:    
                try:
                 valor = float(input("Digite o valor a ser depositado: "))
                 break
                except:
                 print("apenas números são aceitos")
             if valor > 0:   
                 dados[cpf]["saldo"] += valor
                 with open("dados.json", "w") as arquivo:
                    json.dump(dados, arquivo, indent=4)
                 print(f"Depósito de R${valor:.2f} realizado com sucesso!")
             else:
                 print("o valor deve ser maior que 0")
            elif escolha_conta == "3":
             while True:
                try:
                 valor = float(input("Digite o valor a ser sacado: "))
                 break
                except:
                    print("apenas números são aceitos")
                    
             if valor > 0 and valor <= dados[cpf]["saldo"]:
                    dados[cpf]["saldo"] -= valor
                    with open("dados.json", "w") as arquivo:
                        json.dump(dados, arquivo, indent=4)
                    print(f"Saque de R${valor:.2f} realizado com sucesso!")
             elif valor <0:
                print("o valor deve ser maior que 0")
             else:
                    print("Saldo insuficiente!")
            elif escolha_conta == "4":
             break
    elif cpf not in dados:
        print("CPF não cadastrado.")
    elif dados[cpf]["senha"] != senha:
        print("Senha incorreta.")    
 elif escolha == "3":
    while_loop = False
    print("Saindo do sistema...")