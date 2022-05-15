from components.div import Div
from pages.index import indexPage
from pages.counter import counterPage
from store import Store
from window import Window
import pathlib

from flask import Flask, render_template, request
app = Flask(__name__, template_folder='static')


@app.route("/")
def index():
    page = indexPage()
    return repr(Window(page))
    # Window(component)
    # return render_template('index.html')

@app.route("/counter")
def counter():
    page = counterPage()
    return repr(Window(page))

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    params = request.args.to_dict()
    store = Store()
    store.counter = int(params['updatedValue'])
    print ("Hello", params)
    return ("nothing")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
