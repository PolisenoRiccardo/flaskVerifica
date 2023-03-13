from flask import Flask, render_template
import datetime
now = datetime.datetime.now()

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template("index.html", ora=(now.hour, now.minute, now.second))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)