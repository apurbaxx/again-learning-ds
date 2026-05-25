import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%M-%D %H:%M:%S",
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("ArithmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a} and {b} to {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a} and {b} to {result}")
        return result
    except ZeroDivisionError:
        logger.error(f"Dividing by zero failed")
        return None

divide(2,0)