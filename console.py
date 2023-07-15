#!/usr/bin/python3
"""Entry point of the command interpreter."""
import cmd
import json
import models


class HBNBCommand(cmd.Cmd):
    """Class for HBNB command interpreter"""

    prompt = "(hbnb) "
    valid_models = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Do nothing when the empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of the given class,
        and save it to the JSON file.
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        try:
            class_obj = getattr(models, class_name)
        except AttributeError:
            print("** class doesn't exist **")
            return
        new_instance = class_obj()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if arg == "":
            print("** class name missing **")
            return
        try:
            args = arg.split()
            cls = args[0]
            if cls not in HBNBCommand.valid_models:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(cls, obj_id)
            if key not in models.storage.all():
                print("** no instance found **")
                return
            print(models.storage.all()[key])
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg == "":
            print("** class name missing **")
            return
        try:
            args = arg.split()
            cls = args[0]
            if cls not in HBNBCommand.valid_models:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(cls, obj_id)
            if key not in models.storage.all():
                print("** no instance found **")
                return
            models.storage.all().pop(key)
            models.storage.save()
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        try:
            if arg == "":
                print([str(v) for v in models.storage.all().values()])
            elif arg in HBNBCommand.valid_models:
                objs = [str(v) for k, v in models.storage.all().items()
                        if arg in k]
                print(objs)
            else:
                print("** class doesn't exist **")
        except Exception as e:
            print(e)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if arg == "":
            print("** class name missing **")
            return
        try:
            args = arg.split()
            cls = args[0]
            if cls not in HBNBCommand.valid_models:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = "{}.{}".format(cls, obj_id)
            if key not in models.storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            obj = models.storage.all()[key]
            setattr(obj, attr_name, attr_value)
            models.storage.save()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
