import os
import inquirer
import subprocess

class Module :
    def __init__ ( self, name, path ):
        self.name = name
        self.path = path

    def check_if_can_create ( self ):
        pass

    def go ( self ):
        self.menu()
        self.execute()

    def execute ( self, **kwargs ):
        pass

    def menu ( self ):
        pass