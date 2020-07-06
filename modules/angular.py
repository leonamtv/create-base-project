import os
import subprocess

class Angular :

    def __init__ ( self, name = '', path = '' ):
        self._create_command = "ng new --directory={} {}"
        self.name = name
        self.path = path

    def exec ( self, skip_boilerplate = False ):
        if self.name != '':
            if  self.path != '':
                if os.path.exists( os.path.join( self.path, self.name )):
                    os.makedirs ( os.path.join( self.path, self.name ) )
                command = self._create_command.format ( os.path.join( self.path, self.name ), self.name )
                cmd = subprocess.Popen(command.split(' '))
                cmd.communicate()
                if skip_boilerplate :
                    pass
                else:
                    pass
            else :
                raise Exception("Caminho do projeto vazio")
        else:
            raise Exception("Nome do projeto vazio.")
