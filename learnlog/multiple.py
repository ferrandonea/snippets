import logging

# Configurar el logger
logger = logging.getLogger("MiLogger")
logger.setLevel(logging.DEBUG)

# Formateo de la salida del log
#log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_format = logging.Formatter("%(levelname)-8s: \t %(asctime)s %(filename)s %(funcName)s %(lineno)s - %(message)s")
#logging.basicConfig(level=logging.DEBUG, format=f"%(levelname)-8s: \t %(filename)s %(funcName)s %(lineno)s - %(message)s")
# Handler para escribir en el archivo
file_handler = logging.FileHandler('mi_app.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

# Handler para mostrar en la consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(log_format)
logger.addHandler(console_handler)

# # Ejemplo de uso del logger
# logger.debug("Este es un mensaje de nivel DEBUG")
# logger.info("Este es un mensaje de nivel INFO")
# logger.warning("Este es un mensaje de nivel WARNING")
# logger.error("Este es un mensaje de nivel ERROR")
# logger.critical("Este es un mensaje de nivel CRITICAL")
