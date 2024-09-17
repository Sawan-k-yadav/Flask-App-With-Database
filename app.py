from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:sawan@localhost:3306/todo"

# Not using database name in URI as creating database with other logic below
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:sawan@localhost:3306/todo"
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str: # By __repr__ method, you can control how your objects are represented as strings.
        return f"{self.sno}-  {self.title}"

    # with app.app_context(): #  ---> This approach will create table everytime when app runs, and can give 
    #     db.create_all()     #  ---> error when table already exists.
   

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title= request.form['title']
        desc= request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    alltodo = Todo.query.all()
    return render_template('index.html', alltodo=alltodo)
    # return "<h1>hello world</h1>"


@app.route('/show')
def products():
    alltodo = Todo.query.all()
    print(alltodo)
    return "<h1>This is products page</h1>"


@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method=='POST':
        title= request.form['title']
        desc= request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)
    

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')   # If you will "/" then it will give error as no attribute as strip

if __name__ == "__main__":
    app.run(debug=True, port=8000) 