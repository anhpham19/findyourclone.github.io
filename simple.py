from flask import *
import os.path
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/chatTrump.html', methods=['POST'])
def handleChat():
	print(request.form['msg'])
	return render_template('chatTrump.html')

@app.route('/profiles/<name>')
def handle_name(name):
	print(name)
	if(os.path.exists("templates/profiles/" + name)):
		print("Found a profile!")
		return render_template("profiles/" + name)
	else:
		print("Profile Not Exist")
		return redirect('https://en.wikipedia.org/wiki/' + name.replace('.html', ''))

@app.route('/<path:path>')
def catch_all(path):
	print('catch all!')
	print(path)
	return send_from_directory('templates/', path);

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
