from html.entities import html5
import pathlib

class Store: 
    _instance = None
    # counter = 0
    # fmap = {}
    smap = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Store, cls).__new__(cls)
        return cls._instance

    def addState(self, state):
        self.smap[str(state.__hash__())] = state
        return (state.value, state.modifier)

    def getState(self, hash):
        return self.smap[hash]

    # def addFunction(self, function):
    #     fhash = function.__hash__()
    #     self.fmap[str(fhash)] = function
    #     return fhash

    # def getFunction(self, hash):
    #     return self.fmap[hash]