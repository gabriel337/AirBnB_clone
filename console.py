#!/usr/bin/python3
""" 
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program\n """
        return True

    def do_EOF(self, line):
        """ EOF is added """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
