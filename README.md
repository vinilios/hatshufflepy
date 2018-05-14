hatshufflepy
============

Cython wrapper for the 
[hat_shuffle_implementation](https://bitbucket.org/JannoSiim/hat_shuffle_implementation/src/lib/)
mixnet. 

Python
======

The module requires **Python 2.7**.

Installing hatshufflepy
==================

### From PyPI

1. Install Dependencies:

```bash
sudo apt-get install build-essential git libboost-all-dev cmake libgmp3-dev libssl-dev libprocps4-dev pkg-config python-pip
```

2. Install hatshufflepy

```bash
pip install hatshufflepy
```

3. Set LD_PRELOAD

Add to `.bashrc`:

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprocps.so
```

or set an environmental variable for the current session

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprocps.so
```


### From source


1. Install dependencies:

```bash
sudo apt-get install build-essential git libboost-all-dev cmake libgmp3-dev libssl-dev libprocps4-dev pkg-config python-pip
pip install cython setuptools
```

2. Install hatshufflepy

```bash
sudo python setup.py install
```

3. Set LD_PRELOAD

Add to `.bashrc`:

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprocps.so
```

or set an environmental variable for the current session

```bash
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libprocps.so
```

***So far we have tested these only on Ubuntu 16.04 LTS.***
