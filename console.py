#!/usr/bin/python3
"do_all && do_show && do_destroy is missing the condition for the instance of the class"

import cmd
from models.base_model import BaseModel
from models import class_name, storage

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

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
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in class_name:
            classes = class_name[arg]()
            print(classes.id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of the instance class and id"""
        argv = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if len(argv) < 2:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")


    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        argv = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if len(argv) < 2:
                    print("** instance id missing **")
            elif argv[0] not in class_name:
                print("** class doesn't exist **")


    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg[0] not in class_name:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        argv = arg.split()

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if len(argv) < 2:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
