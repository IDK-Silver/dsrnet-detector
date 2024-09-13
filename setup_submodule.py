import subprocess

subprocess.run(["git", "submodule", "init"])

with open('src/dsrnet_detector/extern/DSRNet/__init__.py', 'w') as export:
    export.write("")

subprocess.run(["ls"])