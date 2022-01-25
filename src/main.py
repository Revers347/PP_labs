from flask import Flask
from waitress import serve
from methods import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint)


@app.route('/api/v1/hello-world-5')
def index():
    return "Hello World 5"

serve(app, host='0.0.0.0', port=5000)