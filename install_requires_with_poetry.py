from subprocess import run
from sys import executable


run(f"{executable} -m pip install --upgrade pip".split())
run(f"{executable} -m pip install poetry".split())
run(f"poetry env use {executable}".split())
run(
    "poetry export -f requirements.txt --output requirements.txt --without-hashes".split()
)
run(f"{executable} -m pip install -r requirements.txt".split())
run("rm -f requirements.txt".split())
