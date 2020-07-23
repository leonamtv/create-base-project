import os
import subprocess
import inquirer

from modules.base.module import Module

class Flutter ( Module ):

    def __init__ ( self, name = '', path = '' ):
        Module.__init__( self, name, path )
        self._create_command = """flutter create --project-name={} {}""" 
        self._skip_boilerplate = False      

    def execute ( self ):
        if self.name != '':
            if  self.path != '':
                full_path = os.path.join( self.path, self.name )
                if not os.path.exists( full_path ):
                    os.makedirs ( full_path )
                command = self._create_command.format ( self.name, full_path )
                cmd = subprocess.Popen(command.split(' '))
                cmd.communicate()
                if self._skip_boilerplate :
                    file = open ( os.path.join(full_path, 'lib/main.dart'), 'w' )
                    file.write(flutter_main_template.format(title = str(self.name)))
                    file.close()
            else :
                raise Exception("Caminho do projeto vazio")
        else:
            raise Exception("Nome do projeto vazio.")


    def menu ( self ) :
        answers = inquirer.prompt([
          inquirer.Text('boilerplate', "Skip boilerplate? [y/N]")
        ])

        self._skip_boilerplate = answers['boilerplate'].lower() == 'y'

flutter_main_template = \
"""
import 'package:flutter/material.dart';

void main() {{
  runApp(
    MaterialApp (
      title: "{title}",
      home: Home()
    )
  );
}}

class Home extends StatelesWidget {{
  @override
  Widget build(BuildContext context) {{
    return Scaffold ();
  }}
}}
"""