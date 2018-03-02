import subprocess
import time
import os

#preparacion del directorio del emulador
time.sleep(20)
os.chdir("Sdk/platform-tools")

#instalacion de una app
archivo=open("datasetPrueba.txt", "r")

for g in archivo.readlines():
	instalador="./adb install " + g
	print(instalador) 
	subprocess.Popen([instalador], shell=True)
	time.sleep(60)
	detenerAVD="./adb kill-server"
	subprocess.call([detenerAVD], shell=True)
	reconectarHost="./adb reconnect"
	subprocess.call([reconectarHost], shell=True)
	reconectarAVD="./adb reconnect device"
	subprocess.call([reconectarAVD], shell=True)
	time.sleep(10)
	
	#obtencion de paquetes
	subprocess.Popen(['./adb root'], shell=True)
	prueba='./adb shell "pm list packages"'

	packages=subprocess.Popen([prueba],shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = packages.communicate()
	f = open ('paquetes.txt','w')
	f.write(out)
	f.close()

	archivoPack=open('paquetes.txt','r')
	nombreArchivoPartido=g.split('.')
	nombreArchivo=nombreArchivoPartido[0]

	for s in archivoPack.readlines():
		if nombreArchivo in s:
			print ("lo encontre")
			print "El paquete es: "+s
		
		print s

archivoPack.close()


archivo.close()







#for element in out:
#	print element 
#	if "chess" in element:
#    		print ("lo encontre")
#		print element



