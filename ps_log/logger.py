import logging
from logging import handlers


class PyLogger(object):
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR
    }

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, filename, level="info", fmt="%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s"):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)
        self.logger.setLevel(self.level_relations.get(level))
        if not self.logger.handlers:
            sh = logging.StreamHandler()
            sh.setFormatter(format_str)
            th = handlers.TimedRotatingFileHandler(filename=filename, encoding="utf-8")
            th.setFormatter(format_str)
            self.logger.addHandler(sh)
            self.logger.addHandler(th)


if __name__ == '__main__':
    log = PyLogger("text.log").logger
    log.debug("this is debug")
    log.info("this is info")
    log.warning("this is warn")
    log.error("this is error.")
