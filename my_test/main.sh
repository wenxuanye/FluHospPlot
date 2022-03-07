#!/bin/bash

set -eux

# today
TODAY=$(date +%Y%m%d)
python3 preprocess.py
python3 build.py

git config --global user.email "wey420@lehigh.edu"
git config --global user.name "wenxuanye"

git pull
git add .
git checkout main
git merge dev

git commit -m "$TODAY Git actions auto run"
git push -u origin main
# push the update to main branch
# git push