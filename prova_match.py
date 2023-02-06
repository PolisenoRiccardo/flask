import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  ora = datetime.datetime.now()
  
  if ora.hour < 12 and ora.hour > 5:
    saluto = 'Buogiorno'
    img = 'https://viaggin.com/wp-content/uploads/friburgo-in-svizzera.jpg'
  elif ora.hour > 12 and ora.hour < 18:
    saluto = 'Buonpomeriggio'
    img = 'https://vtrend.it/wp-content/uploads/2022/11/tramonto-rosso.jpeg'
  elif ora.hour > 18 and ora.hour < 23:
    saluto = 'Buonasera'
    img = 'https://cdn.studenti.stbm.it/images/2022/01/03/la-mia-sera-orig.jpeg'
  else: 
    saluto = 'Buonanotte'
    img = 'https://assets.afcdn.com/story/20200715/2073240_w2121h1590c1cxt0cyt0cxb2121cyb1414.jpg'

  return render_template("salutobyorario.html", Titolo='Welcome', Testo='Hello, world!', saluto=saluto, img=img) 
    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)