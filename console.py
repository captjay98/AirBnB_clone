#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models import storage

classes = ["BaseModel",
           "User",
           "Place",
           "State",
           "City",
           "Amenity",
           "Review"]


class HBNBCommand(cmd.Cmd):
    """the HBNB cmd interpreter"""

    prompt = "(hbnb)"
    intro = "Welcome to the HBNB Command Interpreter"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("quitting")
        raise SystemExit

    def do_EOF():
        """Program exits using EOF"""
        return True

    def emptyline(self):
        """Does nothing"""
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel,
        saves it to json and prints Id"""

        if not arg:
            print("** class name missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = (eval(arg)())
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints string representation of an
        instance based on class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            argv = arg.split(' ')

            if argv[0] not in classes:
                print("** class doesn't exist **")
            elif len(argv) < 2:
                print("** instance id missing **")
            else:
                key = argv[0] + "." + argv[1]
                if key in storage.all():
                    new = storage.all()[key]
                    print(new)
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on classname and id"""
        if not arg:
            print("** class name missing **")
        else:
            argv = arg.split(' ')

            if argv[0] not in classes:
                print("** class doesn't exist **")
            elif len(argv) < 2:
                print("** instance id missing **")
            else:
                key = argv[0] + '.' + argv[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """prints all string representation of all instances
        based or not on the class name"""
        pass

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        and save the change into the JSON file"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
