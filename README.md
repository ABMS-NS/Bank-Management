# Sistema Bancário Fronteira Norte

## 🚀 Funcionalidades

### Operações Básicas
- **Consultar Saldo**: Visualizar saldo em BRL e USD
- **Sacar**: Retirar dinheiro da conta
- **Depositar**: Adicionar dinheiro à conta
- **Transferir**: Enviar dinheiro entre contas do sistema
- **Histórico**: Visualizar todas as transações realizadas

### Funcionalidades Avançadas
- **Pagamento de Boletos**: Sistema completo de geração e pagamento de boletos
- **Câmbio**: Conversão entre Real (BRL) e Dólar (USD) com cotação em tempo real
- **Empréstimos**: Solicitação de empréstimos com diferentes taxas de juros
- **Talão de Cheque**: Gerenciamento de talões de cheque
- **Metas de Investimento**: Criação e gerenciamento de metas financeiras
- **Notificações**: Alertas para boletos vencidos
- **Suporte ao Cliente**: Informações de contato

## 📋 Pré-requisitos

- Python 3.6 ou superior
- Bibliotecas necessárias:
  ```bash
  pip install requests
  pip install python-dateutil
  ```

## 🛠️ Estrutura do Projeto

O sistema é composto por quatro módulos principais:

### 1. `main.py` - Módulo Principal
- Interface do usuário e menu principal
- Controle de fluxo do programa
- Gerenciamento de login e autenticação

### 2. `conta.py` - Classe Conta
```python
class Conta:
    def __init__(self, nome, senha, saldo_inicial, talao_cheque)
    def sacar(self, valor)
    def depositar(self, valor)
    def consultar_saldo(self)
    def consultar_saldo_dolar(self)
    def verificar_talao_cheque(self)
```

### 3. `boletos.py` - Sistema de Boletos
```python
class Boleto:
    def __init__(self, titular, valor, nome, vencimento)
    def pagar(self, conta_logada, lista_boletos)
```

### 4. `fun_aux.py` - Funções Auxiliares
- Conversão de moedas com API em tempo real
- Classe para metas de investimento
- Funções utilitárias

## 🎯 Como Usar

### Execução
```bash
python main.py
```

### Primeiro Acesso
1. Execute o programa
2. Digite seu nome e senha
3. Se a conta não existir, uma nova será criada automaticamente
4. Navegue pelo menu usando os números das opções

### Contas Pré-cadastradas
Para testes, o sistema possui contas de exemplo:
- **Kris** (senha: 1234) - Saldo: R$ 1000
- **Susie** (senha: 9876) - Saldo: R$ 1500  
- **Aubrey** (senha: 4567) - Saldo: R$ 2500
- **Kel** (senha: 999) - Saldo: R$ 99999
- **Mari** (senha: 4444) - Saldo: R$ 0

## 💡 Funcionalidades Detalhadas

### Sistema de Empréstimos
- **Prazo ≤ 3 meses**: Taxa de 5%
- **Prazo > 3 meses**: Taxa de 10%
- Geração automática de boleto para pagamento

### Câmbio
- Cotação em tempo real via API (economia.awesomeapi.com.br)
- Conversão bidirecional BRL ↔ USD
- Arredondamento automático para 2 casas decimais

### Metas de Investimento
- Criação de metas personalizadas
- Depósitos incrementais
- Acompanhamento de progresso

### Sistema de Notificações
- Alertas automáticos para boletos vencidos
- Exibição no início de cada sessão

## 🔧 Tratamento de Erros

O sistema inclui tratamento robusto de erros para:
- Saldos insuficientes
- Valores inválidos
- Falhas de conexão com API
- Contas inexistentes
- Operações não autorizadas

## 📊 Histórico de Transações

Todas as operações são registradas no histórico da conta:
- Saques e depósitos
- Transferências (enviadas e recebidas)
- Pagamentos de boletos
- Conversões de moeda
- Empréstimos
- Atividades relacionadas a metas

## 🌐 API Externa

O sistema utiliza a API gratuita da AwesomeAPI para obter cotações em tempo real:
- **URL**: https://economia.awesomeapi.com.br/json/last/USD-BRL
- **Timeout**: 5 segundos
- **Fallback**: Valor padrão em caso de falha
