#!/usr/bin/python3

import subprocess
print("content-type: text/html")
print()

print(subprocess.getoutput("sudo docker rm -f $(sudo docker ps -a -q)"))
