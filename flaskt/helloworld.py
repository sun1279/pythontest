from flask import Flask

app = Flask(__name__, static_url_path='')
#app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ =="__main__":
    app.run(debug=True, port=39003, host='0.0.0.0')
