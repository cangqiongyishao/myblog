from flask import Flask,render_template
import requests

URL='https://api.npoint.io/674f5423f73deab1e9a7'
response=requests.get(URL)
data=response.json()

app=Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html',data=data)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html',id=id,data=data)


if __name__=='__main__':
    app.run(debug=True)