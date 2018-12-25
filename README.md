# Computational Physics
Originally made for Durham University's Department of Physics' course _Laboratory Skills and Electronics_ under the sub-module _Computational Physics_, as part of the coursework in 2017/2018.

This repository contains a series of python assignments centered around Physics problems. The problems are designed with the aim of exposing undergraduate physics students to the world of computational physics, rendering them aware of the multitude of avenues available to them when it comes to problem solving.

The problems in the first 4-5 weeks are rather simple before ramping up in difficulty in the final 3 or 4 weeks.

## Structure
This repository is generally structured as follows:
```bash
├── Week 1
│   ├── CP_1.pdf
│   └── cp_1.py
├── Week 2
│   ├── CP_2.pdf
│   └── cp_2.py
├── Week 3
│   ├── CP_3.pdf
│   └── cp_3.py
├── Week 4
│   ├── cp_4.pdf
│   └── cp_4.py
├── Week 5
│   ├── CP_5.pdf
│   └── cp_5.py
├── Week 6
│   ├── CP_6.pdf
│   ├── cp_6.py
│   └── cp_6.pyc
├── Week 7
│   ├── CP_7.pdf
│   └── cp_7.py
└── Week 8
    ├── CP_8.pdf
    └── cp_8.py
```
The CP_X.pdf files contain the assignment briefs, while the cp_X.py files are the actual solutions

## Pre-Requisites
This work was originally made in [Python 2.7.X](https://www.python.org/downloads/release/python-2715/).
I believe it _should_ work with Python 3 aswell but I have not tested this.

The following packages should be installed:
- [NumPy](http://www.numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [SciPy](https://www.scipy.org/)

These can all be installed via [pip](https://pypi.org/project/pip/) with `pip install --user <package_name>`.
NB underscores should be changed to hyphens when installing.

## Usage
Each of the scripts can be run by simply ensuring you are in the desired `week X` directory and entering `python cp_x.py` into the terminal.
