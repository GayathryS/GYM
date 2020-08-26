from database import Database
import uuid
class User(object):
    def __init__(self, name,_id):
        self.name = name
        self._id = _id

class Details(object):
    def __init__(self,_id,name,email):
        self.name = name
        self._id = _id
        self.email = email