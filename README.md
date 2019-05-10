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
# Freezing Requirements: 'freeze' the current state of the environment packages
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
- Configuration of pip
```
Ref:
https://pip.pypa.io/en/stable/user_guide/#configuration
```
- Config file
    - Per-user:
    ```
    On Unix the default configuration file is: $HOME/.config/pip/pip.conf which respects the XDG_CONFIG_HOME environment variable.
    On macOS the configuration file is $HOME/Library/Application Support/pip/pip.conf if directory $HOME/Library/Application Support/pip exists else $HOME/.config/pip/pip.conf.
    On Windows the configuration file is %APPDATA%\pip\pip.ini.

    There are also a legacy per-user configuration file which is also respected, these are located at:

    On Unix and macOS the configuration file is: $HOME/.pip/pip.conf
    On Windows the configuration file is: %HOME%\pip\pip.ini

    You can set a custom path location for this config file using the environment variable PIP_CONFIG_FILE.
    ```
    - Inside a virtualenv:
    ```
    On Unix and macOS the file is $VIRTUAL_ENV/pip.conf
    On Windows the file is: %VIRTUAL_ENV%\pip.ini
    ```
    - Site-wide:
    ```
    On Unix the file may be located in /etc/pip.conf. Alternatively it may be in a “pip” subdirectory of any of the paths set in the environment variable XDG_CONFIG_DIRS (if it exists), for example /etc/xdg/pip/pip.conf.
    On macOS the file is: /Library/Application Support/pip/pip.conf
    On Windows XP the file is: C:\Documents and Settings\All Users\Application Data\pip\pip.ini
    On Windows 7 and later the file is hidden, but writeable at C:\ProgramData\pip\pip.ini

    Site-wide configuration is not supported on Windows Vista
    ```
    - If multiple configuration files are found by pip then they are combined in the following order:
    ```
    The site-wide file is read
    The per-user file is read
    The virtualenv-specific file is read

    Each file read overrides any values read from previous files, so if the global timeout is specified in both the site-wide file and the per-user file then the latter value will be used.
    ```
- Further configuration of pip and virtualenv
    - Requiring an active virtual environment for pip
    ```
    # Method 1:
    $ vim %APPDATA%\pip\pip.ini
    # or:
    $ vim %HOME%\pip\pip.ini
    # enter:
    
    [global]
    require-virtualenv = true
    
    # Esc & ZZ, save the file and quit.
    
    # Method 2:
    # cd the project dir, and activate the virtual env:
    $ source Scripts\activate
    # and then:
    $ pip config set global.editor vim
    $ pip config set global.require-virtualenv true
    # or:
    $ pip config set global.editor vim
    $ pip config edit  # this enables us to edit the file %APPDATA%\pip\pip.ini
    # appends:
    
    require-virtualenv = true
    
    # Esc & ZZ, save the file and quit.
    
    ```
    - Caching packages for future use
    ```
    $ pip config set download-cache %HOME%\pip\cache
    ```
