#from static.index import element
from window import Window

from flask import Flask, render_template, request
app = Flask(__name__, template_folder='static')

@app.route("/")
def index():
    return repr(Window(None, "Pizza!"))
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
