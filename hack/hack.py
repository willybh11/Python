import sys
import time
from random import *
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple

colors = [G,W]
if raw_input("BEGIN HACK: (y/N)") == "y":
    while 1:
        sys.stdout.write(colors[randint(0,1)]+(str(randint(0,1)))+W)
        sys.stdout.flush()
        time.sleep(0.0005)
