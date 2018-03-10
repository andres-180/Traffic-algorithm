# -*- coding: utf-8 -*-
import subprocess
import time
import os
import sys

#preparacion del directorio del emulador
time.sleep(20)
print os.getcwd()
#instalacion de una app
archivo=open("datasetPrueba.txt", "r")
os.chdir("..")
os.chdir("Sdk/platform-tools")

for g in archivo.readlines():
	try:
		commandR="./adb install " + g 
		commandSE=commandR.strip()
		instalador=commandSE+" > estadoInstalacion.txt"
		print instalador
		install=subprocess.call([instalador], shell=True)
		variableEstado=open("estadoInstalacion.txt", "r")
		fileLineas=variableEstado.readlines()
		variableEstado.close()
		ultimaLinea=fileLineas[len(fileLineas)-1]
		ultimaLineaSE=ultimaLinea.strip()
 		
		if ultimaLineaSE=="Success":	
			time.sleep(60)
			detenerAVD="./adb kill-server"
			subprocess.call([detenerAVD], shell=True)
			reconectarHost="./adb reconnect"
			subprocess.call([reconectarHost], shell=True)
			reconectarAVD="./adb reconnect device"
			subprocess.call([reconectarAVD], shell=True)
			time.sleep(5)
			subprocess.call(["./adb reboot"], shell= True)
			time.sleep(10)
			#obtencion de paquetes
			subprocess.Popen(['./adb root'], shell=True)
			prueba='./adb shell "pm list packages"'

			packages=subprocess.Popen([prueba],shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			out, err = packages.communicate()
			f = open('paquetes.txt','w')
			f.write(out)
			f.close()

			archivoPack=open('paquetes.txt','r')
			nombreArchivoPartido=g.split('.')
			nombreArchivoPartido2=nombreArchivoPartido[0].split("Apps/")
			nombreArchivo=nombreArchivoPartido2[1]
			print "el nombre del archivo es: "+ nombreArchivo
			for s in archivoPack.readlines():
				if nombreArchivo in s:
					paqueteCompleto=s.split(':')
					nombrePaquete=paqueteCompleto[1]
					nombrePaquete2=nombrePaquete.strip()
#ejecucion monkey 
					comandoMonkey="./adb -e shell monkey --ignore-crashes -p "+nombrePaquete2+" -v --throttle 5000 200"
					subprocess.call([comandoMonkey],shell=True)
#completar desinstalacion
					des="./adb shell pm uninstall -k "+nombrePaquete2
					subprocess.call([des],shell=True)
					time.sleep(30)			
					subprocess.call(["./adb reboot"], shell =True)
					time.sleep(10)
					print "finish"
		
				else:
					listaPa = open("paquetesFallidos.txt", "w")
					listaPa.write(g)
					listaPa.close()

			archivoPack.close()
		else:
			listaApps = open("instalacionesFallidas.txt", "w")
			listaApps.write(g)
			listaApps.close()
			print "error con la aplicacion"	
	except IOError as e:
		t = open("errores.txt", "w")
		t.write("I/O error({0}): {1}".format(e.errno, e.strerror)+"\n")
		t.close()

archivo.close()







