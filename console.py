#!/usr/bin/python3
"""program that contains the entry point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """the HBNB cmd interpreter"""

    prompt = "(hbnb)"
    intro = "Welcome to the HBNB Command Interpreter"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("quitting")
        raise SystemExit

    def do_EOF():
        """Program exits v using EOF"""
        return True

    def emptyline(self):
        """Does nothing"""
        pass

    def do_create(self, arg):
        """Creates new instance of BaseModel,
        saves it to json and prints Id"""

        pass

    def do_show(self, arg):
        """Prints string representation of an
        instance based on class name and id"""

        pass

    def do_destroy(self, arg):
        """Deletes an instance based on classname and id"""

        pass

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
