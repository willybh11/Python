# netsh wlan show profiles NETWORKNAME key=clear

import os
import time

os.system('netsh wlan show profiles %s key=clear' %(raw_input('Network Name:\n>>> ')))
time.sleep(10000)
