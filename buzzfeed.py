import requests
import json
import urllib
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
#add title and subtitle below
#add favorites and separate page for favorites
#our awesome code to find the image urls 
#arrange articles by impressions (most popular bigger images)

def images():
	url = 'http://www.buzzfeed.com/api/v2/feeds/index'
	response = urllib.urlopen(url)
	data = json.loads(response.read())

	feedLength = len(data['flow'])

	images = []

	for indexInFeed in range(feedLength):
		element = {"image": data['flow'][indexInFeed]['content']['images']['dblbig']}
		element["url"] = "https://www.buzzfeed.com/" + data['flow'][indexInFeed]['content']['users'][0]['username'] + "/" + data['flow'][indexInFeed]['content']['uri']
		element["title"] = data['flow'][indexInFeed]['content']['header']['title']
		images.append(element) 
		indexInFeed+=1


	return render_template('index.html', images=images)


if __name__ == "__main__":
    app.run()

