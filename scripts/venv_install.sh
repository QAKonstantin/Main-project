#!/bin/bash
cd ..
FILE=venv/

if [ -d "$FILE" ]; then
    source venv/Scripts/activate &&
    pip install -U pip &&
    pip install -Ur requirements.txt
else
    python3 -m venv venv &&
    source venv/Scripts/activate &&
    pip install -U pip &&
    pip install -Ur requirements.txt
fi