import os
import inquirer
import subprocess

class Module :
    def __init__ ( self, name, path ):
        self.name = name
        self.path = path

    def execute ( self, **kwargs ):
        pass

    def menu ( self ):
        pass