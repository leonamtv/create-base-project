import os
import subprocess

flutter_main_template = """import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp (
      title: '{}',
      home: Home()
    )
  );
}

class Home extends StatelesWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold ();
  }
}

"""

class Flutter :

    def __init__ ( self, name = '', path = '' ):
        self._create_command = """flutter create --project-name={} {}"""        
        self.name = name
        self.path = path

    def exec ( self, skip_boilerplate = False ):
        if self.name != '':
            if  self.path != '':
                full_path = os.path.join( self.path, self.name )
                if os.path.exists( full_path ):
                    os.makedirs ( full_path )
                command = self._create_command.format ( self.name, full_path )
                cmd = subprocess.Popen(command.split(' '))
                cmd.communicate()
                if skip_boilerplate :
                    file = open ( os.path.join(full_path, 'lib/main.dart'), 'w')
                    file.write(flutter_main_template)
                    file.close()
            else :
                raise Exception("Caminho do projeto vazio")
        else:
            raise Exception("Nome do projeto vazio.")

