import json
from components.div import Div
from core.router import Router, SingleRoute
from pages.countercomponent import CounterComponent
from pages.counterhome import HomeComponent
from pages.index import indexPage
from pages.counter import counterPage
from store import Store
from window import Window
import pathlib

from flask import Flask, render_template, request
app = Flask(__name__, template_folder='static')

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

# background process happening without any refreshing


@app.route('/background_process_test')
def background_process_test():
    params = request.args.to_dict()

    if 'updateFunction' in params:
        state = Store().getState(params['updateFunction'])
        state.value = state.modifier(state.value)
        return (str(state.value))
    elif 'router' in params and 'path' in params:
        router = params['router']
        routeName = params['path']
        response = {
            "path": "/" + router + routeName,
            "body": str(Router().render(router, routeName))
        }
        return (json.dumps(response))

    return ('no return')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
