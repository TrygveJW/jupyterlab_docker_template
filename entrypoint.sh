#!/bin/bash

pwd

if [ -d "./.py_env" ]; then
    python3 -m ipykernel install --user --name=.py_env
fi

jupyter lab --port=8888 --no-browser --ip=0.0.0.0
