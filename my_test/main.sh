#!/bin/bash

set -eux


python3 preprocess.py
python3 build.py

git config --global user.email "wey420@lehigh.edu"
git config --global user.name "wenxuanye"

git add .
git commit -m "update"
git push