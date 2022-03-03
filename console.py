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
            print(models.id)

    def do_show(self, arg):
        """Prints the string representation of the instance class and id"""
        arg.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_name:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_name:
            print("** class doesn't exist **")


    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg[0] not in self.class_name:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.class_name:
            print("** class doesn't exist **")




if __name__ == '__main__':
    HBNBCommand().cmdloop()
