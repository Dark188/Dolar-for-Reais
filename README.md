# API de Conversão de Dólar para Real

Esta é uma API simples construída com Flask para converter valores de dólar para real brasileiro usando uma taxa de câmbio atual.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/Dark188/Dolar-for-Reais
    cd .\Dolar-for-Reais\ 
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Defina sua chave da API de câmbio em `API_KEY` no arquivo `app.py`.

2. Execute a aplicação:
    ```bash
    python app.py
    ```

3. Acesse a API em `http://127.0.0.1:5000/convert?amount=10`, substituindo `10` pelo valor que deseja converter.

## Exemplo de Requisição

GET /convert?amount=10 HTTP/1.1
Host: 127.0.0.1:5000

## Exemplo de Resposta

```json
{
    "amount_in_usd": 10.0,
    "amount_in_brl": 50.0,
    "rate": 5.0
}


