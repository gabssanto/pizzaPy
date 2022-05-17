from pydoc import classname
from components.button import Button
from components.div import Div
from components.text import Text
from store import Store
from dill.source import getsource
import pickle
import json

class State:
  def __init__(self, value, modifier) -> None:
      self.value = value
      self.modifier = modifier

def addCounter(counter):
    counter += 1
    return counter

# def parseBackgroundTask(state):
#     return """
# <script type=text/javascript>
#         $(function() {
#           $('a#test').on('click', function(e) {
#             e.preventDefault()
#             $.getJSON('/background_process_test', 
#                 """ + json.dumps({ 'updateFunction': state.__hash__() }) + """,
#                 function(data) {
#                   $(".updatable > .value_"""+ str(state.__hash__()) +"""").each(function(idx) {
#                     $(this).text(data);
#                     console.log(data);
#                   });
#             });
#             return false;
#           });
#         });
# </script>
# """


def counterPage():
    #counter = Store().addFunction(addCounter)

    state = State(1, addCounter)
    Store().addState(state)

    state2 = State(56, addCounter)
    Store().addState(state2)

    # button = Div(
    #     children=['Add to counter'],
    #     style={'background-color': 'red', 'width': '100px',
    #            'padding': '16px', 'cursor': 'pointer'},
    #     #script=parseBackgroundTask(state)
    # )
    return Div(
        className="container",
        children=[
            Text(
              value=state,
            ),
            "<br>",
            Button(
              onClick=state,
              children=["HIT ME"]
            ),
            "<br><br>",
            Text(
              value=state2
            ),
            "<br>",
            Button(
              onClick=state2,
              children=["do not hit me"]
            )
            # button,
            # "<a href=# id=test><button class='btn btn-default'>Test</button></a>"
        ]
    )
