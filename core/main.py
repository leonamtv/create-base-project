import os
import inspect
import argparse
import inquirer
import importlib

from sys import argv
from core.module import Module

def get_answers ( questions ):
    return inquirer.prompt( questions )

def menu ( args ) :

    PATH_TO_MODULES = './modules'

    modules_to_import = [ x for x in os.listdir(PATH_TO_MODULES) 
                         if '.py' in x and "__" not in x ]
    imported_modules  = [ importlib.import_module( PATH_TO_MODULES.strip('./') + '.' + module.strip('.py'), package='modules' ) 
                         for module in modules_to_import ]
    imported_classes =  [ inspect.getmembers(module, inspect.isclass)[0][1] for module in imported_modules 
                         if issubclass(inspect.getmembers(module, inspect.isclass)[0][1], Module) ]
    imported_classes_names = [ imported_class.__name__ for imported_class in imported_classes ]

    if args.types:
        for project_type in imported_classes_names:
            print(' - ' + str(project_type))
    else:
        if args.path:        
            answers = get_answers([
                inquirer.List('type', message = "What kind of project would yuou like to create?", choices = imported_classes_names ),
                inquirer.Text('name', "What is the name of the project?"),
            ])
            project = imported_classes[imported_classes_names.index(answers['type'])](answers['name'], args.path[0])
            project.menu()
            project.execute()
        else:
            raise Exception('You need to provide a path where the project will be created.')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Universal project creator.',add_help=False)

    parser.add_argument('path', nargs=1, action='store', help='Path where the project will be created at.')
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this messages and exits.')
    parser.add_argument('-t', '--types', action='store_true', help='Print types of projects one can create.')
    parser.add_argument('-c', '--create', action='store_true', help='Creates a new module.')

    args = parser.parse_args()

    menu( args )
