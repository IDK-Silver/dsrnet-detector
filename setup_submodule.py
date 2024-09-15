import subprocess

subprocess.run(["git", "submodule", "init"])
subprocess.run(["git", "submodule", "update", '--recursive'])
with open('src/dsrnet_detector/extern/DSRNet/__init__.py', 'w') as export:
    export.write("")
