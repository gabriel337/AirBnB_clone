#!/usr/bin/python3
""" 
"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '
    class_name = {"BaseModel": BaseModel}

    def do_quit(self, line):
        """Quit command to exit the program\n """
        return True

    def do_EOF(self, line):
        """ EOF is added """
        return True

    def emptyline(self):
        """empty line if no command is given"""
        pass

    def do_create(self, arg):
        """creates a new instance of BaseModel, saves it and prints the id"""
        if len(arg) <= 0:
            print("** class name missing **")
        elif arg[0] not in self.class_name:
            print("** class doesn't exist **")
        else:
            models = eval(class_name)().save()
            print(model.id)

    def do_show(self, arg):
        """"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_name:
            print("** class doesn't exist **")


    def do_destroy(self, arg):
        """"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_name:
            print("** class doesn't exist **")


    def do_all(self, arg):
        """"""

    def do_update(self, arg):
        """"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_name:
            print("** class doesn't exist **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
