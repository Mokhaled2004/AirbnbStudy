#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage



class HBNBCommand(cmd.CMD):
      """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb)"

    def emptyline(self):
        """Do nothing """

        pass

    def do_quit(self, arg):
        """Quit the program """

        return True


    def do_EOF(self, arg):
        """EOF to quit the program """

        print("")
        return True

    def do_create(self, arg):

        """Usage: create <class>
        Create a new class instance and print its id.
        """

        argl = parse(arg)

        if len(argl) == 0:

            print("** class name missing **")

        elif argl[0] not in HBNBCommand.__classes:

            print("** class doesn't exist **")

        else:

            print(eval(argl[0]().id))
            storage.save()



    def do_show(self, arg):

        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """

        argl = parse(arg)
        objdir = storage.all()

        if len(argl) == 0:

            print("** class name missing **")

        elif argl[0] not in HBNBCommand.__classes:

            print("** class doesn't exist **")
        elif len(argl) == 1:

            print("** instance id missing **")

        elif "{}.{}".format(argl[0],argl[1]) not in objdir:

            print("** no instance found **")

        else:

            print(objdir["{}.{}".format(argl[0],argl[1])])


    def do_destroy(self, arg):

          """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""

        argl = parse(arg)
        objdir = storage.all()

        if len(argl) == 0:

            print("** class name missing **")

        elif argl[0] not in HBNBCommand.__classes:

            print("** class doesn't exist **")

        elif len(argl) == 1:

            print("** instance id missing **")

        elif "{}.{}".format(argl[0],argl[1]) not in objdir:

            print("** no instance found **")

        else:

            del objdir["{}.{}".format(argl[0],argl[1])]
            storage.save

      
    def do_all(self,arg)

     """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""

        argl = parse[arg]

        if len(argl) > 0 and arg[0] not in HBNBCommand.__classes:

            print("** class doesn't exist **")

        else:

            objl = []

            for obj in storage.all().values():
                
                if len(argl) > 0 and arg[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                
                elif len(argl) == 0:

                    objl.append(obj.__str__())

            print(objl)


    def do_update(self ,arg):


    







if __name__ == "__main__":
    HBNBCommand().cmdloop()
