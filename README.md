Setup
=====

Docker
------

The project is set up to be able to be run in a docker container for easiest setup. Install docker for your system and then run `docker build <your-docker-project-name> .` Learn about docker somewhere else, not here.

Run a container, using the `-v` option to mount your data directory to the container's `/data`.
 The Jupyter notebook for this project will be running on port 8888 of the container. To find out what port the jupyter server is running on in your system, do `docker ps`, and then head to that location in your browser.

If you are using a VM and have your data directory on an external drive, you need to mount that drive in your VM to access it in the container. To do that with docker-machine on mac, with the VM stopped run

`VBoxManage sharedfolder add default --name Volumes  --hostpath /Volumes --automount`

Then start the default VM, ssh into it using `docker-machine ssh default`, and run the following two commands (copied from [here](https://github.com/aaronbbrown/docker_home/blob/master/dm_run#L62)).

```
$ sudo mkdir -p /Volumes
$ sudo mount -t vboxsf -o rw,dmode=777,fmode=777 Volumes /Volumes
```

Python Requirements
-------------------

Data analysis in this project is done in Python. To install the Python dependenices, set up a python virtual environment in the top level directory of the repository to keep these installed libraries separate from the rest of your system. If you do not have virtualenv installed, install it with `pip install virtualenv`. Then, create the virtualenv in a new directory named `env/` by running

```
$ virtualenv env
```

Enter the virtualenv by running `source env/bin/activate`.

Now, from inside the virtualenv, install our python dependencies. The dependencies are listed in `requirements.txt` and can be installed automatically. However, as of Dec 2015, pynbody won't automatically install numpy. For this reason, run the following commands in this order:

```
pip install numpy
pip install -r requirements.txt
```

Pynbody Issue on Mac OS X
-------------------------

When used inside a virtualenv on OS X, matplotlib for some reason cannot use its default backend which causes problems when initializing the pynbody module. In order to be able to import and use pynbody successfully, you need to update the matplotlib backend _before_ importing pynbody at all, for example to "TkAgg". For this reason, make sure that you call `matplotlib.use("TkAgg")` before pynbody is imported for the first time in a process.


Totipnat
--------

[Tipsy](http://www-hpcc.astro.washington.edu/tools/tipsy/tipsy.html) is a tool for reading and visualizing numerical simulation snapshots. We will use it to convert snapshot files into tipsy binaries, so that we can load them up in pynbody as well as feed them into Amiga Halo Finder.

Pynbody and Amiga Halo Finder reads files in a tipsy binary format. We won't need tipsy itself, but will need to install `totipnat` in order to convert the snapshot files to tipsy binary.

Installing totipnat can be done by cloning the [tipsy_tools github](https://github.com/N-BodyShop/tipsy_tools) and running `make`. The `totipnat` will be created in the tipsy_tools directory, and can be then moved to your desired location. Wherever you choose, set its path as the variable `TOTIPNAT` in `analysis/conf.py`.


Amiga Halo Finder
-----------------

[Amiga Halo Finder (AHF)](http://popia.ft.uam.es/AHF/Download.html) is a tool that reads tipsy binary files and summarizes the gravitationally bound objects within the snapshot. We will use in preprocessing of our data to produce halos that we will analyze in pynbody. Download AHF at the link and follow the installation instructions.

Install by downloading the tar file, unzipping it using `tar -xzvf ahf-v1.0-084`, entering the directory, and running `make`. It will create a binary called `AHF-v1.0-084` in the `bin` directory, which you can move to your desired location. Wherever you choose, set that path as the variable `AHF` in `analysis/conf.py`.
