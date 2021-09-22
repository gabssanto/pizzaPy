from components.div import Div
import pathlib

from flask import Flask, render_template, request
app = Flask(__name__, template_folder='static')


@app.route("/")
def hello():
    a = str(pathlib.Path(__file__).parent.absolute()) + '/static/'
    f = open("{a}index.html".format(a=a), "w+")
    f.write("<script>")
    f.write(Div(className="container", children=[
            'hello', Div(children=['world'])]))
    f.write("</script>")
    f.close()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
