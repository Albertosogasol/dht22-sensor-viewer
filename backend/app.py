from flask import Flask, request, jsonify
from flask_cors import CORS

# Instancia de flask
app = Flask(__name__)
CORS(app) # Permitir peticiones desde el frontend

@app.route('/temperatures', methods=['GET'])
def get_temperatures():
    # Simulación de datos
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    data = [
        {"date": "2025-01-01", "temperature": 22},
        {"date": "2025-01-02", "temperature": 24}
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)