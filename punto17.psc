Algoritmo punto17 
	escribir "velocidad vehiculo_uno (Km/h)" 
	leer vehiculo_uno 
	escribir "velocidad vehiculo_dos (Km/h)"
	leer vehiculo_dos 
	escribir "distancia entre ellos"
	leer distancia 
	tiempo<-60*distancia /(vehiculo_uno-vehiculo_dos)
	escribir "tarda en minutos: " abs(tiempo)
FinAlgoritmo
