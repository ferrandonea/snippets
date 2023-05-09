import logging
import datetime as dt

today = dt.datetime.today()
filename = f"{today.year:02d}-{today.month:02d}-{today.day:02d}.log"

logging.basicConfig(level=logging.DEBUG, format=f"%(levelname)-8s: \t %(filename)s %(funcName)s %(lineno)s - %(message)s")



logger = logging.getLogger("MILOG")
file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s - %(created)f %(filename)s %(funcName)s %(process)d %(threadName)s")

logger.addHandler(file_handler)

logger.debug("Un debug")
logger.info("Una info")
logger.warning("Algo crítico")

def hola():
    logger.info("Test hola")