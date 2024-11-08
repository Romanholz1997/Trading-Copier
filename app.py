from flask import Flask, render_template, jsonify

app = Flask(__name__)

data = [
    {"id": 1, "account": "Metatrader 4", "mode": "Hedging", "balance":"0.00/0.00", "equity":0.00, "margin": 0.00, "openTrades": 0, "plan": "Free Master", "onOff": "Off", "status":"success"},
    {"id": 2, "account": "Metatrader 4", "mode": "Hedging", "balance":"0.00/0.00", "equity":0.00, "margin": 0.00, "openTrades": 0, "plan": "Free Master", "onOff": "Off", "status":"inactive"},
    {"id": 3, "account": "Metatrader 4", "mode": "Hedging", "balance":"0.00/0.00", "equity":0.00, "margin": 0.00, "openTrades": 0, "plan": "Free Master", "onOff": "Off", "status":"Wrong"},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
