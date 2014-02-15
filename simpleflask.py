from flask import Flask, Blueprint

app = Flask(__name__)
def hello2():
	return 'mmm'
bp = Blueprint('bp', __name__)

bp.route('/hello2',methods=['GET', 'POST'], endpoint='hello2')(hello2)
app.register_blueprint(bp)
print app.blueprints

@app.route('/hello')
def hello():
	return 'heloo'



if __name__ == '__main__':
	app.run()