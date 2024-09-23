from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Drink(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.name} - {self.description}'

@app.route('/')
def index12():
    return str('This typically means that you attempted to use functionality that needed the current application.'
    'To solve this, set up an application contextwith app.app_context().' 
    'See the documentation for more information')

@app.route('/more')
def get_shit():
    return {"sgf0": "dfgfd"} 

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug = True)
