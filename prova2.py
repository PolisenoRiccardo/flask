from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/en')
def hello_world():
    return render_template("index1.html", Titolo='Welcome', Testo='Hello, world!') # render_template importa un file html

@app.route('/it')
def ciao_mondo():
  return render_template("index2.html", Titolo='Benvenuti', Testo='Ciao, mondo!')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)