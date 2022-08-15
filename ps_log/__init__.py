from ps_log import logger


class Constant(object):
    __log = None

    def getLog(self):
        if self.__log is None:
            self.__log = logger.PyLogger("ps-printer-plug.log").logger
        return self.__log
