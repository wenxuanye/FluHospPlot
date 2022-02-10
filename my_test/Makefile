#mcandrew;

PYTHON:=python3 -W ignore

COMMITprefix:= Flu Hosp data generated on 
COMMITsuffix:=$(shell date +"%Y-%m-%d")

COMMIT:=$(COMMITprefix) $(COMMITsuffix)
git:
	git checkout dev
runall: preprocess build git

preprocess:
	$(PYTHON) preprocess.py

build:
	$(PYTHON) build.py

git:
	git config --global user.email "wey420@lehigh.edu"
	git config --global user.name "wenxuanye"
	git add . && git commit -m "$(COMMIT)" && git push
