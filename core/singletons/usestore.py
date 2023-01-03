from html.entities import html5
import pathlib

class UseStore:
    __instance = None



    def __init__(self):
        if UseStore.__instance is not None:
            raise Exception("This class is a singleton!")

        UseStore.__instance = self

    @staticmethod
    def get_instance():
        if UseStore.__instance is None:
            UseStore()

        return UseStore.__instance

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
