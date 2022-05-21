import json
from core.components.div import Div
from core.router import Router, SingleRoute
from core.handleDOM import handleDOM
from pages.countercomponent import CounterComponent
from pages.counterhome import HomeComponent
from pages.index import indexPage
from pages.counter import counterPage
from pages.matplotlib_page import matplotlibPage
from core.singletons.store import Store
from window import Window

from flask import Flask, render_template, request
app = Flask(__name__, template_folder='static')
app.register_blueprint(handleDOM)

counterRoutes = [
    SingleRoute("/", HomeComponent),
    SingleRoute("/pag1", CounterComponent, [1, True]),
    SingleRoute("/pag2", CounterComponent, [50, False])
]

Router().createRouter("counter", counterRoutes)


@app.route("/")
def index():
    page = indexPage()
    return repr(Window(page))
    # Window(component)
    # return render_template('index.html')


@app.route("/counter/", defaults={"path": None})
@app.route("/counter/<path>")
def counter(path):
    if path is not None:
        path = "/" + path

    page = counterPage(path)
    return repr(Window(page))

@app.route("/test")
def matplot():
    page = matplotlibPage()
    return repr(Window(page))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
