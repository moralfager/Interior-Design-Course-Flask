from flask import Flask, render_template, request, redirect, url_for
import re
from forteBankApi import getPurchaseURL, checkStatusForte
import time
import uuid
from flask_sqlalchemy import SQLAlchemy
from Crypto import encrypt
from getCourseApi import getCourseAddPerson
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Data(db.Model):
    __tablename__ = 'data'
    unique_id = db.Column(db.String,primary_key=True)
    order_id = db.Column(db.String)
    session_id = db.Column(db.String)
    url = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    email = db.Column(db.String)
    token = db.Column(db.String)

    def __init__(self, unique_id, order_id, session_id, url, name, surname, email, token):
        self.unique_id = unique_id
        self.order_id = order_id
        self.session_id = session_id
        self.url = url
        self.name = name
        self.surname = surname
        self.email = email
        self.token = token

    def __repr__(self):
        return f'<order_id {self.order_id}>'


@app.route('/')
def index():
    message = request.args.get('success')
    return render_template('index.html', message=message)

# @app.route('/buy')
# def buy():
#     return render_template('buy-page.html')

@app.route('/info')
def info():
    return render_template('course-info.html')


@app.route("/buy", methods=['GET', 'POST'])
def buy():
    base_price = '14 900₸'
    premium_price = '24 900₸'
    unique_id = str(uuid.uuid4())
    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            print(unique_id)
            name = request.form['name']
            surname = request.form['surname']
            email = request.form['email']
            token = encrypt(unique_id)
            getPurchaseURLData = getPurchaseURL(1, unique_id, name, surname, email,token)

            print(addDataDB(getPurchaseURLData))


            # return redirect(getPurchaseURL(extract_digits(base_price)*100))
            return redirect(getPurchaseURLData[3])
        elif request.form.get('action2') == 'VALUE2':
            name = request.form['name']
            surname = request.form['surname']
            email = request.form['email']
            token = encrypt(unique_id)
            print(unique_id)

            getPurchaseURLData = getPurchaseURL(2, unique_id, name, surname, email, token)

            print(addDataDB(getPurchaseURLData))

            return redirect(getPurchaseURLData[3])
            # return redirect(getPurchaseURL(extract_digits(premium_price)*100))
        else:
            print("nothing")
    elif request.method == 'GET':
        return render_template('buy-page.html',premium_price=premium_price, base_price=base_price)

    return render_template("index.html")


@app.route("/buy/checkPayment/<unique_id>", methods=['GET', 'POST'])
def checkPayment(unique_id):
    data = getElementDBbyUnique_id(unique_id)
    token = data[7]
    status = checkStatusForte(data[1], data[2])
    if status == "DECLINED":
        print('checkPayment')
        return redirect(f'/buy/getCourse/{token}')
    return redirect('/buy')


@app.route("/buy/getCourse/<token>", methods=['GET', 'POST'])
def getCourseAdd(token):
    data = getElementDBbyToken(token)
    getCourseAddPerson(data[4], data[5], data[6])
    return redirect(url_for('index', success=True))


@app.route("/submit", methods=['GET', 'POST'])
def getCoseAdd():
    return redirect(url_for('index', success=True))

def extract_digits(s):
    digits = re.findall(r'\d+', s)
    return int(''.join(digits))

def delayed_checker():
    time.sleep(60)


def addDataDB(data):
    unique_id = data[0]
    order_id = data[1]
    session_id = data[2]
    url = data[3]
    name = data[4]
    surname = data[5]
    email = data[6]
    token = data[7]
    data = Data(unique_id, order_id, session_id, url, name, surname, email, token)
    db.session.add(data)
    db.session.commit()
    return 'Data added'


def getElementDBbyUnique_id(unique_id):
    data = []

    myitems = Data.query.filter_by(unique_id=unique_id).all()
    for item in myitems:
        unique_id = item.unique_id
        order_id = item.order_id
        session_id = item.session_id
        url = item.url
        name = item.name
        surname = item.surname
        email = item.email
        token = item.token
        data.extend([unique_id,order_id,session_id,url, name,surname,email,token])
    return data

def getElementDBbyToken(token):
    data = []

    myitems = Data.query.filter_by(token=token).all()
    for item in myitems:
        unique_id = item.unique_id
        order_id = item.order_id
        session_id = item.session_id
        url = item.url
        name = item.name
        surname = item.surname
        email = item.email
        token = item.token
        data.extend([unique_id,order_id,session_id,url, name,surname,email,token])
    return data

@app.route('/about')
def about():
    return render_template('about-us.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)




