import datetime
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
  now = datetime.datetime.now()
  return render_template("index.html", giorno=now.day, mese=now.month, anno=now.year, ora=now.hour, minuti=now.minute)

@app.route('/mappa')
def map():
  return render_template("mappa.html")

@app.route('/mappa600')
def map1():
  return render_template("mappa.html", width=600)

@app.route('/mappa800')
def map2():
  return render_template("mappa.html", width=800)

@app.route('/mappa1000')
def map3():
  return render_template("mappa.html", width=1000)
  
@app.route('/template')
def template():
  return render_template("Arsha/index.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
