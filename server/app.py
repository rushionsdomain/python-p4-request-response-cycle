# server/app.py

from flask import Flask, request, current_app, g, jsonify

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name

    # Simulating a condition: If host is not 127.0.0.1, return 404
    if host != '127.0.0.1:5555':
        return f'<h1>Resource not found</h1>', 404

    return f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user\'s device is {g.path}</h3>
    '''

@app.route('/json')
def get_json():
    # Returning a JSON response with status code 201 (Created)
    data = {"message": "Welcome to our Flask app!", "status": "success"}
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)
