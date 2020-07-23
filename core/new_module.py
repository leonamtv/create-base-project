import os
import inquirer

from core.module import Module

class NewModule ( Module ):
    
    def __init__ ( self, name = '', path = '' ):
        Module.__init__( self, name, path )
    
    def execute ( self ):
        if self.name != '':
            if self.path != '' or not os.path.exists( self.path ):
                file = open(os.path.join(self.path, self.name.lower()) + '.py', 'w')
                file.write ( new_module_default_template.format(title=self.name.capitalize(), template_name=self.name.lower()))
            else:
                Exception('You have to provide a valid path')
        else:
            raise Exception('You have to provide a valid name')

    def menu ( self ):
        answers = inquirer.prompt( [ inquirer.Text('name', 'What is the new module name? (The name cannot contain special characters)')] )
        self.name = answers['name']

new_module_default_template = \
"""
import os
import inquirer
import subprocess

from core.module import Module

class {title} ( Module ):

    def __init__ ( self, name = '', path = '' ):
        Module.__init__( self, name, path )

    def execute ( self ):
        if self.name != '':
            if  self.path != '':
                pass
            else :
                raise Exception("You have to provide a valid path")
        else:
            raise Exception("You have to provide a valid name")

    def menu ( self ):
        pass

{template_name}_main_template = \\
\"\"\"
\"\"\"
"""