from flask import Flask, render_template, jsonify, request
import LVQ

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rekomendasi')
def rekomendasi():
    return render_template('rekomendasi.html')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        json_ = request.get_json()

        data = [
            json_['N'],
            json_['P'],
            json_['K'],
            json_['temperature'],
            json_['humidity'],
            json_['ph'],
            json_['rainfall']
        ]

        lvq = LVQ.model()
        prediction = lvq.predict(data)

        return jsonify({'prediction': str(prediction)})
    except ValueError:
        return jsonify({'error': ValueError})

@app.route('/team')
def team():
    return render_template('team.html')
