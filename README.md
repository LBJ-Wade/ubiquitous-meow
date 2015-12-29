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
pip install pynbody
pip install -r requirements.txt
```


Totipnat
--------

[Tipsy](http://www-hpcc.astro.washington.edu/tools/tipsy/tipsy.html) is a tool for reading and visualizing numerical simulation snapshots. We will use it to convert snapshot files into tipsy binaries, so that we can load them up in pynbody as well as feed them into Amiga Halo Finder.

Pynbody and Amiga Halo Finder reads files in a tipsy binary format. We won't need tipsy itself, but will need to install `totipnat` in order to convert the snapshot files to tipsy binary.

Installing totipnat can be done by cloning the [tipsy_tools github](https://github.com/N-BodyShop/tipsy_tools) and running `make`. The `totipnat` will be created in the tipsy_tools directory, and can be then moved to your desired location. Wherever you choose, set its path as the variable `TOTIPNAT` in `analysis/conf.py`.


Amiga Halo Finder
-----------------

[Amiga Halo Finder (AHF)](http://popia.ft.uam.es/AHF/Download.html) is a tool that reads tipsy binary files and summarizes the gravitationally bound objects within the snapshot. We will use in preprocessing of our data to produce halos that we will analyze in pynbody. Download AHF at the link and follow the installation instructions.

Install by downloading the tar file, unzipping it using `tar -xzvf ahf-v1.0-084`, entering the directory, and running `make`. It will create a binary called `AHF-v1.0-084` in the `bin` directory, which you can move to your desired location. Wherever you choose, set that path as the variable `AHF` in `analysis/conf.py`.
