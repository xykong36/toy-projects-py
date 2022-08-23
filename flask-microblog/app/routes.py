from flask.templating import render_template
from app import app 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Xiangyu'}
    return render_template('index.html', title='Home', user=user) 
