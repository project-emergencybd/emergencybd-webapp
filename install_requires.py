from subprocess import run
from sys import executable

run(f"{executable} -m pip install --upgrade pip".split())
run(f"{executable} -m pip install -r requirements.txt".split())
