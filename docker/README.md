# Docker
Como especie de contenedor que tiene todo, incluyendo cosas del Sistema Operativo creo, al parecer es como una máquina virtual, creo
Tiene el código, las dependencias, los archivos de configuración, bla, bla, bla

Con contenedores la única dependencia es el *runtime* de docker y puede ser automatizado por los *pipelines* que tienen algunos proveedores de servicios.

### Imagen
Es una cosa que tiene las dependencias, el código , bla y es lo que se comparte

### Container
Es como una lasaña de imágenes, puedo tener una imagen de linux + una de python + ... + una de mi programa. Los container pesan poco, especialmente comparado con las máquinas virtuales.

### Docker vs VM
Las VM tiene virtualizado las aplicaciones + kernel. En Docker se virtualizan sólo las aplicaciones. Sobre el kernel ocupa el del sistema operativo sobre el que se está utilizando, por eso pesan poco, o mucho menos.

## Docker Desktop
Bajar docker desktop, buscar en google. Es una máquina virtual en Linux y permite ejecutar containers y acceder al sistema de archivos + la red. Le trae:

* Docker Compose, que tiene el CLI y otras cosas más
* Tiene paquetes preinstalados, como para Debian, Fedora, Ubuntu, Arch

## Docker Hub
Aparecen ene imágenes o contenedores de ene cosas, con distintas versiones, etc etc.

A la derecha de cada imagen hay un comando
`docker pull IMAGEN` , por ejemplo `docker pull python`

## Comandos para bajar/borrar

* `docker images`
Muestra la lista de imágenes
    * REPOSITORY: la cosa
    * TAG: un tag
    * IMAGE ID: identificador único
    * CREATED: obvio
    * SIZE: obvio
* `docker pull XXX`: Baja el archivo de imagen de XXX
* `docker pull XXX:YY` : Baja XXX pero la versión YY. Puedo tener el mismo XXX con distintas versiones. En docker hub se pueden buscar las imágenes, hay ene oficiales.
    * en M1 a veces falla la cosa y te dice algo críptico del estilo `no matching manifest for linux/arm64/v8 in the manifest list entries`, en ese caso hay que hacer `docker pull --platform linux/x86_64 XXX:YY` , ni idea porque
* `docker image rm XXX:YY` : Elimina una imagen . Probando parece que también se puede hacer `docker image rm IMAGE_ID` con IMAGE_ID el image_id de la imagen, parece que incluso funciona poniendo las primeras letras de ese corcho.

## Crear un contenedor en base a una imagen
* Primero necesitamos una imagen, por ejemplo la de Mongo
`docker pull mongo`

* Ahora `docker create mongo` y eso crea la cosa. Y va a tirar un id enorme del container alfo asi 695aad5de78c33b35f02d2652fa03cf6fd7acabb32c4fb186911b300956ef8b7
* Ahora para correrlo tenemos `docker start 695aad5de78c33b35f02d2652fa03cf6fd7acabb32c4fb186911b300956ef8b7
`
* con `docker ps` se puede ver lo que está corriendo
    * DOCKER_ID es como un resumen del ID
    * IMAGE es la imagen base
    * COMMAND es lo que utiliza el contenedor para ejecutarse
    * CREATED
    * STATUS 
    * PORT : El puerto
    * NAMES : Nombre del contenedor
* con `docker stop 695aad5de78c` lo freno
* `docker ps` me va a parecer vació porque no está corriendo
* `docker ps -a` Muestra todos los contenedores que existen aunque no estén funcionando
* Podemos referirnos también por el nombre y eliminarlo
* `docker create --name NOMBREQUELEQUIEROPONER mongo` 
* **port mapping** Si quiero acceder a mongo, no voy a poder, a pesar que sale un puerto en el `ps`, entonces debemos mapear un puerto del computador al puerto del contenedor
    * Esto se hace `docker create -p27017:27017 --name monguito mongo` en el -p el primer número (que va pegado) es el puerto en mi máquina y el segundo es el puerto en el contenedor y si hago `docker start monguito`y después `docker ps` en PORTS me va a salir `0.0.0.0:27017->27017/tcp` que es de nuestra máquina (0.0....) al container
    * Puedo no hacer esto pero docker es el que decide que hacer. Podría hacer `docker create -p27017 --name monguito2 mongo`y ahí va hacer `0.0.0.0:53977->27017/tcp` o sea lo pone en cualquier lado
