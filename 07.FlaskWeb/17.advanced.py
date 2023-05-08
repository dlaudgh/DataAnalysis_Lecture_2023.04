from flask import Flask, render_template, request
from weather_util import get_weather
import crawl_util as cu
import os, random

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    global quote       # quotes 변수를 전역 변수로 만들어 줌
    filename = os.path.join(app.static_folder, 'data/todayQuote.txt')
    with open(filename, encoding='utf-8') as f:
        quotes = f.readlines()
    quote = random.sample(quotes, 1)[0]

@app.route('/')
def home():
    menu = {'ho':1, 'us':0, 'cr':0, 'sc':0}
    return render_template('prototype/home.html', menu=menu, weather=get_weather(app),
                           quote=quote)

@app.route('/interpark')
def interpark():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    book_list = cu.interpark()
    return render_template('prototype/interpark.html', book_list=book_list, 
                           menu=menu, weather=get_weather(app), quote=quote)

@app.route('/genie')
def genie():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    song_list = cu.genie()
    return render_template('prototype/genie.html', song_list=song_list, 
                           menu=menu, weather=get_weather(app), quote=quote)

@app.route('/siksin', methods=['GET', 'POST'])
def siksin():
    menu = {'ho':0, 'us':0, 'cr':1, 'sc':0}
    if request.method == 'GET':
        return render_template('prototype/siksin.html', menu=menu, weather=get_weather(app),
                               quote=quote)
    else:
        place = request.form['place']
        food_list = cu.siksin(place)
        return render_template('prototype/siksin_res.html', food_list=food_list, 
                               menu=menu, weather=get_weather(app), place=place, quote=quote)

@app.route('/schedule')
def schedule():
    menu = {'ho':0, 'us':0, 'cr':0, 'sc':1}
    return render_template('prototype/schedule.html', menu=menu, weather=get_weather(app),
                           quote=quote)

if __name__ == '__main__':
    app.run(debug=True)