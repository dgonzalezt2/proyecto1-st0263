## PROYECTO 1: SISTEMA DE ARCHIVOS DISTRIBUIDOS

 Integrantes:

* [Juan Esteban Castro García](https://github.com/castro-1)
* [David González Tamayo](https://github.com/dgonzalezt2)

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
 
