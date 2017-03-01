from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/item/<id>')
def hello_world(id):
    return "Hello world: {}".format(id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
