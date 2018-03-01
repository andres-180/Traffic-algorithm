import subprocess
import time
import os

#instalacion de una app
#time.sleep(5)
os.chdir("Sdk/platform-tools")











#obtencion de paquetes
subprocess.Popen(['./adb root'], shell=True)
prueba='./adb shell "pm list packages"'

packages=subprocess.Popen([prueba],shell=True)
out, err = packages.communicate()
#print "este es el pk "+out
"""for element in out:
	print element 
	if "chess" in element:
    		print ("lo encontre")
		print element"""




"""time.sleep(20)
archivo=open("datasetPrueba.txt", "r")
linea=archivo.read()
while linea!="":
	ruta=linea
	instalador="./adb install " + linea
	print(instalador) 
	subprocess.Popen([instalador], shell=True)
	detenerAVD="./adb kill-server"
	subprocess.Popen([detenerAVD], shell=True)
	reconectarHost="./adb reconnect"
	subprocess.Popen([reconectarHost], shell=True)
	reconectarAVD="./adb reconnect device"
	subprocess.Popen([reconectarAVD], shell=True)
	
	
	linea=archivo.read()
archivo.close() """
