from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/data', methods=['POST'])
def receive_data():
    if not request.is_json:
        return jsonify({"error": "Invalid Content-Type, expected application/json"}), 415
    data = request.get_json()
    return jsonify({"received": data})

if __name__ == "__main__":
    app.run(debug=True)
