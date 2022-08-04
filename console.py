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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
