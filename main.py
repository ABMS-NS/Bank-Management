# importando funções dos outro módulos
from conta import *
from boletos import *
from datetime import datetime
from dateutil.relativedelta import relativedelta
from fun_aux import *
from decimal import Decimal, ROUND_HALF_UP

# função para exibir opções e receber a escolha do usuário
# recebe o prompt como parâmetro e retorna a opção escolhida (evitar redundância no código)
def ask_int(prompt):
    print(prompt)
    opcao = input("Digite o número da opção desejada: ")
    return opcao



def notificacoes(conta_logada, lista_boletos):
    print("\n----------- Notificações -----------\n")
    
    hoje = datetime.today().date()
    for boleto in lista_boletos:
        if conta_logada.nome == boleto.titular:
            #garante que a data está no formato correto (tipo datetime.date)
            vencimento = datetime.strptime(boleto.vencimento, "%Y-%m-%d").date()
            if vencimento < hoje:
                print(f"Boleto vencido: {boleto.nome} - R$ {boleto.valor:.2f} (Vencimento: {boleto.vencimento})")

    print("\n----------- Fim das Notificações -----------\n")


def arredondar(valor):
    return float(Decimal(valor).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))





def loop_menu(conta_logada, contas, lista_boletos):
    while True:
        print("\n=========== Menu de Operações ===========\n")
        notificacoes(conta_logada, lista_boletos)  # Exibe notificações de boletos vencidos
        opcao = ask_int("\n1. Consultar Saldo\n2. Sacar\n3. Depositar\n4. Ver Histórico\n5. Transferir\n6. Trocar de Conta\n7. Pagar boleto\n8. Câmbio Real -> Dolar \n9. Câmbio Dolar -> Real\n10. Emprestimo\n11. Sair\n")

        #opcao == "1" é consultar o saldo
        if opcao == "1":
            print(f"Seu saldo atual é (BRL): R$ {conta_logada.consultar_saldo():.2f}")
            print(f"Seu saldo atual é (USD): {conta_logada.consultar_saldo_dolar():.2f} USD")


        #saque
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            try:
                conta_logada.sacar(valor)
                conta_logada.historico.append(f"Saque: -{valor}")
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")


        #opção 3 é o depósito
        elif opcao == "3":
            valor = float(input("Digite o valor a ser depositado: "))
            try:
                conta_logada.depositar(valor)
                conta_logada.historico.append(f"Depósito: +{valor}")
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        #histórico de transação
        elif opcao == "4":
            print("Histórico de transações:")
            if conta_logada.historico:
                for transacao in conta_logada.historico:
                    print(f"- {transacao}")
            else:
                print("Nenhuma transação registrada.")

        
        # opção 5 é a transferência entre contas
        elif opcao == "5":
            nome_destino = input("Digite o nome da conta de destino: ")
            valor = float(input("Digite o valor a ser transferido: "))

            if nome_destino == conta_logada.nome:
                print("Você não pode transferir para si mesmo.")
                continue

            conta_destino = None
            for conta in contas:
                if conta.nome == nome_destino:
                    conta_destino = conta
                    break

            if conta_destino:
                try:
                    conta_logada.sacar(valor)
                    conta_destino.depositar(valor)
                    print(f"Transferência de R$ {valor:.2f} para {conta_destino.nome} realizada com sucesso!")
                    conta_logada.historico.append(f"Transferência para {conta_destino.nome}: -R$ {valor:.2f}")
                    conta_destino.historico.append(f"Recebido de {conta_logada.nome}: +R$ {valor:.2f}")
                except ValueError as e:
                    print(f"Erro na transferência: {e}")
            else:
                print("Conta de destino não encontrada.")


        #opção 6 é trocar de conta
        elif opcao == "6":
            print("Contas disponíveis:")
            for conta in contas:
                print(f"- {conta.nome}")

            nome = input("Digite o nome da conta que deseja acessar: ")
            senha = input("Digite a senha da conta: ")

            for conta in contas:
                if conta.nome == nome and conta.senha == senha:
                    conta_logada = conta
                    print(f"Conta trocada com sucesso! Bem-vindo(a), {conta_logada.nome}!")
                    loop_menu(conta_logada, contas, lista_boletos)
                    break
            else:
                print("Conta não encontrada ou senha incorreta.")

        # pagar boleto
        elif opcao == "7":
            if not lista_boletos:
                print("Nenhum boleto disponível para pagamento.")
                continue

            print("Boletos disponíveis:")
            for i, boleto in enumerate(lista_boletos):
                print(f"{i + 1}. {boleto.nome} - R$ {boleto.valor:.2f} (Vencimento: {boleto.vencimento})")

            escolha = int(input("Digite o número do boleto que deseja pagar: ")) - 1

            if 0 <= escolha < len(lista_boletos):
                boleto_escolhido = lista_boletos[escolha]
                boleto_escolhido.pagar(conta_logada, lista_boletos)
            else:
                print("Escolha inválida.")

        # opção 8 é converter de BRL para USD (real para dolar)
        elif opcao == "8":
            valor_brl = float(input("Digite o valor em BRL que deseja converter para USD: "))
            if valor_brl > conta_logada.saldo:
                print("Saldo insuficiente em BRL para conversão.")
                continue

            valor_usd = converter_para_dolar(valor_brl)
            valor_usd = arredondar(valor_usd)

            conta_logada.saldo_dolar += valor_usd
            conta_logada.saldo -= arredondar(valor_brl)

            conta_logada.historico.append(f"Conversão: +{valor_usd:.2f} USD")
            print(f"Saldo em USD atualizado: {conta_logada.saldo_dolar:.2f} USD")
            print(f"Valor convertido: R$ {valor_brl:.2f} BRL = {valor_usd:.2f} USD")


        # opção 9 é converter de USD para BRL (dolar para real)
        elif opcao == "9":
            valor_usd = float(input("Digite o valor em USD que deseja converter para BRL: "))
            if valor_usd > conta_logada.saldo_dolar:
                print("Saldo em USD insuficiente para conversão.")
                return

            valor_brl = converter_para_brl(valor_usd)
            valor_brl = arredondar(valor_brl)

            conta_logada.saldo += valor_brl
            conta_logada.saldo_dolar -= arredondar(valor_usd)

            conta_logada.historico.append(f"Conversão: +R$ {valor_brl:.2f} BRL")
            print(f"Saldo em BRL atualizado: R$ {conta_logada.saldo:.2f}")
            print(f"Valor convertido: {valor_usd:.2f} USD = R$ {valor_brl:.2f} BRL")

        # opção 10 é o empréstimo
        elif opcao == "10":
            valor_emprestimo = float(input("Digite o valor do empréstimo: "))
            prazo = int(input("Digite o prazo do empréstimo em meses: "))
            if prazo <= 0: 
                print("Prazo inválido. Deve ser maior que 0.")
                continue
            if prazo <= 3:
                taxa_juros = 0.05  # 5% de juros
            else:
                taxa_juros = 0.10

            valor_total = valor_emprestimo * (1 + taxa_juros)
            vencimento = (datetime.today() + relativedelta(months=prazo)).strftime("%Y-%m-%d")

            #cria e adiciona boleto na lista
            boleto = Boleto(conta_logada.nome, valor_total, "Empréstimo", vencimento)
            lista_boletos.append(boleto)

            conta_logada.historico.append(f"Empréstimo: +R$ {valor_emprestimo:.2f} (Vencimento: {vencimento})")
            print(f"Empréstimo de R$ {valor_emprestimo:.2f} gerado com sucesso.")
            print(f"Valor total a pagar (com juros): R$ {valor_total:.2f}")
            print(f"Vencimento em: {vencimento}")

        elif opcao == "11":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# main
