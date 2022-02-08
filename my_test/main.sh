#!/bin/bash

set -eux

# 修改为你的 CSDN_ID
CSDN_ID="sculpta"

python3 preprocess.py
python3 build.py

git add .
git commit -m "update"
git push