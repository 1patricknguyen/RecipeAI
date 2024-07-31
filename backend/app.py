from flask import Flask, request, jsonify
from flask_cors import CORS
from jsonschema import validate, ValidationError, SchemaError
import json
import ai


app = Flask(__name__)
CORS(app)

recipe_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "ingredients": {"type": "array", "items": {"type": "string"}},
        "steps": {"type": "array", "items": {"type": "string"}}
    },
    "required": ["title", "ingredients", "steps"]
}

links_schema = {
    "type": "object",
    "properties": {
        "links": {"type": "array", "items": {"type": "object", "properties": {"title": {"type": "string"}, "link": {"type": "string"}}}}
    },
    "required": ["links"]
}


@app.route('/api/recipe', methods=['POST'])
def generate_recipe():
    data = request.get_json()
    result = json.loads((ai.create_recipe(data)))
    try:
        validate(instance=result, schema=recipe_schema)
        return jsonify(result), 200
    
    except ValidationError as e:
        return jsonify({"message": "Validation Error", "error": e.message}), 400
    
    except SchemaError as e:
        return jsonify({"message": "Schema Error", "error": e.message}), 500
    
    except Exception as e:
        return jsonify({"message": "Other Error", "error": str(e)}), 500


@app.route('/api/link', methods=['POST'])
def generate_link():
    data = request.get_json()
    result = json.loads((ai.link_recipe(data)))
    try:
        validate(instance=result, schema=links_schema)
        return jsonify(result), 200
    
    except ValidationError as e:
        return jsonify({"error": e.message}), 400
    
    except SchemaError as e:
        return jsonify({"error": e.message}), 500
    
    except Exception as e: 
        return jsonify({"error": str(e)}), 500
    
    
