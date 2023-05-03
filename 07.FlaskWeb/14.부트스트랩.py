import os
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
import map_util as mu
import crawl_util as cu

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('14.carousel.html')

@app.route('/scatter', methods=['GET','POST'])
def scatter():
    if request.method == 'GET':
        return render_template('09.산점도.html')
    else:
        num = int(request.form['num'])
        mean = float(request.form['mean'])
        std = float(request.form['std'])
        min = float(request.form['min'])
        max = float(request.form['max'])
        xs = np.random.normal(loc=mean, scale=std, size=num)
        ys = np.random.uniform(min, max, num)
        plt.figure()
        plt.scatter(xs, ys)
        filename = os.path.join(app.static_folder, 'img/scatter.png')
        plt.savefig(filename)
        return render_template('09.산점도_res.html')

@app.route('/hotPlaces', methods=['GET','POST'])
def hotPlaces():
    if request.method == 'GET':
        return render_template('10.hotplaces.html')
    else:
        # client가 입력한 장소 알아내기
        place1 = request.form['place1']
        place2 = request.form['place2']
        place3 = request.form['place3']
        places = [place1, place2, place3]
        mu.hot_places(places, app)
        return render_template('10.hotplaces_res.html')

@app.route('/interpark')
def interpark():
    book_list = cu.interpark()
    return render_template('11.interpark.html', book_list=book_list)

@app.route('/progress')
def progress():
    return render_template('13.progress bar.html')

if __name__ == '__main__':
    app.run(debug=True)
