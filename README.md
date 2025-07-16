💳 Banco Fronteira Norte
Este é um sistema simples de gestão bancária feito em Python, com funcionalidades como criação de contas, transferências, saques, depósitos, pagamento de boletos, câmbio de moedas e empréstimos.

📌 Funcionalidades
Criação e login de contas

Consulta de saldo (BRL e USD)

Saques e depósitos

Histórico de transações

Transferência entre contas

Troca de conta logada

Pagamento de boletos (com aviso de vencidos)

Conversão de moedas (BRL ⇄ USD)

Empréstimos com geração automática de boletos

🗂️ Estrutura do Projeto
bash
Copiar
Editar
bank-management/
│
├── main.py              # Arquivo principal com o menu e a lógica geral
├── conta.py             # Classe Conta com métodos de movimentação e saldo
├── boletos.py           # Classe Boleto com lógica de pagamento e vencimento
├── fun_aux.py           # Funções auxiliares (ex: API de câmbio)
└── README.md            # Este arquivo
🧪 Requisitos
Python 3.7+

Bibliotecas:

dateutil (instale com pip install python-dateutil)

requests (para câmbio, instale com pip install requests)

▶️ Como Executar
Clone o repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/bank-management.git
cd bank-management
Execute o sistema:

bash
Copiar
Editar
python main.py
Faça login com um nome e senha. Se a conta não existir, ela será criada automaticamente com saldo zero.

🌐 Câmbio
O sistema utiliza uma API externa para converter moedas:

BRL → USD

USD → BRL

Atenção: É necessário estar conectado à internet para essa funcionalidade funcionar corretamente.

🧾 Boletos
Boletos podem ser gerados manualmente ou automaticamente (como no caso de empréstimos). O sistema notifica boletos vencidos toda vez que o menu principal é exibido.

💰 Empréstimos
Você pode solicitar um empréstimo com:

Prazo ≤ 3 meses: 5% de juros

Prazo > 3 meses: 10% de juros

O valor total com juros será adicionado como boleto com vencimento ao final do prazo.
