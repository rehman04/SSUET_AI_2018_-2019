from flask import Flask , render_template
from data import Articles
app=Flask(__name__)

articles=Articles()
@app.route('/')
def about():
#     return '<h1>Hello Flask</h1>' #HTML State
    return render_template('about.html')

@app.route('/articles')
def article():
#     return '<h1>Hello Flask</h1>' #HTML State
    return render_template('articles.html',articles=articles)

@app.route('/articles/<id>')
def articlee(id):
    return render_template('article.html',id=id)

#server side rendereing 
#we can return complete html page by render_template
if __name__ == '__main__':
    app.run(debug=True, port=2000)

# set FLASK_APP=app.py
# $env:FLASK_APP = "app"