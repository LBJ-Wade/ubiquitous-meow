Setup
=====

Python Requirements
-------------------

Data analysis in this project is done in Python. To install the Python dependenices, set up a python virtual environment in the top level directory of the repository to keep these installed libraries separate from the rest of your system. If you do not have virtualenv installed, install it with `pip install virtualenv`. Then, create the virtualenv in a new directory named `env/` by running

```
$ virtualenv env
```

Enter the virtualenv by running `source env/bin/activate`.

Now, from inside the virtualenv, install our python dependencies. The dependencies are listed in `requirements.txt` and can be installed automatically. However, as of Dec 2015, pynbody has some issues with its automatically installing its dependencies including numpy, scipy, and matplotlib. For this reason, run the following commands in this order:

```
pip install numpy
pip install scipy
pip install matplotlib
pip install git+git://github.com/pynbody.pynbody.git
pip install -r requirements.txt
```


Tipsy
-----

[Tipsy](http://www-hpcc.astro.washington.edu/tools/tipsy/tipsy.html) is a tool for reading and visualizing numerical simulation snapshots. We will use it to convert snapshot files into tipsy binaries, so that we can load them up in pynbody as well as feed them into Amiga Halo Finder.

Follow the instructions in the link to install Tipsy.

TODO: Include instruction to install tipsy at a predefined destination that can be used by the python code.


Amiga Halo Finder
-----------------

[Amiga Halo Finder (AHF)](http://popia.ft.uam.es/AHF/Download.html) is a tool that reads tipsy binary files and summarizes the gravitationally bound objects within the snapshot. We will use in preprocessing of our data to produce halos that we will analyze in pynbody. Download AHF at the link and follow the installation instructions.

TODO: Include instruction to install AHF at a predefined destination that can be used by the python code.
