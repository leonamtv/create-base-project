import os
import inquirer
import subprocess

from core.module import Module

class Angular ( Module ):

    def __init__ ( self, name = '', path = '' ):
        Module.__init__( self, name, path )
        self._create_command = "ng new {}"
        self._skip_boilerplate = False

    def check_if_can_create ( self ):
        command_check_installation = 'which ng'
        output = subprocess.Popen(command_check_installation.split(' '), 
                                  stdout=subprocess.PIPE, 
                                  stderr=subprocess.STDOUT,
                                  cwd='/')
        stdout, _ = output.communicate()
        result = os.path.abspath(stdout.decode().strip('\n'))
        return os.path.isfile(result)

    def execute ( self ):
        if self.check_if_can_create():
            if self.name != '':
                if  self.path != '':
                    if not os.path.exists( self.path ):
                        os.makedirs ( self.path )
                    command = self._create_command.format ( self.name )
                    cmd = subprocess.Popen(command.split(' '), cwd=self.path )
                    cmd.communicate()
                    if self._skip_boilerplate :
                        file = open(os.path.join(self.path, self.name, 'src/app/app.component.html'), 'w')
                        file.write(angular_main_template)
                        file.close()
                else :
                    raise Exception("You have to provide a valid path")
            else:
                raise Exception("You have to provide a valid name")
        else:
            raise Exception("Looks like the software didn't find the angular-cli installation in this machine.")

    def menu ( self ):
        answers = inquirer.prompt([
          inquirer.Text('boilerplate', "Skip boilerplate? [y/N]")
        ])

        self._skip_boilerplate = answers['boilerplate'].lower() == 'y'

angular_main_template = \
"""
<html>
    <head>
        <title>{{ title }}</title>
    </head>
    <body></body>
</html>
"""