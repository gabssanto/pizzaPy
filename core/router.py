from re import A
from typing import List

class SingleRoute:
    def __init__(self, name="", component=None, arguments=[]) -> None:
        self.name = name
        self.component = component
        self.arguments = arguments


class RouterNavigate:
    def __init__(self, router, target) -> None:
        self.router = router
        self.target = target

    def value(self):
        return f"routerNavigate('{self.router}', '{self.target}')"


class Router:
    _instance = None
    appRoutes = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Router, cls).__new__(cls)
        return cls._instance

    def createRouter(self, routerName, routes: List[SingleRoute]):
        singleRoutes = {}
        arguments = {}
        for route in routes:
            singleRoutes[route.name] = route.component
            arguments[route.name] = route.arguments

        self.appRoutes[routerName] = {
            "first": routes[0].name,
            "routes": singleRoutes,
            "arguments": arguments
        }

    def render(self, router, routeName=None):
        from core.components.div import Div
        
        if routeName is None:
            routeName = self.appRoutes[router]["first"]

        route = self.appRoutes[router]["routes"][routeName]
        args = self.appRoutes[router]["arguments"][routeName]

        return Div(
            className="router_"+router,
            onLoad="setPageRouter('"+router+"')",
            children=[route(*args)]
        )

    def navigate(self, router, routeName):
        return RouterNavigate(router, routeName)
