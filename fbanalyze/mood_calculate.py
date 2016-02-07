from facepy import GraphAPI
from textblob import TextBlob

def mood_calculate():
	graph = GraphAPI('CAACEdEose0cBAGZB8uP6RcS48CoMCqWcbwi1r5gtBMxuOqdiOxHjJTRZCPZC7ZCLCjbiXVBAKxwwncU3XvXIiiLRl0DY3ZAm9QoPdzd8agKbOqvb7T6JsXEDD6nqnOv801SExEGNjPZCOUrP6A74bZBGn4D72H1r2chJnXopyaC6jXbgntxkKIR7elgcWDhxQJvzNvZAkRnRiYTZBzZBZCyJrKG')
	feed = graph.fql('SELECT message FROM status WHERE uid = me()')

	parsed_text = " "

	for message in feed['data']:
		parsed_text += message['message'].encode('ascii','ignore')

	blob = TextBlob(parsed_text)

	polarity = []
	for sentences in blob.sentences:
		polarity.append(sentences.sentiment.polarity)

	positive_count=0
	negative_count=0
	neutral_count=0

	for values in polarity:
		if values > 0.0:
			positive_count +=1
		elif values < 0.0:
			negative_count +=1
		else:
			neutral_count +=1


	maximum = positive_count

	if (neutral_count > positive_count and neutral_count > negative_count):
		return "Neutral"

	elif negative_count > positive_count:
		return "Negative"

	else:
		return "Positive"
