from flask import Flask, render_template
import requests, json



app = Flask(__name__)

@app.route('/')
def index():
    cfrom = ['INS', 'EUR', 'DLR', 'GBR']
    cto = ['INS', 'EUR', 'DLR']
    print(cto)
    return render_template('index.html', cfrom=cfrom,cto=cto)



if __name__ == "__main__":
    app.run(debug=True)
    