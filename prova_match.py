import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  ora = datetime.datetime.now()
  
  if ora.hour < 12 and ora.hour > 0:
    saluto = 'Buogiorno'
  else:
    saluto = 'Buonpomeriggio'
  return render_template("salutobyorario.html", Titolo='Welcome', Testo='Hello, world!', saluto=ora) 
    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)