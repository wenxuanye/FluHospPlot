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
	git add . && git commit -n -m "$(COMMIT)" && git push
