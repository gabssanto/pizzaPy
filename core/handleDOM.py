import json
from core.router import Router
from core.singletons.store import Store
import warnings
from flask import Blueprint, request

handleDOM = Blueprint('handleDOM', __name__)

# background process happening without any refreshing
@handleDOM.route('/handleDOM')
def index():
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

    return warnings.warn("PizzaPy Virtual DOM does not implement the given parameters")