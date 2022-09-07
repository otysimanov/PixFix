from logging import exception
from flask import Flask, render_template, redirect, jsonify, url_for, request
import requests
import datetime
import hashlib
import hmac
import pyautogui
from backend.config import config, snap, core
from midtransclient import error_midtrans

app = Flask('__name__', static_folder='static', static_url_path='')

app.register_blueprint(config)


@app.route('/')
def index():
    
    
    return render_template('index.html', client_key = snap.api_config.client_key)
    
@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        nama = request.form.get('nama_lengkap')
        email = request.form.get('email')
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            transaction_token = snap.create_transaction_token({
                "transaction_details": {
                    "order_id": "pixfix-"+timestamp,
                    "gross_amount": 35000
                }, "credit_card":{
                    "secure" : True
                }, "enabled_payments": ['shopeepay'],
                "customer_details": {
                    "first_name": nama,
                    "email": email,
                }
            })

            return jsonify({'token': transaction_token})
        except error_midtrans.MidtransAPIError as err:
            return jsonify({'error': err})
        return jsonify({"nama":nama, "email": email})



@app.route('/berhasil')
def berhasil():
    return render_template('success.html')

@app.route('/lanjut')
def lanjut():
    pyautogui.hotkey('alt', 'tab')
    res = requests.get('http://localhost:1500/api/start?mode=print&password=H7n4ME7rO9tEJD0S')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5005)
