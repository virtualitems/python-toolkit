# ----------------------------------------
# Generic object using dict
# ----------------------------------------

class AttrDict(dict):
    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value


# ----------------------------------------
# Generic object using object
# ----------------------------------------

class Object(object):
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    def __repr__(self):
        return str(self.__dict__)
