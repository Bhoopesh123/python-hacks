import logging
import sys


def enable_logging(level_logging):

    log_level=logging.getLevelName(level_logging)

    logging.basicConfig(stream=sys.stdout, level=log_level, format='%(asctime)s %(levelname)s:%(message)s')


if __name__ == '__main__':
    enable_logging('DEBUG')

    logging.debug("Harmless debug Message")
    logging.info("Just an information")
    logging.warning("Its a Warning")
    logging.error("Did you try to divide by zero")
    logging.critical("Internet is down")
    var1 = "Hello"
    logging.info(f"Just an information on passing a variable {var1}")
