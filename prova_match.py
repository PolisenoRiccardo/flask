import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  ora = datetime.datetime.now()
  
  def sato(oras):
    if oras < 12 and oras > 5:
      return ['Buogiorno', 'https://viaggin.com/wp-content/uploads/friburgo-in-svizzera.jpg']
    elif oras > 12 and oras < 18:
      return ['Buonpomeriggio', 'https://vtrend.it/wp-content/uploads/2022/11/tramonto-rosso.jpeg']
    elif oras > 18 and oras < 23:
      return ['Buonasera', 'https://cdn.studenti.stbm.it/images/2022/01/03/la-mia-sera-orig.jpeg']
    else: 
      return ['Buonanotte', 'https://assets.afcdn.com/story/20200715/2073240_w2121h1590c1cxt0cyt0cxb2121cyb1414.jpg']
    
  saluto = sato(ora.hour)[0]
  img = sato(ora.hour)[1]


  return render_template("salutobyorario.html", Titolo='Welcome', Testo='Hello, world!', saluto=saluto, img=img) 
    


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)