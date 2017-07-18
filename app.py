import urllib.request, json 
from flask import Flask

app = Flask(__name__)
link = 'https://www.hackerearth.com/chrome-extension/events/'
@app.route('/')
def homepage():
	with urllib.request.urlopen(link) as url:
	data = json.loads(url.read().decode())
	
	return """
	<h1>Hello heroku</h1>
	<p>It is currently {time}.</p>
	""".format(time=data['response'][0]['time'])

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)




