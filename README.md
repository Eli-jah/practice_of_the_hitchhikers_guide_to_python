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
# then, we should add ~/.local/bin to PATH. (need to edit file ~/.bashrc)

# for Windows:
$ py -m site --user_base
# output:
# eg. C:\Users\Username\AppData\Roaming\Python37\site-packages
# then, we should add C:\Users\Username\AppData\Roaming\Python37\Scripts to PATH.
```
- Running on pipenv
```
# install package on pipenv
$ pipenv install packagename

# running on pipenv
$ pipenv run python main.py
```
