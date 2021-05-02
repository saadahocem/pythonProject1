from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/saada'
db=SQLAlchemy(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
class user (db.Model):
    __tablename__="student"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column('username',db.String(50),unique=True)
    email=db.Column(db.String(100),unique=True)


