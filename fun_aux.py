import requests



#importamos a biblioteca requests para fazer requisições HTTP e poder utilizar o valor do dolar em tempo real
def obter_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # Lança erro se o status não for 200
        dados = resposta.json()
        valor_dolar = float(dados['USDBRL']['bid'])
        return valor_dolar
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Erro ao obter a cotação: {e}")
        return None


#função para converter certo valor em BRL para USD
def converter_para_dolar(valor_brl):
    valor_dolar = obter_dolar()
    return valor_brl / valor_dolar if valor_dolar else 0.0

def converter_para_brl(valor_usd):
    valor_dolar = obter_dolar()
    return valor_usd * valor_dolar if valor_dolar else 0.0
