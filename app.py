from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados do voo AZU2454
FLIGHT_DATA = {
    "AZU2454": {
        "flight_number": "AZU2454",
        "origin": {
            "code": "CGH",
            "city": "São Paulo",
            "date": "18 de mai.",
            "terminal": "-",
            "gate": "-",
            "scheduled_time": "06:00",
            "actual_time": "06:12",
            "status": "Partiu"
        },
        "destination": {
            "code": "MCZ",
            "city": "Maceió",
            "date": "18 de mai.",
            "terminal": "T1",
            "gate": "E02",
            "scheduled_time": "08:55",
            "actual_time": "09:01",
            "status": "Chegou"
        },
        "flight_info": {
            "duration": "2h 49min",
            "status": "Concluído",
            "progress": {
                "completed": True,
                "percentage": 100
            }
        }
    }
}

@app.route('/api/flight', methods=['GET'])
def flight_info():
    flight_number = request.args.get('number')
    
    if not flight_number:
        return jsonify({
            "status": "error",
            "error": {
                "code": "MISSING_FLIGHT_NUMBER",
                "message": "O número do voo é obrigatório"
            }
        }), 400
    
    if flight_number in FLIGHT_DATA:
        return jsonify({
            "status": "success",
            "data": FLIGHT_DATA[flight_number]
        })
    
    return jsonify({
        "status": "error",
        "error": {
            "code": "FLIGHT_NOT_FOUND",
            "message": "Não foi possível encontrar informações para o voo especificado"
        }
    }), 404

@app.route('/', methods=['GET'])
def index():
    return "API de Voos - Use /api/flight?number=AZU2454"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
