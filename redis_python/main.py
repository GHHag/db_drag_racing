from flask import Flask, jsonify, request
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/<key>', methods=['GET'])
def get_value(key):
    value = r.get(key)
    if value is None:
        return jsonify({'error': 'Key not found'}), 404
    else:
        return jsonify({'value': value.decode('utf-8')}), 200

@app.route('/<key>', methods=['PUT'])
def update_value(key):
    if request.is_json:
        data = request.get_json()
        value = data.get('value')
        if value is not None:
            r.set(key, value)
            return jsonify({'message': 'Value updated'}), 200
    return jsonify({'error': 'Invalid request data'}), 400

@app.route('/<key>', methods=['DELETE'])
def delete_value(key):
    result = r.delete(key)
    if result == 1:
        return jsonify({'message': 'Key deleted'}), 200
    else:
        return jsonify({'error': 'Key not found'}), 404

@app.route('/', methods=['POST'])
def create_value():
    if request.is_json:
        data = request.get_json()
        key = data.get('key')
        value = data.get('value')
        if key is not None and value is not None:
            result = r.set(key, value)
            if result:
                return jsonify({'message': 'Value created'}), 201
            else:
                return jsonify({'error': 'Failed to create value'}), 500
    return jsonify({'error': 'Invalid request data'}), 400

if __name__ == '__main__':
    app.run(debug=True)