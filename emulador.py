import subprocess
import time
import os

#Inicializacion del abd
os.chdir("..")
os.chdir("Sdk/emulator")
subprocess.Popen(["./emulator -avd Pixel_XL_API_22_3 -port 5560"], shell=True)
os.system("gnome-terminal -x sh -c 'cd ..;cd ..;cd ArchivosTrafico;python instalacionApp.py; exec bash'")




