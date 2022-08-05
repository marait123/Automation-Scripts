

import subprocess

o = subprocess.run("nmcli device wifi show-password")
print(o)
