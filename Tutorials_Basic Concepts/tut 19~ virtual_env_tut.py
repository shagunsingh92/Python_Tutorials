'''
1. If we are creating a project we should ideally create it in a virtual environment and should create
a requirements file for that project.

2. Virtual environments are important because the python packages and modules keep getting updated and if
we want to pass on our project to someone in future, we should create our program in a virtual environment
and should keep the list of all the required modules in the requirement file. By doing so at a later point
we can simply give this requirement file to another person who can install exactly the version of modules
which are required to run that particular program.

3. inorder to create a virtual environment, one should create a new folder> open powershell in that folder>
run command " virtualenv name_of_virtual_env"

4. Once a virtual environment is created we need to activate it in order to work in the environment. In order
to do this run these commands : ".\name_of_virtual_env\Scripts\activate"

5. After getting into the virtual environment one can create a requirements file by running the following command
"pip freeze > requirement_file_name.txt" (take care of the spaces else it will throw error)

6. In order to work in a virtual environment one can open the virtual environment in pycharm by passing in
the path of the virtual environment and can create files in that project

7. in order to install new modules in a virtual environment one can run the following command in the powershell
window on the virtual environment folder or in the terminal of the pycharm : "pip install module_name"

8. If one wants the virtual environment to have all the site packages of the system interpreter, we can
run the following command : "virtualenv --system-site-packages virtual_file_name" at the time of creating
a virtual environment i.e the very first command.

9. If someone wants to install all the packages mentioned in a requirement file then they should use the
following command: "pip install -r .\ requirement_file_name.txt"

'''