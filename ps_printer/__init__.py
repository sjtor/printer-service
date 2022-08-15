from ps_printer import PsPrinter


class Constant(object):
    printer = None


def printer():
    if not Constant.printer:
        Constant.printer = PsPrinter.Printer()
    return Constant.printer
