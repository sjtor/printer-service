from http.server import *
from ps_log import Constant
import json
import ps_printer

success_msg = {"code": 20000, "message": "调用成功"}
not_support_msg = {"code": 40005, "message": "服务暂不被支持"}
error_msg = {"code": 50001, "message": "打印失败"}
host = ('localhost', 8918)
log = Constant().getLog()

class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        path = self.path
        log.info("post request uri: " + path)
        if path != '/ps/certificate/_print':
            self.wfile.write(json.dumps(not_support_msg).encode())
            return
        content_len = int(self.headers.get("Content-Length"))
        post_body = self.rfile.read(content_len).decode('utf8').replace("'", '"')
        log.info("request body : " + str(post_body))
        param = json.loads(post_body)
        try:
            self.printToPrinter(param)
            self.wfile.write(json.dumps(success_msg).encode())
        except Exception as e:
            log.error(e)
            self.wfile.write(json.dumps(error_msg).encode())
        except:
            log.error("打印服务异常")
            self.wfile.write(json.dumps(error_msg).encode())


    def printToPrinter(self, param):
        ps_printer.printer()\
            .printFile(param)


if __name__ == '__main__':
    server = HTTPServer(host, RequestHandler)
    server.serve_forever()