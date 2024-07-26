from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import ai


app = Flask(__name__)
CORS(app)
@app.route('/api/recipe', methods=['POST'])
def generate_recipe():
    data = request.get_json()
    result = json.loads((ai.create_recipe(data)))
    return jsonify(result)
    
