import os
from flask import Flask, render_template

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))

TEMPLATE_DIR = os.path.join(BASE_DIR, "src", "frontend", "template")
STATIC_DIR = os.path.join(BASE_DIR, "src", "frontend")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)