def main(): 

    contas = [] # lista para armazenar as contas criadas e fazer as validações necessárias

    #inicializando contas de exemplo para o banco
    #parâmetros (Nome do usuário, Senha, Saldo inicial)
    contas.append(Conta("Kris", "1234", 1000))
    contas.append(Conta("Susie", "9876", 1500))
    contas.append(Conta("Aubrey", "4567", 2500))
    contas.append(Conta("Kel", "999", 99999))
    contas.append(Conta("Mari", "4444", 0))

    #inicializando boletos de exemplo
    lista_boletos = [] # lista para armazenar os boletos criados
    #parâmetros (Titular, Valor, Nome do boleto, Vencimento)
    lista_boletos.append(Boleto("Kris", 100, "Instalação da fonte", "2023-10-31"))
    lista_boletos.append(Boleto("Mari", 200, "Corrimão da escada", "2023-11-15"))


    #começo do menu no terminal, pede o usuário e a senha
    print("Banco Fronteira Norte - Bem-vindo!")
    print("Logue em uma conta ou crie uma.")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

    #loop para login (bem simples, possívelmente alterar depois)
    for conta in contas:
        if conta.nome == nome and conta.senha == senha:
            conta_logada = conta # armazena a conta atual(conta logada)
            print(f"Bem-vindo(a), {conta_logada.nome}!")
            break
    else:
        # se não encontrar a conta, cria uma nova
        print("Conta não encontrada. Criando uma nova conta...")
        conta_nova = Conta(nome, senha, 0)
        contas.append(conta_nova)
        conta_logada = conta_nova

    # loop do menu principal
    loop_menu(conta_logada, contas, lista_boletos)



    
if __name__ == "__main__":
    main()