
from flask import Flask

app = Flask(__name__)

@app.route('/home')
def home():
    return "Welcome All"


if __name__ == '__main__':
    app.run(port=5008, debug=True)