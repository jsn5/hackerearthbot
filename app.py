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
	val = '['
	for i in data['response']:
		if etype != None:
			if etype in i['challenge_type'].lower() and 'ongoing' in i['status'].lower():
				val+=str('{ "title" : "'+i['title']+'", "description" : "'+i['description']+'", "url" : "'+i['url']+'", "date" : "'+i['date']+'" },')
		else:
			if 'ongoing' in i['status'].lower():
				val+=str('{ "title" : "'+i['title']+'", "description" : "'+i['description']+'", "url" : "'+i['url']+'", "date" : "'+i['date']+'" },')
	if val == '[':
		val = 'No events found!'
	else:
		val = str(val[:-1]+"]")
	return val

def upcomingEvents(data, etype):
	val = '['
	for i in data['response']:
		if etype != None:
			if etype in i['challenge_type'].lower() and 'upcoming' in i['status'].lower():
				val+=str('{ "title" : "'+i['title']+'", "description" : "'+i['description']+'", "url" : "'+i['url']+'", "date" : "'+i['date']+'" },')
		else:
			if 'upcoming' in i['status'].lower():
				val+=str('{ "title" : "'+i['title']+'", "description" : "'+i['description']+'", "url" : "'+i['url']+'", "date" : "'+i['date']+'" },')
	if val == '[':
		val = 'No events found!'
	else:
		val = str(val[:-1]+"]")
	return val

def allEvents(data, etype):
	val = '['
	for i in data['response']:
		if etype != None:
			if etype in i['challenge_type'].lower():
				val+=str('{ "title" : "'+i['title']+'", "description" : "'+i['description']+'", "url" : "'+i['url']+'", "date" : "'+i['date']+'" },')
		else:
			val+=str('{ "title" : "'+i['title']+'", "description" : "'+i['description']+'", "url" : "'+i['url']+'", "date" : "'+i['date']+'" },')
	if val == '[':
		val = 'No events found!'
	else:
		val = str(val[:-1]+"]")
	return val






if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
