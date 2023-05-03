from flask import Flask, render_template
import crawl_util as cu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/interpark')
def interpark():
    book_list = cu.interpark()
    return render_template('11.interpark.html', book_list=book_list)

if __name__ == '__main__':
    app.run(debug=True)
