from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import Serializer


app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

class studentInfo(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    course = db.Column(db.String(length=30), nullable=False)
    score = db.Column(db.Integer(), nullable=False)

@app.route('/studentinfo', methods=["GET"])
def studentinfo():
    dbinfo = studentInfo.query.all()
    averagescore = 0
    count = 0
    passedlist = []
    failedlist=[]
    for student in dbinfo:
        averagescore+=student.score
        count+=1
        if student.score < 50:
            failedlist.append((student.name,student.score))
        else:
            passedlist.append((student.name,student.score))
    averagescore=averagescore/count
    return render_template("info.html", passed=passedlist, failed=failedlist, avg=averagescore)

if __name__=="__main__":
    app.run(debug=True)