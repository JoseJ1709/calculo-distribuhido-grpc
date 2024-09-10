# calculo-distribuhido-grpc

<h2 align="center">
  Ejecución de Aplicacion
</h2>

Para empezar se debe tener ya instalado Python, Java SDK 17 y Maven:

## Confirmacion
En la terminal, ejecute estos scripts, si todo funciona solo se deben ver las versiones:
```bash
python --version
java --version
mvn --version
```

## Instalacion de paketes
En la terminal, diríjase al directorio donde se ecnuentren los paquetes python y ejecute estos scripts:
```bash
pip install grpcio
pip install grpcio-tools
```

## Compilación de Cliente y Server
En la terminal, diríjase al directorio donde se ecnuentren los paquetes python y ejecute estos scripts en terminales separadas:
```bash
python cliente.py
python server.py
```

## Compilacion del proyecto
En una nueva terminal diriaje dentro de la carpeta calculo-grpc/ y ejecute:
```bash
mvn clean install
mvn clean package
```

## Ejecución de los Workers
Ejecute desde la misma ubicacion y en dos terminales disitnas, solamente cambiando el puerto:
```bash
java -jar target/calculo-grpc-1.0-SNAPSHOT-jar-with-dependencies.jar 50052
java -jar target/calculo-grpc-1.0-SNAPSHOT-jar-with-dependencies.jar 50053
```
