from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'eb1e2dfca09e0f31924bb469'

@app.route('/convert', methods=['GET'])
def convert():
    amount = request.args.get('amount', type=float)
    if amount is None:
        return jsonify({'error': 'Parâmetro "amount" é obrigatório'}), 400
    
    try:
        response = requests.get(f'https://v6.exchangerate-api.com/v6/eb1e2dfca09e0f31924bb469/latest/USD')
        data = response.json()
        
        if 'conversion_rates' in data:
            rate = data['conversion_rates']['BRL']
            converted_amount = amount * rate
            return jsonify({'amount_in_usd': amount, 'amount_in_brl': converted_amount, 'rate': rate})
        else:
            return jsonify({'error': 'Não foi possível obter a taxa de câmbio'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
