# Banco do Futuro

Sistema bancário desenvolvido em **Python** para praticar conceitos fundamentais de programação e armazenamento de dados.

## 📖 Sobre o projeto

O **Banco do Futuro** é um sistema bancário executado pelo terminal, permitindo que o usuário crie e acesse uma conta e realize operações bancárias básicas.

Os dados das contas são armazenados em um arquivo **JSON**, permitindo que as informações permaneçam salvas mesmo após o encerramento do programa.

## ⚙️ Funcionalidades

-  Criar conta
-  Acessar conta com CPF e senha
-  Consultar saldo
-  Realizar depósitos
-  Realizar saques
-  Validar CPF
-  Impedir cadastro de CPF duplicado
-  Validar valores inseridos
-  Salvar dados automaticamente em JSON
-  Encerrar o sistema

## Menu principal

```text
Bem vindo ao Banco do Futuro!

1- Abrir conta
2- Acessar conta
3- Sair

Escolha uma opção:

Após acessar uma conta:

1- Consultar saldo
2- Depositar
3- Sacar
4- Voltar

Tecnologias
 Python 3
 JSON
 Visual Studio Code
 GitHub
 Conceitos praticados

Este projeto foi desenvolvido para colocar em prática conceitos fundamentais de Python, como:

Variáveis
input() e print()
Estruturas condicionais
Estruturas de repetição
Dicionários
Funções
Manipulação de arquivos
Leitura e escrita de JSON
try e except
Validação de dados
F-strings
Operações matemáticas
Persistência de dados

 Estrutura do projeto
Banco-do-Futuro/
│
├── main.py
├── dados.json
└── README.md
main.py

Arquivo principal responsável pelo funcionamento do sistema bancário.

dados.json

Arquivo utilizado para armazenar os dados das contas cadastradas.

Exemplo:

{
    "12345678901": {
        "nome": "João",
        "senha": "1234",
        "saldo": 500
    }
}

 Como executar
1. Clone o repositório
git clone https://github.com/SEU-USUARIO/Banco-do-Futuro.git
2. Acesse a pasta
cd Banco-do-Futuro
3. Execute o programa
python main.py

 Funcionamento

O programa inicia apresentando um menu com três opções:

1. Abrir conta

O usuário informa seu nome, CPF e senha. O sistema verifica se o CPF possui 11 dígitos, se contém apenas números e se ainda não está cadastrado.

2. Acessar conta

O usuário informa seu CPF e senha. Caso os dados estejam corretos, o sistema libera o acesso às operações da conta.

3. Sair

Encerra o programa.

Após o login, o usuário pode consultar seu saldo, realizar depósitos, realizar saques ou voltar ao menu principal.


 Persistência de dados

O projeto utiliza o módulo json do Python para armazenar as informações das contas.

Os dados são carregados ao iniciar o programa:

with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

E atualizados sempre que uma alteração é realizada:

with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, indent=4)

Dessa forma, as contas continuam armazenadas mesmo depois que o programa é fechado.

 Objetivo do projeto

Este projeto foi desenvolvido como parte do meu processo de aprendizado em Python.

O principal objetivo foi transformar conhecimentos básicos de programação em uma aplicação prática, trabalhando com entrada de dados, validações, estruturas de repetição, dicionários e persistência de informações.

  Próximas melhorias
 Organizar o código utilizando funções
 Separar o projeto em módulos
 Adicionar histórico de transações
 Criar extrato bancário
 Adicionar transferência entre contas
 Melhorar a validação de CPF
 Implementar criptografia de senhas
 Criar testes automatizados
 Melhorar o tratamento de erros
 Criar uma interface gráfica

 Aviso

Este projeto possui finalidade educacional e não deve ser utilizado para operações bancárias reais.

As informações são armazenadas localmente e as senhas não possuem criptografia.


  Autor

Cesar Augusto

Estudante de Análise e Desenvolvimento de Sistemas.

Atualmente desenvolvendo projetos em Python para aprimorar meus conhecimentos em programação e construir meu portfólio.

⭐ Obrigado por visitar o projeto!
