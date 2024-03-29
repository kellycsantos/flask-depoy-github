from flask import Flask , jsonify

app = Flask(__name__)
app.config['TESTING'] = True 

@app.route("/")
def hello_world():
    return "<p>Hello, Flask GitHub Actions!</p>"

livros = [
    {
        "id": 0,
        "nome" : "Titulo 1",
        "autor" : "Anne"
    },
    {
        "id": 1,
        "nome" : "Titulo 2",
        "autor" : "Sakura"
    },
    {
        "id": 2,
        "nome" : "Titulo 3",
        "autor" : "Solar"
    },
    {
        "id": 3,
        "nome" : "Titulo 4",
        "autor" : "Daya"
    },
]

@app.route('/livros')
def get_livros():
    return jsonify(livros)

if __name__ == "__main__":
    app.run(debug=True, port=5100)
