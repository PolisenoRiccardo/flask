from flask import Flask # obbligatorio
app = Flask(__name__)

@app.route('/', methods=['GET']) # hosta una pagina ('/' è la home)
def hello_world():
    return ('<h1>Ciao, mondo!</h1>')

@app.route('/en', methods=['GET']) # hosta un'altra pagina 
def help_world():
    return ('<h1>Help, world!</h1>')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True) # obbligatorio