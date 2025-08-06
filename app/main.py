from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-change-in-production'
CORS(app)

@app.route('/')
def index():
    return '<h1>Welcome to Bitties!</h1><p>Your Bitcoin Investment Tracker</p><a href="/dashboard">Go to Dashboard</a>'

@app.route('/dashboard')
def dashboard():
    return '<h1>Dashboard</h1><p>Coming soon...</p>'

@app.route('/api/status')
def api_status():
    return jsonify({'status': 'online', 'version': '1.0.0'})

if __name__ == '__main__':
    app.run(debug=True)