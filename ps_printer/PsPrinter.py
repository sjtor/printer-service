import datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtCore import *
from ps_log import Constant
import threading
import sys

log = Constant().getLog()

def toString(param, key):
    val = param.get(key)
    if key == "checkDate":
        pass
    if not val:
        return ""
    if isinstance(str, type(val)):
        if key == "checkDate":
            return val[:16]
        return val
    if isinstance(datetime.datetime, type(val)):
        return datetime.time.strftime("\'%Y-%m-%d %H:%M\'", val)
    else:
        if key == "checkDate":
            return str(val)[:16]
        return str(val)

class Printer():
    files = []
    weight = QFont.DemiBold

    def __init__(self):
        self.app = QApplication(sys.argv)
        t = threading.Timer(1, function=self.__start)
        t.start()

    def __close__(self):
        self.app.exec_()

    def __start(self):
        if self.files:
            log.info("start print...")
            try:
                param = self.files.pop(0)
                self.__printText(param)
            except Exception as e:
                log.error(e)
            except :
                log.error("打印机调用失败.")
            log.info("print job end.")
        t = threading.Timer(1, function=self.__start)
        t.start()

    def __printText(self, param):
        printer = QPrinter()
        painter = QPainter()
        painter.begin(printer)
        # 方法一:
        painter.drawLines([QLine(QPoint(0, 2), QPoint(180, 2))])
        font = painter.font()
        font.setFamily("FangSong")
        font.setWeight(self.weight)
        painter.setFont(font)
        doc = "单号: " + toString(param, "workOrderNo")
        painter.drawText(0, 15, doc)
        doc = "安全例检合格通知单"
        painter.drawText(0, 30, doc)
        doc = "检验时间: " + toString(param, "checkDate")
        painter.drawText(0, 45, doc)
        doc = "车牌号:   " + toString(param, "vehicleNo")
        painter.drawText(0, 60, doc)
        doc = "例检员:   " + toString(param, "checker")
        painter.drawText(0, 75, doc)
        doc = "运营客车随车携带留存备查"
        painter.drawText(0, 90, doc)
        font.setPointSize(7)
        painter.setFont(font)
        doc = "  (本通知单24小时内报班发车有效)"
        painter.drawText(0, 105, doc)
        painter.drawLines([QLine(QPoint(0, 110), QPoint(180, 110))])
        painter.end()

    def printFile(self, param):
        self.files.clear()
        self.files.append(param)

