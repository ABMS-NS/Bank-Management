# 💳 Banco Fronteira Norte

Este é um sistema simples de **gestão bancária** feito em Python, com funcionalidades como criação de contas, transferências, saques, depósitos, pagamento de boletos, câmbio de moedas e empréstimos.

## 📌 Funcionalidades

- Criação e login de contas
- Consulta de saldo (BRL e USD)
- Saques e depósitos
- Histórico de transações
- Transferência entre contas
- Troca de conta logada
- Pagamento de boletos (com aviso de vencidos)
- Conversão de moedas (BRL ⇄ USD)
- Empréstimos com geração automática de boletos

## 🗂️ Estrutura do Projeto

bank-management/
│
├── main.py # Arquivo principal com o menu e a lógica geral
├── conta.py # Classe Conta com métodos de movimentação e saldo
├── boletos.py # Classe Boleto com lógica de pagamento e vencimento
├── fun_aux.py # Funções auxiliares (ex: API de câmbio)
└── README.md # Este arquivo


## 🧪 Requisitos

- Python 3.7+
- Bibliotecas:
  - `dateutil` → instale com:
    ```bash
    pip install python-dateutil
    ```
  - `requests` (necessário para o câmbio):
    ```bash
    pip install requests
    ```

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/bank-management.git
   cd bank-management

2. Execute o sistema:
python main.py
