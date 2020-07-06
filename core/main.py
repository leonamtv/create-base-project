import inquirer

from sys import argv
from modules.flutter import Flutter

def get_answers ( questions ):
    return inquirer.prompt( questions )

def menu ( path ) :
    answers = get_answers([
        inquirer.List('type', message = "What kind of project would yuou like to create?", 
                              choices = [ "Flutter", "Angular", "Python" ]),
        inquirer.Text('name', "What is the name of the project?"),
    ])

    if answers['type'] == 'Flutter':
        
        sub_answers = get_answers([
            inquirer.Text('boilerplate', "Skip boilerplate? [y/N]")
        ])
        
        flutter_project = Flutter(answers['name'], path)

        if sub_answers['boilerplate'].lower() == 'y':
            flutter_project.exec(skip_boilerplate=True)
        else:
            flutter_project.exec()

    elif answers['type'] == 'Angular':
        pass
    else:
        pass

if __name__ == "__main__":
    if len(argv) > 1 :
        menu( argv[1] )