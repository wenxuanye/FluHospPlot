#mcandrew;

PYTHON:=python3 -W ignore

COMMITprefix:= Flu Hosp data generated on 
COMMITsuffix:=$(shell date +"%Y-%m-%d")

COMMIT:=$(COMMITprefix) $(COMMITsuffix)

runall: git1 preprocess build git
git1:
	git checkout dev
preprocess:
	$(PYTHON) preprocess.py

build:
	$(PYTHON) build.py

git:
	git add . && git commit -n -m "$(COMMIT)" && git push origin main
