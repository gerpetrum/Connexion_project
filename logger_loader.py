# add logging to the project
import os
import logging.config
import yaml


def load_logger_config(
    default_path='config/logger.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        try:
            logging.config.dictConfig(config)
            logging.info("Logging configuration loaded successfully")
        except BaseException as be:
            logging.basicConfig(level=default_level, format='%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d %(message)s')
            logging.warning("Could not create log file {}".format(str(be)))
    else:
        logging.basicConfig(level=default_level, format='%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d %(message)s')
        logging.warning("Could not create log file")


