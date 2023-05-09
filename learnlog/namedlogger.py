import logging
logging.basicConfig(level=logging.INFO) 
logger = logging.getLogger("MILOGGER")
logger.debug("No va a salir")
logger.info("Esto si")
logging.basicConfig(level=logging.DEBUG) 
logger.debug("No va a salir? P2") #NO

for handler in logging.root.handlers:
    logging.root.removeHandler(handler) #ELIMINA EL CONFIG PARECE
logging.basicConfig(level=logging.DEBUG) 
logger.debug("No va a salir? P3") #SI
