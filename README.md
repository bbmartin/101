# 101 (the game) 

101 (the game) is a simple game of memory that's time-based. The faster you can locate the pairs from the
cards laid out face down, the better!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Setting Up

A virtual environment was included in the folder so to get the game running, execute the following commands:

This is assuming that you've cd into the project directory and have installed virtualenv beforehand.

**For Windows**

```
.\venv\Scripts\activate.bat
```

**For Mac & Linux**

```
source <venv>/bin/activate
```

Once activated, execute the following just to make sure that the required packages are installed

```
python -m pip install -r requirements.txt
```

Lastly, start up the game by running

```
python main.py
```

## Required Packages

The packages listed below are for linting and running the game.

* astroid==2.1.0
* colorama==0.4.1
* future==0.17.1
* isort==4.3.4
* lazy-object-proxy==1.3.1
* mccabe==0.6.1
* pyglet==1.3.2
* pylint==2.2.2
* six==1.11.0
* wrapt==1.10.11

## Authors

* Julius Arcega 
* Nigel Padua
* Brandon Martin

## Sources

* [https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/index.html#programming-guide](https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/index.html#programming-guide)
* [https://github.com/bitcraft/pyglet/blob/master/examples/timer.py](https://github.com/bitcraft/pyglet/blob/master/examples/timer.py)