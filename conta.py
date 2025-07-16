



class Conta:
    #toda vez que criar um novo usuário precisa chamar o construtor
    def __init__(self, nome, senha, saldo_inicial):
        self.nome = nome
        self.senha = senha
        self.saldo = saldo_inicial
        self.saldo_dolar = 0.0
        self.historico = []

    #não está nos requisitos mas coloquei por uma boa prática
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            raise ValueError("Saldo insuficiente para saque.")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            raise ValueError("Valor de depósito deve ser positivo.")
    
    def consultar_saldo(self):
        return self.saldo
    
    def consultar_saldo_dolar(self):
        return self.saldo_dolar
    