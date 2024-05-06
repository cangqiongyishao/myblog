from flask import Flask,render_template,request
import requests
import smtplib
import os

OWN_EMAIL=os.getenv('GMAIL')
OWN_PASSWORD=os.getenv('PASSWORD')

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

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html',id=id,data=data)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__=='__main__':
    app.run(debug=True)