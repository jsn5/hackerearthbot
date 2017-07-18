import urllib.request, json
from flask import Flask, abort, request


app = Flask(__name__)
@app.route('/', methods=['GET'])
def homepage():
	link = 'https://www.hackerearth.com/chrome-extension/events/'
	event_type = request.args.get('type')
	event_status = request.args.get('status')
	with urllib.request.urlopen(link) as url:
		data = json.loads(url.read().decode())

	options={0 : ongoingEvents,
			 1 : upcomingEvents,
			 2 : allEvents}	

	if event_status == 'ongoing':
		c = 0
	elif event_status == 'upcoming':
		c = 1
	else:
		c = 2

	return options[c](data,event_type) 


def ongoingEvents(data, etype):
	val = ''
	for i in data['response']:
		if etype != None:
			if etype in i['challenge_type'].lower() and 'ongoing' in i['status'].lower():
				val+=str("<h1>"+i['title']+"</h1><p>"+i['description']+"</p><p>"+i['url']+"</p><p>"+i['date']+"</p>")
		else:
			if 'ongoing' in i['status'].lower():
				val+=str("<h1>"+i['title']+"</h1><p>"+i['description']+"</p><p>"+i['url']+"</p><p>"+i['date']+"</p>")
	if val == '':
		val = 'No events found!'
	return val

def upcomingEvents(data, etype):
	val = ''
	for i in data['response']:
		if etype != None:
			if etype in i['challenge_type'].lower() and 'upcoming' in i['status'].lower():
				val+=str("<h1>"+i['title']+"</h1><p>"+i['description']+"</p><p>"+i['url']+"</p><p>"+i['date']+"</p>")
		else:
			if 'upcoming' in i['status'].lower():
				val+=str("<h1>"+i['title']+"</h1><p>"+i['description']+"</p><p>"+i['url']+"</p><p>"+i['date']+"</p>")
	if val == '':
		val = 'No events found!'
	return val

def allEvents(data, etype):
	val = ''
	for i in data['response']:
		if etype != None:
			if etype in i['challenge_type'].lower():
				val+=str("<h1>"+i['title']+"</h1><p>"+i['description']+"</p><p>"+i['url']+"</p><p>"+i['date']+"</p>")
		else:
			val+=str("<h1>"+i['title']+"</h1><p>"+i['description']+"</p><p>"+i['url']+"</p><p>"+i['date']+"</p>")
	if val == '':
		val = 'No events found!'
	return val






if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
