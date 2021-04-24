from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "homepage"

@app.route('/contact')
def contact():
    return "app page"

if __name__ == '__main__':
    app.run()

