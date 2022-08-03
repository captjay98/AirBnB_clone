#!/usr/bin/python3
"""Console that contains entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class that contains entry point of the command interpreter""" 

    def_prompt = "Welcome to the HBNH command interpreter"
    prompt = "(HBNB)"

    def do_create(self):
        'creates an instance'
        pass

    def do_update(self):
        'updates the instance'
        pass

    def do_show(self):
        "shows all availbale instances"
        pass

    def do_destroy(self):
        'destorys the intance'
        pass

    def do_all(self):
        'do all command'
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("This will quit the command interpreter")
        raise SystemExit

    def do_EOF(self, arg):
        'EOF exits the program'
        return True

    def emptyline(self):
        """Empty line prints"""
        pass










if __name__ == '__main__':
    HBNBCommand().cmdloop()