# see if you can ssh into the pi using a python script
import os
import subprocess
from applescript import tell

# ssh into pi
# tell.app( 'Terminal', 'do script"' + 'ssh pi@raspberrypi.local' + '"')
import os
os.system('open -a Terminal "`pwd`"')
# this opens a terminal in a new window

subprocess.call(['open', '-W', '-a', 'Terminal.app', 'python3', '--args', 'test2.py'])