* `docker logs monguito`te muestra logs, pero estático. Si quieremos que escuche eternamente `docker logs monguito --follow` y se sale con CTRL C
* `docker run mongo` : Hace ene cosas:
    * Busca la imagen, si no la encuentra, la baja
    * Crea el contenedor
    * Inicia el contenedor
    * y de ahí se va a quedar pegado en los logs, si apreto CTRL C apago todo
    * Para evitar lo anterior está el modo dettached y eso es `docker run -d mongo` .
    * Acá le puedo aplicar todas las opciones de `docker create`, algo así `docker run --name monguito -p27017:27017 -d mongo` y listeilor

## Conexión a los contenedores
Vamos a usar el archivo `index.js` que es una aplicación de node que se conecta a una BD mongo y que está en la raíz de este repo

* En dockerhub buscamos mongo ya que necesitamos ciertos parámetros . Abajo en <a href="https://hub.docker.com/_/mongo">Docker Hub (Mongo)</a> salen instrucciones para configurarlo. **Todos los contenedores se configuran distinto**
* En este caso necesitamos variables de entorno MONGO_INITDB_ROOT_USERNAME, MONGO_INITDB_ROOT_PASSWORD
* Ahora descargamos la imagen de mongo con `docker pull mongo`
* Ahora creamos el contenedor con `docker create -p27017:27107 --name monguito -e MONGO_INITDB_ROOT_USERNAME=nico -e MONGO_INITDB_ROOT_PASSWORD=password mongo`
* Lo podemos iniciar con `docker start monguito` y verificamos con `docker ps`
* Creamos un archivo Dockerfile y ahí escribimos las instrucciones para que se cree el contenedor
    * Imagen base es node
    * Creo ruta en el contenedor (no la máquina mia)
    * Todo lo que escribamos va a ir ahí
    * En copy se pone la ruta de mi pc y después la del contenedor
    * expose abre el puerto, en la app era el 3000
    * comando que debe ejecutar para que corra

```
FROM node:18

RUN mkdir -p /home/app

COPY . /home/app

EXPOSE 3000

CMD ["node", "/home/app/index.js"]
```
*
    * ahora los contenedores no necesariamente se pueden comunicar, así que hay que hacer una **red de contenedores** . Podemos tener muchas redes con distintos contenedores.
    * `docker network ls` : lista redes
    * `docker network create mired` : con mired es el nombre de la red y nos va a escupir un mega id.
    * para eliminar una red `docker network rm mired` (esto no viene ahora, es pa saber)
    * corremos `docker build NOMBREIMAGEN:TAG RUTA` o en el ejemplo `docker build -t miapp:1 .` (el . es la ruta actual)
    * con `docker images` chequeamos que esté OK
    * ahora tengo que enlazar los contenedores a la red. El que tenía antes ya no sirve, tengo que hacerlo nuevamente
    * `docker create -p27017:27017 --name monguito --network mired -e MONGO_INITDB_ROOT_USERNAME=nico -e MONGO_INITDB_ROOT_PASSWORD=password mongo`
    * Creamos el contenedor de la aplicacion que recien pusimos en una imagen `docker create -p3000:3000 --name chanchito --network mired miapp:1`
    * ahora partimos los contenedores `docker start monguito` y `docker start chanchito`
    * corremos la app en el navegador en localhost:3000 y localhost:3000/crear
    * Ahora podemos ver los logs `docker logs chanchito`


