from flask import Flask, render_template, request
from weather_util import get_weather
import crawl_util as cu

app = Flask(__name__)

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'sc':0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app))

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'sc':1}
    return render_template('prototype/schedule.html', menu=menu, weather=get_weather(app))

@app.route('/interpark')
def interpark():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    book_list = cu.interpark()
    return render_template('prototype/interpark.html', book_list=book_list, menu=menu, weather=get_weather(app))

@app.route('/genie')
def genie():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    chart_list = cu.genie()
    return render_template('prototype/genie.html', chart_list=chart_list, menu=menu, weather=get_weather(app))

@app.route('/siksin')
def siksin():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    siksin_list = cu.siksin()
    return render_template('prototype/siksin.html', siksin_list=siksin_list, menu=menu, weather=get_weather(app))

if __name__ == '__main__':
    app.run(debug=True)
