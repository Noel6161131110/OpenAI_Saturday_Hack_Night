from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from summarizerAI import response_Summary
from convImgTotxt import convertImage
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///summary.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class SummaryDoc(db.Model):
    sno = db.Column(db.Integer,primary_key = True) 
    res_document = db.Column(db.String(),nullable = False)
    summa_document = db.Column(db.String(),nullable = False)


    def __repr__(self) -> str:
        return f"{self.res_document} - {self.summa_document}"



@app.route('/', methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        document = request.form['title']

        user_choice = request.form['options']
        res_doc = response_Summary(document_Text=document,user_choice = user_choice)

        summaryDel = SummaryDoc.query.first()
        db.session.delete(summaryDel)
        db.session.commit()

        summary = SummaryDoc(res_document = document , summa_document = res_doc)
        db.session.add(summary)
        db.session.commit()

    allLog = SummaryDoc.query.all()
    return render_template('index.html', allLog = allLog)

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(f.filename) 
        doc_text = convertImage(f.filename)
        user_choice = request.form['options']
        res_doc = response_Summary(document_Text=doc_text,user_choice = user_choice)

        summaryDel = SummaryDoc.query.first()
        db.session.delete(summaryDel)
        db.session.commit()

        summary = SummaryDoc(res_document = doc_text , summa_document = res_doc)
        db.session.add(summary)
        db.session.commit()

    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True, port = 8000)