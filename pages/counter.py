from components.div import Div
from store import Store
from dill.source import getsource
import pickle
import json

def addCounter(counter):
    counter += 1
    return counter

def parseBackgroundTask(counter):
    foo = dict()
    variable = f'{foo=}'.split('=')[0]
    return """<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script type=text/javascript>
        $(function() {
          $('a#test').on('click', function(e) {
            e.preventDefault()
            $.getJSON('/background_process_test', 
                """ + json.dumps({ 'updatedValue': addCounter(counter), 'variable': variable }) + """,
                function(data) {
              //do nothing
            });
            return false;
          });
        });
</script>
"""


def counterPage():
    counter = Store().counter
    button = Div(
        children=['Add to counter'],
        style={'background-color': 'red', 'width': '100px',
               'padding': '16px', 'cursor': 'pointer'},
        script=parseBackgroundTask(counter)
    )
    return Div(
        className="container",
        children=[
            counter,
            button,
            "<a href=# id=test><button class='btn btn-default'>Test</button></a>"
        ]
    )
