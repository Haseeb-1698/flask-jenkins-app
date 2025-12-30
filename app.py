from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to Flask Jenkins CI/CD Pipeline!',
        'status': 'success'
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'flask-app'
    })

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({
        'message': f'Hello, {name}!',
        'status': 'success'
    })

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
