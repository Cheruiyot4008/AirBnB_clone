#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.review import Review
from models.base_model import BaseModel
from models.state import State
from models.city import City
import cmd
import shlex
from models.amenity import Amenity
from models.place import Place
from models.user import User
import json
from models import storage
from datetime import datetime

"""
Module consule.py a cmd console
"""


class HBNBCommand(cmd.Cmd):
    ''' a command interpreter class '''
    prompt = "(tclb)"

    All_class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_GLX(self, arg):
        '''It Quits the  commandline CTRL+D to exit the program'''
        print("")
        return True

    def do_quit(self, arg):
        '''It Quits the  command to exit the program '''
        return True

    def do_nothing(self, arg):
        ''' does not do anything '''
        pass

    def emptyline(self):
        '''Displays  an empty line + ENTER should not execute anything '''
        pass

    def do_create(self, args):
        '''It creates a new instance BaseModel and saves prints its id '''
        if args == "":
            print("** class name missing **")
            return
        arg = shlex.split(args)
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class does not exist **")
            return
        new = HBNBCommand.All_class_dict[arg[0]]()
        new.save()
        print(new.id)

    def do_show(self, args):
        '''It Prints the string represenation of an instances class name and id '''
        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class does not exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        obj = storage.all()
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            print(str(obj[obj_key]))
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        '''It deletes an instance based on the class name and id (save changes
            into JSON file). Ex: $ destroy BaseModel 1234-1234-1234. '''

        arg = shlex.split(args)
        if len(arg) == 0:
            print("** class name missing **")
            return
        if arg[0] not in HBNBCommand.All_class_dict:
            print("** class does not exist **")
            return
        if len(arg) < 2:
            print("** instance id missing **")
            return
        storage.reload()
        obj = storage.all()
        obj_key = arg[0] + "." + arg[1]
        if obj_key in obj:
            del obj[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        '''It Prints all string representation of all instances based or not
            on the class name. Ex: $ all BaseModel or $ all '''
        storage.reload()
        json_dict = []
        obj_dict = storage.all()
        if args == "":
            for key, value in obj_dict.items():
                json_dict.append(str(value))
            print(json.dumps(json_dict))
            return
        arg = shlex.split(args)
        if arg[0] in HBNBCommand.All_class_dict.keys():
            for key, value in obj_dict.items():
                if arg[0] in key:
                    json_dict.append(str(value))
            print(json.dumps(json_dict))
            return
        else:
            print("** class does not exist **")

    def do_update(self, args):
        '''It Updates an instance based on the class name & id adding/updating
            attribute (save the change into the JSON file). Ex: $ update
            BaseModel 1234-1234-1234 email "aibnb@alxschool.com". '''

        if not args:
            print("** class name missing **")
            return
        arg = shlex.split(args)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.All_class_dict.keys():
            print("** class does not exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = arg[0] + "." + arg[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (len(arg) == 2):
            print("** attribute name missing **")
            return
        if (len(arg) == 3):
            print("** value missing **")
            return
        obj_dict = obj[obj_key].__dict__
        if arg[2] in obj_dict.keys():
            d_type = type(obj_dict[arg[2]])
            print(d_type)
            obj_dict[arg[2]] = type(obj_dict[arg[2]])(arg[3])
        else:
            obj_dict[arg[2]] = arg[3]
        storage.save()

    def do_update2(self, args):
        '''It Updates an instance based on the class name & id adding/updating
            attribute (save the change into the JSON file). Ex: $ update
            BaseModel 1234-1234-1234 email "aibnb@alxschool.com". '''

        if not args:
            print("** class name missing **")
            return
        my_dict = "{" + args.split("{")[1]
        arg = shlex.split(args)
        storage.reload()
        obj = storage.all()

        if arg[0] not in HBNBCommand.All_class_dict.keys():
            print("** class does not exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        try:
            obj_key = arg[0] + "." + arg[1]
            obj[obj_key]
        except KeyError:
            print("** no instance found **")
            return
        if (my_dict == "{"):
            print("** attribute name missing **")
            return
        my_dict = my_dict.replace("\'", "\"")
        my_dict = json.loads(my_dict)
        obj_inst = obj[obj_key]
        for y in my_dict:
            if hasattr(obj_inst, y):
                d_type = type(getattr(obj_inst, y))
                setattr(obj_inst, y, my_dict[y])
            else:
                setattr(obj_inst, y, my_dict[y])
        storage.save()

    def do_count(self, args):
        '''It counts number of instances created '''
        obj = storage.all()
        cnt = 0
        for key in obj:
            if (args in key):
                cnt += 1
        print(cnt)

    def default(self, args):
        '''The method defines actions on objects {<>}.all(), {<>}.count()
        {<>}.show(), {<>}.destroy(), {<>}.update()'''
        cmd_dict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
        }
        arg = args.strip()
        val = arg.split(".")
        if len(val) != 2:
            cmd.Cmd.default(self, arg)
            return
        class_name = val[0]
        command = val[1].split("(")[0]
        line = ""
        if (command == "update" and val[1].split("(")[1][-2] == "}"):
            inputs = val[1].split("(")[1].split(",", 1)
            inputs[0] = shlex.split(inputs[0])[0]
            line = "".join(inputs)[0:-1]
            line = class_name + " " + line
            self.do_update2(line.strip())
            return
        try:
            inputs = val[1].split("(")[1].split(",")
            for num in range(len(inputs)):
                if (num != len(inputs) - 1):
                    line = line + " " + shlex.split(inputs[num])[0]
                else:
                    line = line + " " + shlex.split(inputs[num][0:-1])[0]
        except IndexError:
            inputs = ""
            line = ""
        line = class_name + line
        if (command in cmd_dict.keys()):
            cmd_dict[command](line.strip())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
