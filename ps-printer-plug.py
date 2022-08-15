from request_handler import PReqiuestHandler
from http.server import *
import os
from ps_log import Constant


def kill(pid):
    cmd = None
    if os.name == "nt":
        # win 系统
        cmd = "taskkill /pid " + str(pid) + "/f"
    elif os.name == "posix":
        # linux 系统
        cmd = "kill " + str(pid)
    else:
        print("Undefined os name")
    try:
        if cmd:
            os.system(cmd)
            print(pid, "killed")
    except Exception as e:
        print(e)


def resetProcess():
    if os.path.exists("ps-printer-plug-pid.txt"):
        f = open("ps-printer-plug-pid.txt", mode="r")
        pid = f.read()
        kill(pid)
        f.close()
        pass
    f = open("ps-printer-plug-pid.txt", mode="w")
    pid = os.getpid()
    print("current pid: ", pid)
    f.write(pid.__str__())
    f.close()


if __name__ == '__main__':
    # resetProcess()
    log = Constant().getLog()
    pid = os.getpid()
    log.info("pid: " + str(pid))
    host = ('localhost', 8918)
    server = HTTPServer(host, PReqiuestHandler.RequestHandler)
    server.serve_forever()

