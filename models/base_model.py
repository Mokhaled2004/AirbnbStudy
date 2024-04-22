#!/usr/bin/python3


import models
from uuid import uuid4
from datetime import datetime



class BaseModel:

    """Represents Base model  of the Airbnb Project"""

    def __init__(self,*args,**kwargs):
        
        """initialize a new BaseModel """
    
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key,value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value,tform)
                else :
                    self.__dict__[key] = value

        else:

            models.storage.new(self)

        def save(self):
            
            """update update_at with the current datetime """

            self.update_at = datetime.today()
            models.storage.save()

        def to_dict(self):

            """returns a dictionary containing all keys/values of __dict__ of the instance """

            returndict = self.__dict__.copy()
            returndict["created_at"] = self.created_at.isoformat()
            returndict["updated_at"] = self.updated_at.isoformat()
            returndict["__class__"] = self.__class__.__name__
            return returndict

        def __str__(self):
            """should print: [<class name>] (<self.id>) <self.__dict__> """
            return "[{}] ({}) {}".format(self.__class__.__name__,self.id,self.__dict__)
