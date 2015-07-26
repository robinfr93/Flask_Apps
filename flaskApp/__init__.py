from flask import Flask,render_template,url_for

app = Flask(__name__)



@app.route('/home')   # specify the path, yoursite.com/path, doesn't require for an actual folder to exist there though
def homepage():
	title="Parul's blogspot"
	paragraph=["Hey, welcome to my web page!!","Toodles!!"]
	pageType = "home"
	try:
	    return render_template("index.html",title=title,paragraph=paragraph,pageType=pageType)
	except Exception, e:
		return str(e)

@app.route('/about')
def aboutpage():
	title = "About the site"
	paragraph = ["Created by Robin Francis","Created on : 24/7/15"]
	pageType = "about"

@app.route('/about/contact')
def contactpage():
	title = "Contact Me"
	paragraph = ["Created by Robin Francis","Created on : 24/7/15"]
	pageType = "about"

@app.route('/stats')
def graph(chartID = 'chart_ID', chart_type = 'line', chart_height = 500):
	subtitleText = 'test'
	dataset = [[1408395614.30,430.2],[1408395614.0,431.13],[1408395476.0,431.54]]
	pageType = 'graph'
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
	title = {"text": 'My Title'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('index.html', pageType = pageType,subtitleText = subtitleText,chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
 

if __name__ == "__main__":
    app.run()