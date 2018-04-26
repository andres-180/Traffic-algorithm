listaApps = open("te.txt", "r")
listaAppsCompleta=open("datasetMal.txt", "w")
t=0;
for s in listaApps.readlines():
	s2=s.strip()
	listaAppsCompleta.write("/home/webdev/Android/ArchivosTrafico/Apps/"+s2+'\n')
	t=t+1

print t
listaAppsCompleta.close()
listaApps.close()
