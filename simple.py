from flask import *
import os.path
import os
import urllib
from urllib.request import *
from urllib.parse import *

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/chatTrump.html', methods=['GET'])
def handleGet():
	return render_template("chatTrump.html")

@app.route('/chatTrump.html', methods=['POST'])
def handleChat():
	msg = request.form['msg']
	data = urlencode({'botcust2':'90d4108dfe017b14', 'message':msg})
	url = "https://kakko.pandorabots.com/pandora/talk?botid=f326d0be8e345a13&amp;skin=chat"
	resp = urlopen(url, data.encode())
	ret = resp.read()
	ret = ret.decode()
	ret = ret[:ret.index("<center>")] + ret[ret.index("</center>") + 9:]
	ret = ret.replace("Mitsuku", "Trump").replace("Mousebreaker's home in Leeds","America").replace("robot","man")
	return render_template("chatTrump.html", content=Markup(ret))



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
	app.run(host='0.0.0.0', port=80)
