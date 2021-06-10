from flask import Flask, redirect, url_for, request,render_template
import pyshorteners
app = Flask(__name__)

@app.route('/')
def result():
   return render_template('index.html')
@app.route('/url_shorten',methods=['POST','GET'])
def url_shorten():
   if request.method=='POST':
      url=request.form['name']
      s=pyshorteners.Shortener()
      short_url=s.tinyurl.short(url)
      return render_template('success.html',short_url=short_url)
     


if __name__ == '__main__':
   app.run(debug = True)