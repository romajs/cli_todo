#!/bin/bash -e

virtualenv env --python=python2.7;
source env/bin/activate && pip install --editable ../;
source env/bin/activate && pip install click;

# to test enviroment
source env/bin/activate && pip install pytest;
