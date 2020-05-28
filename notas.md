# Analisis de los archivos

Apertura con h5py
archivo `data/ITPCdata15Ch10Rep.mat` contiene datos de forma directa.
El archivo `data/ITPCdata15Ch5Rep.mat` no mostraba contenidos, probablemente sea una variable directa y no un struct.


_ch10rep.mat_
* imagenes: float64 nd-array (10860, 717, 21)
* tarea: int (10860,1) -> clases 1, 2, 3
* sujeto:  int (10860,1) ->

evento 1 y sujeto 1: 150 señales

# Pendientes
* Quedaría implementar el modelo de la Dani y obtener el resultado por sujeto
* Explorar la distancia intersujetos


