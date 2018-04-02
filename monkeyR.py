# -*- coding: utf-8 -*-
import subprocess
import os
from instalacionApp import getPaquete

nombrePaquete=getPaquete()
os.chdir("../Sdk/platform-tools")	
comandoMonkey="./adb -e shell monkey --ignore-crashes -p "+nombrePaquete+" -v --throttle 6000 300"
subprocess.call([comandoMonkey],shell=True)
