import logging
 # DEBUG: Es para revisar, esta variable ahora es tanto
 # INFO : Información que partió está función o algo así
 # WARNING : No es problema, pero puedo serlo
 # ERROR : Algo anduvo mal, pero no crítico, por ejemplo una conexión
 # CRITICAL: Quedó la crema
 # https://docs.python.org/3/library/logging.html

logging.basicConfig(level=logging.DEBUG) 
# forma rara de hacerlo
logging.log(logging.INFO, "This is our message")
#forma más simple
logging.info("Hola")
logging.warning("Hola!")
logging.error("Hola!!")
logging.critical("Hola !!!!!!")
