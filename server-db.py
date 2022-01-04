from email import message
from flask import Flask, render_template , url_for , request , redirect
import csv
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# DB job
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<USER_NAME>:<PASSWORD>@<HOST>/<DATABASE_NAME'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = '<SECRET_KEY>'

db = SQLAlchemy(app)


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(80), unique=True, nullable=False)
    subject = db.Column(db.String(80), unique=True, nullable=False)
    message = db.Column(db.String(300), nullable=False)

    def __init__(self,email, subject, message):
        self.email = email
        self.subject = subject
        self.message = message



@app.route('/index.html')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name) 


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        entry = Contacts(email, subject, message)
        db.session.add(entry)
        db.session.commit()
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong . Try again !'




if __name__ == '__main__':
    db.create_all()
    app.run()  
   


