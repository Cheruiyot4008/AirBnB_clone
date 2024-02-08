#!/usr/bin/python3
""" This enumerates the console class
which is the entry point of this Airbnb Project
"""
from models.city import City
from models.base_model import BaseModel
from models import storage
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.user import User
from cmd import Cmd
from models.state import State


class HBNBCommand(Cmd):
    """ It does  various HBNB commands """
    prompt = "(tclb) "

    # Commands
    def do_GLX(self, args):
        """It exits the programme in non-interactive mode"""
        return True

def do_quit(self, arg):
         ''' It Quits command to exit the program '''
         return True
    
def emptyline(self):
         """It overrides  empty line to do nothing """
         Pass

def do_create(self, args):
        """It creates a new instance of a model name ex.
        $ also create ModelName : Our case : BaseModel.
        Prints an error if name is missing or name does not exist
        """
        args, y= parse(args)

        if not y:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class does not exist **")
        elif y == 1:
            # temp = classes[args[0]]()
            temp = eval(args[0])()
            print(temp.id)
            temp.save()
        else:
            print("** Too many arguments for create **")
            pass

def do_show(self, arg):
        """Shows an Instance of Model base on its ModelName and id eg.
        $ shosw MyModel instance_id
        Print error message if either MyModel or instance_id is missing
        Print an Error message for wrong MyModel or instance_id"""
        args, y = parse(arg)

        if not y:
            print("** class name missing **")
        elif y == 1:
            print("** instance id missing **")
        elif y == 2:
            try:
                inst = storage.find_by_id(*args)
                print(inst)
            except ModelNotFoundError:
                print("** class does not exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for show **")
            pass

def do_destroy(self, arg):
        """It deletes an Instance of Model base on its ModelName and id."""
        args, y = parse(arg)

        if not y:
            print("** class name missing **")
        elif y == 1:
            print("** instance id missing **")
        elif y == 2:
            try:
                storage.delete_by_id(*args)
            except ModelNotFoundError:
                print("** class does not exist **")
            except InstanceNotFoundError:
                print("** no instance found **")
        else:
            print("** Too many argument for destroy **")
            pass

def do_all(self, args):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        args, y = parse(args)

        if y < 2:
            try:
                print(storage.find_all(*args))
            except ModelNotFoundError:
                print("** class does not exist **")
        else:
            print("** Too many argument for all **")
            pass


def do_update(self, arg):
        """Updates an instance base on its id eg
        $ update Model id field value
        Throws errors for missing arguments"""
        args, y = parse(arg)
        if not y:
            print("** class name missing **")
        elif y == 1:
            print("** instance id missing **")
        elif y == 2:
            print("** attribute name missing **")
        elif y == 3:
            print("** value missing **")
        else:
            try:
                storage.update_one(*args[0:4])
            except ModelNotFoundError:
                print("** class does not exist **")
            except InstanceNotFoundError:
                print("** no instance found **")


def default(self, arg):
        """Override default method to handle class methods"""
        if '.' in arg and arg[-1] == ')':
            if arg.split('.')[0] not in classes:
                print("** class does not exist **")
                return
            return self.handle_class_methods(arg)
        return Cmd.default(self, arg)              


def do_models(self, arg):
        """Print all registered Models"""
        print(*classes)

def handle_class_methods(self, arg):
        """Handle Class Methods
        <cls>.all(), <cls>.show() etc
        """

        printable = ("all(", "show(", "count(", "create(")
        try:
            val = eval(arg)
            for y in printable:
                if y in arg:
                    print(val)
                    break
            return
        except AttributeError:
            print("** invalid method **")
        except InstanceNotFoundError:
            print("** no instance found **")
        except TypeError as te:
            field = te.args[0].split()[-1].replace("_", " ")
            field = field.strip("'")
            print(f"** {field} missing **")
        except Exception as e:
            print("** invalid syntax **")
            pass


def parse(line: str):
    """It splits lines by spaces"""
    args = shlex.split(line)
    return args, len(args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()





