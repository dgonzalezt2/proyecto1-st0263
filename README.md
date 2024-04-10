## ST0263 Tópicos Especiales en Telemática 

* Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
* Estudiante:
[Juan Esteban Castro García](https://github.com/castro-1), jecastrog@eafit.edu.co
| [David González Tamayo](https://github.com/dgonzalezt2), dgonzalez2@eafit.edu.co

# Nombre de la actividad
## Proyecto 1: Sistema de archivos distribuidos
# Contexto: 

Sistemas distribuidos de archivos: Claves en la era digital 

En la era actual, donde la generación de datos se dispara, los sistemas distribuidos de archivos son esenciales para 

* Almacenar: grandes volúmenes de información de forma eficiente. 

* Procesar: terabytes o petabytes de datos con rapidez y escalabilidad. 

* Recuperar: archivos de manera confiable y segura. 

Ejemplos como Google File System (GFS) y Hadoop Distributed File System (HDFS) demuestran su eficacia en entornos informáticos modernos. 

En resumen, los sistemas distribuidos de archivos son una tecnología clave para la gestión eficiente de datos en la era digital. 

# Descripción:  

Un sistema de archivos distribuidos permite compartir y acceder de forma concurrente un conjunto de archivos almacenados en diferentes nodos. Uno de los sistemas más maduros, vigente y antiguo de estos sistemas es el NFS (Network File System) desarrollado en su momento por Sun Microsystems y que hoy en día es ampliamente usado en sistemas Linux. Hay otros sistemas de archivos distribuidos como AFS (Andrew File System) y SMB (Server Message Block) conocido como CIFS. 

# Arquitectura del sistema: 

![image](https://github.com/dgonzalezt2/proyecto1-st0263/assets/81880494/a192a1c4-7cf6-42c4-ad08-cc1628279bb9)

# Relación y comunicación entre los componentes 

1. Cliente <-> Maestro (NameNode): 

El cliente interactúa con el NameNode maestro cuando necesita realizar operaciones de archivos, como subir un nuevo archivo. El maestro responde indicando los DataNodes específicos (esclavos) donde se deben almacenar las particiones del archivo. Esta comunicación se hace a través de API REST. 

2. Maestro <-> Seguidor (NameNode secundario): 

El NameNode maestro (líder) se comunica continuamente con el NameNode seguidor para sincronizar el estado del sistema de archivos y los metadatos. Esta comunicación garantiza que el seguidor esté preparado para asumir el rol de maestro en caso de fallo del líder. La sincronización del estado se realiza a través de una API REST. 

3. Esclavo (DataNode) <-> Maestro (NameNode): 

Los DataNodes (esclavos) se comunican regularmente con el NameNode maestro, enviando heartbeats y reportes de los bloques de datos. La comunicación se realiza mediante API REST. 

4. Cliente <-> Esclavo (DataNode): 

Para la transferencia de archivos, los clientes interactúan directamente con los DataNodes utilizando gRPC. 

### Ambiente de ejecución AWS

![image](https://github.com/dgonzalezt2/proyecto1-st0263/assets/81880494/b9721a5a-95fe-4747-8244-6b04d413d65c)
http://3.94.244.87

### Video Sustentación

[Video](https://youtu.be/EMdCnKGSY8k)

### Referencias:

* [HDFS Architecture](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html)
* [Round-Robin](https://www.linkedin.com/advice/0/how-does-round-robin-algorithm-schedule-tasks-irh4c)

* [GFS](https://es.wikipedia.org/wiki/Google_File_System) 
* [The Google File System](https://g.co/kgs/XzwmU76)

* [HDFS](https://es.wikipedia.org/wiki/Hadoop_Distributed_File_System)
* [The Hadoop Distributed File System](https://ieeexplore.ieee.org/document/5496972)
