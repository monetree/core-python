import logging
import logging
logging.basicConfig(filename='file.txt',level=logging.ERROR)
logging.critical("there is some critical error need to fix it soon")
logging.error("there is an error")
logging.warning("It might be some problem because prog running slow")
logging.info("important info")
logging.debug("some syntax error")