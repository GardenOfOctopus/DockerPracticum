from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import uuid
from urllib.request import urlopen
import time
app = Flask("service")

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://root:password@db:5432/database'
db = SQLAlchemy(app)


class Data(db.Model):
  id = db.Column(db.Uuid, primary_key=True)
  time = db.Column(db.Double, unique=False, nullable=False)
  text = db.Column(db.Text, unique=False, nullable=False)

  def __repr__(self):
        return f"<Data: {self.text}, {self.time}>"
  
with app.app_context():
    db.create_all()
    db.session.commit()
  
def post_data_to_db(text, time):
    data = Data(id=uuid.uuid4(), text=text, time=time)
    db.session.add(data)
    db.session.commit()

def get_data_from_db():
    data_list = db.session.query(Data).all()
    print("Data list:",data_list)
    return data_list

def clear_data_from_db():
    dataToDelete_list = db.session.query(Data).all()
    for dataToDelete in dataToDelete_list:
        db.session.delete(dataToDelete) 
        db.session.commit()

@app.route("/post/<text>")
def post_data(text):
    post_data_to_db(text, time.time())
    return f"Your data '{text}' was posted to database"

@app.route('/get')
def get_data():
    data_list = get_data_from_db()
    return render_template("get.html", data_list=data_list)

@app.route('/clear')
def clear_data():
    clear_data_from_db()
    return f"All data was deleted from database"

app.run(host='0.0.0.0', debug=True)
