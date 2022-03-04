#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import class_name
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        try:
            key = argv[0] + "." + argv[1]
        except Exception:
            pass

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if len(argv) < 2:
                    print("** instance id missing **")
                elif key in storage.all().keys():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")




    def do_destroy(self, arg):
        """Deletes an instance based on class name and id"""
        argv = arg.split()
        try:
            key = argv[0] + "." + argv[1]
        except Exception:
            pass

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if len(argv) < 2:
                    print("** instance id missing **")
                elif key in storage.all().keys():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
            elif argv[0] not in class_name:
                print("** class doesn't exist **")


    def do_all(self, arg):
        """Prints all string representation of all instances"""
        argv = arg.split()

        if len(argv) > 0 and argv[0] not in class_name:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(argv) > 0 and argv[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(argv) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        argv = arg.split()
        try:
            key = argv[0] + "." + argv[1]
        except Exception:
            pass

        if len(arg) == 0:
            print("** class name missing **")
        else:
            if argv[0] in class_name:
                if len(argv) < 2:
                    print("** instance id missing **")
                elif len(argv) < 3:
                    print("** attribute name missing **")
                elif len(argv) < 4:
                    print("** value missing **")
                elif key not in storage.all().keys():
                    print("** no instance found **")
                else:
                    for key, value in storage.all().items():
                        if argv[1] == value.id:
                            setattr(value, argv[2], argv[3].strip('"'))
                            storage.save()
            else:
                print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
