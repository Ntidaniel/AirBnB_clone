#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""
import cmd
import sys
from models.base_model import BaseModel
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = args[0] + '.' + args[1]
            print(models.storage.all()[key])
        except KeyError:
            print("** no instance found **")
        except:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        try:
            key = args[0] + '.' + args[1]
            del models.storage.all()[key]
            models.storage.save()
        except KeyError:
            print("** no instance found **")
        except:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = arg.split()
        objects = models.storage.all()
        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        else:
            if args[0] not in models.classes:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in objects.values()
                   if type(obj).__name__ == args[0]])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        try:
            key = args[0] + '.' + args[1]
            obj = models.storage.all()[key]
            setattr(obj, args[2], args[3])
            models.storage.save()
        except KeyError:
            print("** no instance found **")
        except:
            print("** class doesn't exist **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
