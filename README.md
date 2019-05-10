# practice_of_the_hitchhikers_guide_to_python

Practice of the Hitchhiker's Guide to Python

### Introduction

> Practice of the Hitchhiker's Guide to Python

## Common Operations

- Update `pip`
```
$ python -m pip install -U pip
``` 
- List installed packages
```
$ pip list
```
- Install package `pipenv` **in the mode of user installation**
```
# for the user installation scheme (with the --user option)
$ pip install --user pipenv
```
- Check the `site.USER_BASE` variable
> Path to the base directory for the user site-packages.
```
# for Linux or MacOS:
$ python -m site --user_base
# output:
# eg. ~/.local
# then, we should add ~/.local/bin to PATH. (need to edit the file ~/.bashrc)

# for Windows:
$ py -m site --user_base
# output:
# eg. C:\Users\Username\AppData\Roaming\Python37\site-packages
# then, we should add C:\Users\Username\AppData\Roaming\Python37\Scripts to PATH.
```
- Running on `pipenv`
```
# install package on pipenv
$ pipenv install packagename

# running on pipenv
$ pipenv run python main.py
```
- Install package `virtualenv`
```
$ pip install virtualenv
```
- Create a new project with `virtualenv`
```
$ virtualenv new_project
$ cd new_project
# then, we should set C:\Program Files\Python37\python.exe as VIRTUALENVWRAPPER_PYTHON
# activate the virtual env
$ source Scripts\activate[.bat]
# deactivate the virtual env
$ Scripts\deactivate.bat
```
- Running on `virtualenv`
```
# install package requests
$ pip install requests
# 'freeze' the current state of the environment packages
$ pip freeze > requirements.txt
# restore or reoccur the frozen environment according to the requirements.txt
$ pip install -r requirements.txt
```
- Install package `virtualenvwrapper`
```
# for Linux or MacOS:
$ pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs  # or, we can add this line in the file ~/.bashrc
$ source /usr/local/bin/virtualenvwrapper.sh

# for Windows:
$ pip install virtualenvwrapper-win
# then, we should set %USERPROFILE%\Envs as WORKON_HOME
```
