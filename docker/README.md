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
Aparecen ene imágenes o contenedores de ene cosas.



