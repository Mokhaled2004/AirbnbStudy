#!/usr/bin/python3

"""Define the FileStorage class """
import json
from models.base_model import BaseModel




class FileStorage:

    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):

         """Return the dictionary __objects."""

        return FileStorage.__objects
        

    def new(self,obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,obj.id)] = obj


    def save(self):
         """Serialize __objects to the JSON file __file_path."""

        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path,"w") as f:
            json.dump(objdict, f)


    def reload(self):
         """Deserialize the JSON file __file_path to __objects, if it exists."""
         with open(FileStorage.__file_path) as f:
             objdict = json.load(f)

             for obj in objdict.values():
                 cls_name = obj["__class__"]
                 del obj["__class__"]
                 self.new(eval(cls_name)(**obj))
